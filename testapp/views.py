from django.shortcuts import render,get_object_or_404
from testapp.models import Post

def post_list_view(request):
    post_list=Post.objects.all()
    return render(request,'testapp/post_list.html',{'post_list':post_list})

# def post_detail_view(request,year,month,day,post):
#     post=get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
#     return render(request,'testapp/post_detail.html',{'post':post})