import django.http

from .models import Post
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def posts_list(request):
    q = request.GET.get('q')
    context = {}
    posts = Post.objects
    if q:
        posts = posts.filter(title__contains=q)
        context['q'] = q
    if request.GET.get('p'):
        context['p'] = 'on'
        posts = posts.filter(published=True)
    posts = posts.all()

    context['posts'] = posts
    return render(request, 'posts/list.html', context)


def posts_details(request, post_id):
    p = Post.objects.get(id=post_id)
    context = {
        'post': p
    }
    return render(request, 'posts/details.html', context)

def posts_add(request: django.http.HttpRequest):
    if request.method == 'POST':
       print('dodawanie')
       title = request.POST.get('title')
       content = request.POST.get('content')
       published = bool(request.POST.get('published'))
       Post(title=title,
            content=content,
            published=published).save()
       # Post.objects.create()
       return django.http.HttpResponseRedirect(reverse('posts:list'))
    else:
        print('wyświetlanie')

    p = Post.objects.all()
    context = {
        'posts': p
    }
    return render(request, 'posts/add.html', context)
