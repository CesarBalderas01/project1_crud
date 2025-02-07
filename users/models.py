from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=150)
    user_email = models.EmailField(unique=True)
    user_phone = models.CharField(max_length=16)
    user_date_regis = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

class Assets(models.Model):
    asset_name = models.CharField(max_length=150)
    asset_type = models.IntegerField()