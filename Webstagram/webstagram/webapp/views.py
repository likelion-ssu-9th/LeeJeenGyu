from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Feed
from django.utils import timezone

# Create your views here.
def delete(request,id):
    delete_feed = Feed.objects.get(id=id)
    delete_feed.delete()
    return redirect('feed')

def update(request,id):
    update_feed = Feed.objects.get(id=id)
    update_feed.title = request.POST['title']
    update_feed.writer = request.POST['writer']
    update_feed.body = request.POST['body']
    update_feed.image = request.FILES['image']
    update_feed.pub_date = timezone.now()
    update_feed.save()
    return redirect('feed',update_feed.id)

def edit(request,id):
    edit_feed = Feed.objects.get(id=id)
    return render(request,'edit.html',{'feed':edit_feed})

def detail(request,id):
    feed = get_object_or_404(Feed,pk=id)
    return render(request,'detail.html',{'feed':feed})

def create(request):
    new_feed = Feed()
    new_feed.title = request.POST['title']
    new_feed.writer = request.POST['writer']
    new_feed.body = request.POST['body']
    new_feed.image = request.FILES['image']
    new_feed.pub_date = timezone.now()
    new_feed.save()
    return redirect('feed')

def new(request):
    return render(request,'new.html')

def feed(request):
    feeds = Feed.objects.all()
    return render(request,'feed.html',{'feeds':feeds})

def profile(request):
    feeds = Feed.objects.all()
    return render(request,'profile.html',{'feeds':feeds})

def signup(request): # 회원가입
    if request.method == "POST":
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(username = request.POST['username'], password=request.POST['password'])
            auth.login(request, user)
            return redirect('/')
    return render(request,'signup.html')

# def login(request): #로그인
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         #auth.authenticate 라는 말은 DB에서 방금전에 입력한 이 내용이 우리한테 있는 회원명단이 맞는지 확인시켜주는 함수
#         user = auth.authenticate(request, username=username, password=password)

#         if user is not None:    # is not None = None이 아니라면 = 회원이라면
#             auth.login(request,user)
#             return redirect('/')
#         else:
#             return render(reuqst, 'login.html', {'error': 'username or password is incorrect'})
#     else:
#         return render(request, 'login.html')

def login(request):
    if request.method=="POST" :
        username= request.POST['username']
        password= request.POST['password']
        user=auth.authenticate(request, username=username, password=password)

        if username is not None:
            auth.login(request, user)
            return redirect('feed')
        else:
            return render(request, 'login.html',{'error' : 'username or password is incorrect. '})
    else:
        return render(request, 'login.html')

def logout(request): # 로그아웃
    if request.method == "POST":
        auth.logout(request)
        return redirect('/')
    return render(request,'login.html')

