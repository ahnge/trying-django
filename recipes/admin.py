from django.contrib import admin
from .models import Recipe, RecipeIngredient

# Register your models here.
class RecipeIngredientAdmin(admin.StackedInline):
    model = RecipeIngredient
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientAdmin]
    list_display = ["name", "user"]
    readonly_fields = ["created_at", "updated_at"]
    raw_id_fields = ["user"]


admin.site.register(Recipe, RecipeAdmin)
# admin.site.register(RecipeIngredient)
