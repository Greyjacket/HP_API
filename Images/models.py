from django.db import models

class Image(models.Model):
    sku = models.CharField(max_length=16, unique=True)
    root_sku = models.CharField(max_length=16, unique=True)
    old_sku = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=128)
    height = models.IntegerField()
    width = models.IntegerField()
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=10000, null=True, blank=True)
    material_type = models.CharField(max_length=32)
    category = models.CharField(max_length=64)
    sub_category = models.CharField(max_length=64)
    collection = models.CharField(max_length=72)
    sub_collection = models.CharField(max_length=72)
    url = models.CharField(max_length=200, null=True, blank=True)
    path = models.CharField(max_length=400, null=True, blank=True)
    variations = models.CharField(max_length=400, null=True, blank=True)
    variation_group = models.CharField(max_length=20, null=True, blank=True)
    info = models.CharField(max_length=200, null=True, blank=True) #
    validated = models.BooleanField(default=False)
