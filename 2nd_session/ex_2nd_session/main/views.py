from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.

def mainpage(request):
    return render(request, 'main/mainpage.html')

def interestpage(request):
    return render(request, 'main/interestpage.html')

def new(request):
    return render(request, 'main/new.html')

def post(request):
    posts = Post.objects.all()
    return render(request, 'main/post.html', {'posts':posts})

def create(request):    # 데이터베이스에 저장하는 함수
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.pub_date = timezone.now()
    new_post.weather = request.POST['weather']
    new_post.mood = request.POST['mood'] 
    new_post.body = request.POST['body']

    new_post.save()

    return redirect('detail', new_post.id)

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'main/detail.html', {'post':post})



