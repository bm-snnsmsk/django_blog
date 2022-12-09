from django.contrib import admin
## from post.models import Post
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", 'content', 'publishing_date')
    list_display_links = ('content', 'publishing_date')
    list_filter = ('publishing_date',)
    #list_editable = ('content',) ## title 'da sayfa hata verir
    list_editable = ('title',) ## title list_display_links yer verilmemeli yoksa sayfa hata verir
    search_fields = ('title','content') 
    list_per_page = 1 



# Register your models here.

admin.site.register(Post, PostAdmin)
