from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Folder(MPTTModel):
    name = models.CharField(max_length=200, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    class HTTPMeta:
        order_insertion_by = ["name"] 
    
    def __str__(self):
        return self.name
