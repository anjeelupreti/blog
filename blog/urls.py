
from django.urls import path,include
from .views import (
    
    add_blog,
    list_blog,
    view_blog,
    edit_blog,
    delete_blog,
)


urlpatterns = [
    
    path('',list_blog,name='list_blog'),
    path('add/',add_blog,name='add_blog'),
    path('view/<title>',view_blog,name='view_blog'),
    path('edit/<title>',edit_blog,name='edit_blog'),
    path('delete/<title>',delete_blog,name='delete_blog'),
]

