from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from folders.models import Folder 
# Register your models here.

admin.site.register(Folder, DraggableMPTTAdmin)