from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects #퀴리셋
    return render(request,'home.html',{'blogs':blogs})

    
def detail(request,blog_id):
    details=get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'details':details})

def new(request):#new.html 띄어주는 함수
    return render(request,'new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수     
    blog = Blog()#Blog라는 클래스로부터 blog 객체생성
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()#블로그를 작성한 시점을 넣어줌
    blog.save()#쿼리셋메소드. blog에 대한 내용을 저장해라.
    return redirect('/blog/'+str(blog.id))