from django.utils.text import slugify
import random


def slugify_title(instance, save=False, new_slug=None):
    if new_slug:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        rand_int = random.randint(1, 500_00)
        slug = f"{slug}-{rand_int}"
        return slugify_title(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance