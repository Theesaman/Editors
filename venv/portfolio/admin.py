from django.shortcuts import render
from django.contrib import admin
from .models import Contact,Portfolio,Blog,Comment,Category,Gallery,Books,About,PortfolioCategory,Portfolio_Single,GalleryCategory
from django.utils.html import format_html
# Register your models here.


admin.site.register((Comment,Category,PortfolioCategory,GalleryCategory))


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    readonly_fields = ['id']
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
  


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('img','title','created_date','content','category')
    readonly_fields = ['id']
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
  

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('img','title','author','description','pages','publication_date','publisher')
    readonly_fields = ['id']
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
  



  
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('img','title','description')
    readonly_fields = ['id']

    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
  


  
@admin.register(Portfolio_Single)
class portfolio_singleAdmin(admin.ModelAdmin):
    list_display = ('title','description','img')
    readonly_fields = ['id']

    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
  



@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('img', 'title', 'created_date')
    readonly_fields = ['id']

    def img(self, obj):
        return format_html(
            '<img width="100" height="100" src="{}" style="border-radius: 50%;" />',
            obj.image.url
        )
    
 
    

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('img','title' ,'description', 'created_date')
    readonly_fields = ['id']
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}" style="border-radius: 50%;"/>'.format(obj.image.url))
  

