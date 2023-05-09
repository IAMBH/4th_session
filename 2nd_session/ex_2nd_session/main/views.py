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
    new_post.image = request.FILES.get('image')
    new_post.save()
    return redirect('main:detail', new_post.id)

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'main/detail.html', {'post':post})

def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, 'main/edit.html', {'post':edit_post })

def update(request, id):
    update_post = Post.objects.get(id=id)
    update_post.title = request.POST['title']
    update_post.writer = request.POST['writer']
    update_post.pub_date = timezone.now()
    if request.FILES.get('image'):
        update_post.image = request.FILES.get('image')
    else: 
        update_post.image = update_post.image
    update_post.weather = request.POST['weather']
    update_post.mood = request.POST['mood'] 
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('main:detail', update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('main:post')

# def delete_img(request, id):
#     delete_img_post = Post.objects.get(id=id)
#     delete_img_post.image.delete(save=True)
#     return redirect('main:detail', delete_img_post.id)

# def edit_img(request, id):
#     edit_img_post = Post.objects.get(id=id)
#     return render(request, 'main/editimg.html', {'post':edit_img_post})

# def update_img(request, id):
#     update_img_post = Post.objects.get(id=id)
#     update_img_post.image = request.FILES.get('image')
#     update_img_post.save()
#     return redirect('main:detail', update_img_post.id)
    
