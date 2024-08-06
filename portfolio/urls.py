from django.urls import path
from .views import index_view, books_view, PortfolioListView, AboutListView, GalleryListView, BlogListView, ContactFormView, Portfolio_Single_view,BlogDetailView,GalleryDetailView

from . import views
urlpatterns = [
    path('', index_view, name='index-page'),
    path('contact/', ContactFormView.as_view(), name='contact-page'),
    path('books/', books_view, name='books-page'),
    path('portfolio/', PortfolioListView.as_view(), name='portfolio-page'),
    path('about/', AboutListView.as_view(), name='about-page'),
    path('gallery/', GalleryListView.as_view(), name='gallery-page'),
    path('blog/', BlogListView.as_view(), name='blog-page'),
    path('portfolio-single/', Portfolio_Single_view, name='portfolio-single-page'),
    path('blog/<int:pk>',BlogDetailView.as_view(),name="blog-single-page"),
    path('gallery/<int:pk>',GalleryDetailView.as_view(),name="gallery-single-page")
    
]
