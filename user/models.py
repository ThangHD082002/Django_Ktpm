from djongo import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'user'

# class Role(models.Model):
#     name = models.CharField(max_length=50)
#     userrole = models.ManyToManyField(User)
#     class Meta:
#         db_table = 'role'
    