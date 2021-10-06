from django.contrib import admin
from django import forms
from .models import Category, SubCategory, Item
from django.contrib.admin import SimpleListFilter


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug', 'parent_category')
    def get_queryset(self, request):        
        qs = super(CategoryAdmin, self).get_queryset(request)
        return qs.filter(parent_category_id__isnull=True)  


class SubCategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('category', 'parent_category', )  
    def get_queryset(self, request):        
        qs = super(SubCategoryAdmin, self).get_queryset(request)
        return qs.exclude(parent_category_id__isnull=True)
    def render_change_form(self, request, context, *args, **kwargs):
         context['adminform'].form.fields['parent_category'].queryset = Category.objects.filter(parent_category_id__isnull=True)
         return super(SubCategoryAdmin, self).render_change_form(request, context, *args, **kwargs)


class ItemAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['sub_category'].queryset = SubCategory.objects.exclude(parent_category_id__isnull=True)
        return super(ItemAdmin, self).render_change_form(request, context, *args, **kwargs)

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Item,ItemAdmin)