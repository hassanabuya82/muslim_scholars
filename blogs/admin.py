import django
from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id","title","created_by", "created_on", "image","content"]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id","post","name", "email"]

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["id","name","email", "subject", "message"]

@admin.register(ContactEmail)
class ContactEmailAdmin(admin.ModelAdmin):
    list_display = ["id","email"]
