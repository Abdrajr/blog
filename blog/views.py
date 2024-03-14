from django.shortcuts import render, get_list_or_404
from .models import Post
from django.http import Http404

def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post found.")


    return render(request,
                  'blog/post/detail.html',
                  {'post': post})

    


def post_list(request):
    post = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'post': post})
