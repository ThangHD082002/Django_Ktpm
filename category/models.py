from djongo import models


class Category(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    class Meta:
        db_table = 'category'
        ordering = ['-created_at']