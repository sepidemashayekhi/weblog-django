from django.contrib import admin
from .models import  Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=[
        'id','title' , 'slug' , 'author' , 'publish' , 'status',
        ]
    list_filter = [
        'status', 'created', 'publish', 'author'
        ]
    search_fields = [
        'title', 'budy'
        ]
    prepopulated_fields = {'slug': ('title',)}  #creat slug from title 
    
    raw_id_fields = ['author']  # to serch a user 
    
    date_hierarchy = 'publish' 
    
    ordering = ['status', 'publish']