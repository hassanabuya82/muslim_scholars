import django
from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id","created_by", "created_on", "image","content","title"]
