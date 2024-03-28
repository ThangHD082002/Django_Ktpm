from djongo import models

# Create your models here.


class InforBook(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField(null=True)
    price = models.FloatField(null=True)


    class Meta:
        db_table = 'inforbook'