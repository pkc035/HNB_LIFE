from django.db import models

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=20)
    lat  = models.FloatField(default=0)
    lon  = models.FloatField(default=0)
    tags = models.CharField(max_length=20, default='')

    class Meta:
        db_table = 'shops'

# class Gps(models.Model):
#     lat  = models.FloatField()
#     lon  = models.FloatField()
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)

#     class Meta:
#         db_table = 'gps'

# class Tag(models.Model):
#     name = models.CharField(max_length=20)
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)

#     class Meta:
#         db_table = 'tags'