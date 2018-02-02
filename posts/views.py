from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .forms import PostForm
from .models import Post


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    # if request.method == 'post':
    #     print(request.POST.get('content'))
    #     print(request.POST.get('title'))
    #     # Post.objects.create(title=title)
    context = {
        'form': form,

    }
    return render(request, 'posts/post_form.html', context)


def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        'title': instance.title,
        'instance': instance,
    }
    return render(request, 'posts/post_detail.html', context)


def post_list(request):
    queryset = Post.objects.all()
    context = {
        'object_list': queryset,
        'title': 'List'
    }
    return render(request, 'posts/index.html', context)


def post_update(request):
    return HttpResponse("<h1>Update</h1>")


def post_delete (request):
    return HttpResponse("<h1>Delete</h1>")
