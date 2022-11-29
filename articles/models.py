from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Q

from .utils import slugify_title


class ArticleQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookup)


# class ArticleManager(models.Manager):
#     def get_queryset(self):
#         return ArticleQuerySet(self.model, using=self._db)

#     def search(self, query=None):
#         return self.get_queryset().search(query=query)


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=50, blank=True, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.DateField(
        auto_now_add=False, auto_now=False, null=True, blank=True
    )
    objects = ArticleQuerySet.as_manager()

    def save(self, *args, **kwargs):
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Article)
def before_sacing(sender, instance, **kwargs):
    if instance.slug is None:
        slugify_title(instance)


@receiver(post_save, sender=Article)
def make_slug(sender, instance, created, *args, **kwargs):
    if created:
        slugify_title(instance, save=True)
