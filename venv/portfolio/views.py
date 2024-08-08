from django.shortcuts import render
from .models import Contact,Gallery,Books,Portfolio,About,PortfolioCategory,Portfolio_Single,Blog,Comment,Category,GalleryCategory
from django.core.paginator import Paginator
from .forms import ContactForm,CommentForm
from django.views.generic.edit import FormView,FormMixin
from django.views.generic.detail import DetailView
from .bot import send_message
from django.views.generic.list import ListView
from django.urls import reverse

class ContactFormView(FormView):
    template_name = "contact.html"
    form_class =ContactForm
    success_url = "/"
 
    def form_valid(self,form):
      name = form.cleaned_data.get('name')
      email = form.cleaned_data.get('email')
      content = form.cleaned_data.get('content')
      text = f"Name: {name}\nEmail: {email}\ntext: {content}"
      send_message(text)
      form.save()

      
      form.save()
      return super().form_valid(form)
    


def index_view(request):
 return render(request,'index.html')




class AboutListView(ListView):
    model = About
    template_name = 'about.html'
    context_object_name = 'about'



class GalleryListView(ListView):
    model = Gallery
    context_object_name = 'gallery'
    template_name = 'gallery.html'







# def blog_view(request):
#     blogs = Blog.objects.all()
#     context = {
#         "blogs": blogs,
#     }
#     return render(request, 'blog.html', context)


class BlogListView(ListView):
    model = Blog
    paginate_by = 2
    context_object_name = 'blogs'
    template_name = "blog.html"

    def get_queryset(self):
        return Blog.objects.order_by('-created_date')
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
 



def books_view(request):
    books = Books.objects.all()
    context = {
        "books" : books,
    }
    return render(request, 'books.html',context)

# def portfolio_view(request):
#     portfolio = Portfolio.objects.all()
#     context = {
#         "portfolio" : portfolio,
#     }
#     return render(request, 'portfolio.html', context = context)

class PortfolioListView(ListView):
    model = Portfolio
    # paginate_by = 100
    context_object_name = 'portfolios'
    template_name = "portfolio.html"



    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context["categories"] = PortfolioCategory.objects.all()
        return context
    


def Portfolio_Single_view(request):
    portfolio_single = Portfolio_Single.objects.all()
    context = {
        "portfolio_single" : portfolio_single,
    }
    return render(request, 'portfolio_single.html', context)



class GalleryDetailView(DetailView):
    model = GalleryCategory
    template_name = "gallery-single.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["gallery"] = Gallery.objects.filter(category=context.get('category'))

        return context
    
class BlogDetailView(FormMixin,DetailView):
    model = Blog
    template_name = "blog-single.html"
    context_object_name = "blog"
    form_class = CommentForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(blog=context.get('blog'))
        context['comments_count'] = Comment.objects.filter(blog=context.get('blog')).count()

        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.blog = self.object
        form.save()
        return super(BlogDetailView, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog-single-page', kwargs={'pk': self.object.pk})




