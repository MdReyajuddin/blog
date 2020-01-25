from django.contrib import admin
from testapp.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display =['title','author','body','publish','created','updated','status']
    list_filter = ['publish','status','created','author']
    search_fields = ['body','tittle']
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Post,PostAdmin)