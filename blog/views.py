from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})

def about(request):
    return HttpResponse('welcome to about page')


# Base templates
def base_template(request):
    return render(request, 'blog/base.html', {})
