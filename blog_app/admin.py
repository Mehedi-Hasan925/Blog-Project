from django.contrib import admin
from blog_app import models

# Register your models here.
admin.site.register(models.Blog)
admin.site.register(models.comment)
admin.site.register(models.like)