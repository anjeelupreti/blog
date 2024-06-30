from django.contrib import admin
from blog.models import Blog

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','add_date']
    search_fields=['id','title','add_date']

