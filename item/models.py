from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Category(models.Model):
    category = models.CharField(max_length=30)
    slug = models.SlugField(max_length=255, unique=True)
    parent_category = models.ForeignKey('self', related_name="main_category", null=True, blank=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.category

# Used proxy model for Category model.
class SubCategory(Category):
    class Meta:
        proxy = True
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'    

    def __str__(self):
        return self.category

class Item(models.Model):
    item_url = models.URLField(max_length = 200)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="sub_category")
    item_date = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.item_url


