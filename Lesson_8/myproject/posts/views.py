from django.shortcuts import render
from .models import post
from django.contrib.auth.decorators import login_required

# Create your views here.
def posts_list(request):
    posts = post.objects.all().order_by('-date') # - sign makes last updated post to the first 

    return render(request , 'posts/post_list.html' , {'posts': posts})

def post_page(request, slug):
    single_post = post.objects.get(slug=slug)
    return render(request,'posts/post_page.html',{'post': single_post})

@login_required(login_url="/users/login/")
def post_new(request):
    return  render(render , 'posts/post_new.html')