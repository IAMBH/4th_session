from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Tag
from django.utils import timezone
from django.db.models import Q

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
    if request.user.is_authenticated:   # 로그인 되어 있으면 게시글 저장
        new_post = Post()
        new_post.title = request.POST['title']
        # 현재 로그인 한 유저
        new_post.writer = request.user
        new_post.pub_date = timezone.now()
        new_post.weather = request.POST['weather']
        new_post.mood = request.POST['mood'] 
        new_post.body = request.POST['body']
        new_post.image = request.FILES.get('image')
        new_post.save()
        # 본문 내용을 띄어쓰기로 잘라냄
        words = new_post.body.split(' ')
        tag_list = []
        for w in words:
            if len(w)>0 and w[0]=='#':
                tag_list.append(w[1:])
        for t in tag_list:
            tag, boolean = Tag.objects.get_or_create(name=t)
            new_post.tags.add(tag.id)
        return redirect('main:detail', new_post.id)
    else:
        return redirect('accounts:login')

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    if request.method == 'GET':
        comments = Comment.objects.filter(post=post)
        return render(request, 'main/detail.html', {
            'post':post,
            'comments':comments,
            })
    elif request.method == "POST":
        new_comment = Comment()
        new_comment.post = post
        new_comment.writer = request.user
        new_comment.content = request.POST['content']
        new_comment.pub_date = timezone.now()
        new_comment.save()
        words = new_comment.content.split(' ')
        tag_list = []
        for w in words:
            if len(w)>0 and w[0]=='#':
                tag_list.append(w[1:])
        for t in tag_list:
            tag, boolean = Tag.objects.get_or_create(name=t)
            new_comment.tags.add(tag.id)
        return redirect('main:detail', id)
    
def delete_com(request, id):
    delete_com = Comment.objects.get(id=id)
    if request.user == delete_com.writer:
        delete_com.delete()
    return redirect('main:post')

def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, 'main/edit.html', {'post':edit_post })

def update(request, id):
    if request.user.is_authenticated:
        update_post = Post.objects.get(id=id)
        if request.user == update_post.writer:
            update_post.title = request.POST['title']
            update_post.writer = request.user
            update_post.pub_date = timezone.now()
            if request.FILES.get('image'):
                update_post.image = request.FILES.get('image')
            else: 
                update_post.image = update_post.image
            update_post.weather = request.POST['weather']
            update_post.mood = request.POST['mood'] 
            update_post.body = request.POST['body']
            update_post.save()
            # 태그 수정
            words = update_post.body.split(' ')
            tag_list = []
            for w in words:
                if len(w)>0 and w[0]=='#':
                    tag_list.append(w[1:])

            update_post.tags.clear()    # 원래 있던 tag필드 삭제
            # 이렇게 되면 post.tags는 없어지는데 Tag의 내용은 안없어지네
            for t in tag_list:
                tag, boolean = Tag.objects.get_or_create(name=t)
                update_post.tags.add(tag.id)
            return redirect('main:detail', update_post.id)
    return redirect('accounts:login')

def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('main:post')


def tag_list(reqeust):
    tags = Tag.objects.all()
    return render(reqeust, 'main/tag_list.html',{
        'tags':tags,
    })

def tag_posts(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    posts = Post.objects.filter(Q(tags=tag) | Q(comment__tags=tag)).distinct()

    # 이쪾 건드리면 과제 구현할 수 있을 거같은데
    return render(request, 'main/tag_posts.html', {
        'tag':tag,
        'posts':posts,
    })

def likes(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.like.all():
        post.like.remove(request.user)
        post.like_count -= 1
        post.save()
    else:
        post.like.add(request.user)
        post.like_count += 1
        post.save()
    return redirect('main:detail', post.id)

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
    
