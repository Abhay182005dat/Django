from django.shortcuts import render , redirect
from .models import post
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def posts_list(request):
    posts = post.objects.all().order_by('-date') # - sign makes last updated post to the first 

    return render(request , 'posts/post_list.html' , {'posts': posts})

def post_page(request, slug):
    single_post = post.objects.get(slug=slug)
    return render(request,'posts/post_page.html',{'post': single_post})

@login_required(login_url="/users/login/")
def post_new(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST , request.FILES) # request.FILES is for the image you are putting that is banner
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return  render(request , 'posts/post_new.html', {'form': form})