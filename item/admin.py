from django.contrib import admin

# Register your models here.
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

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Item)