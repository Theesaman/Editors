from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"

  
class PortfolioCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name} "


class Portfolio(models.Model):
    title = models.CharField(max_length=70)
    image = models.ImageField(upload_to='Images/portfolio')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(PortfolioCategory,on_delete=models.CASCADE)
    


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"

class Blog(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='Images/blog')
    created_date = models.DateTimeField(auto_now=True)
    content = RichTextField()
    
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self) -> str:
        title = self.title[:10]
        return f"{title}"


class Comment(models.Model):
    image = models.ImageField(upload_to='images/', default='default.jpg') 
    full_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.message} by {self.full_name}"
    
class GalleryCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Images/gallery_category') 
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"
    
class Gallery(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Images/gallery') 
    created_date = models.DateTimeField(auto_now=True)
 
    category = models.ForeignKey(GalleryCategory,on_delete=models.CASCADE)




class Books(models.Model):
    image = models.ImageField(upload_to='Images/books')
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    pages = models.IntegerField()
    publication_date = models.DateField()
    publisher = models.CharField(max_length=255)


    def __str__(self):
        return self.title


class Portfolio_Single(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    image = models.ImageField(upload_to='Images/portfolio_single')
    def __str__(self):
        return self.title 
    

