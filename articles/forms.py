from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"

    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title", f"{title} is already in use")
        return data


# class ArticleForm(forms.Form):
#     title = forms.CharField()
#     content = forms.TimeField()

#     def clean_title(self):
#         cleaned_data = self.cleaned_data
#         print("cleaned_data", cleaned_data)
#         title = cleaned_data.get("title")
#         print("title", title)
#         return title
