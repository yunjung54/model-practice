from django.shortcuts import render

from .models import Blog
# Create your views here.

def home(request):
    posts = Blog.objects.all()
    # 변수와 딕셔너리로 키와 벨류로 이루어짐 파이썬도 마찬가지이다
    return render(request ,'home.html',{'key_posts':posts,})
    # 왼쪽에 있는 키가 넘어가느데 거기에 벨루가 포스츠