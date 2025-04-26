from django.shortcuts import render
from .models import post
# Create your views here.
def posts_list(request):
    posts = post.objects.all().order_by('-date') # - sign makes last updated post to the first 

    return render(request , 'posts/post_list.html' , {'posts': posts})
