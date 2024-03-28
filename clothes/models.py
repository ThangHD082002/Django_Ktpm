from djongo import models
from category.models import Category

class Clothes(models.Model):
    name = models.CharField(max_length=224, null=False, blank=False)
    author = models.CharField(max_length=224, null=False, blank=False)
    price = models.IntegerField(default = 0)
    image = models.ImageField(upload_to='images/clothes')
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add = True) 
    updated_at = models.DateTimeField(auto_now = True)
    clothes_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
        db_table = 'clothes'