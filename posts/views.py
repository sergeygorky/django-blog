from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import PostForm
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Successfully Created')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form,

    }
    return render(request, 'posts/post_form.html', context)


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        'title': instance.title,
        'instance': instance,
    }
    return render(request, 'posts/post_detail.html', context)


def post_list(request):
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 5)

    page = request.GET.get('page')
    queryset = paginator.get_page(page)
    context = {
        'object_list': queryset,
        'title': 'List'
    }
    return render(request, 'posts/post_list.html', context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None,
                    instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, '<a href="#">Item</a>Saved',
                         extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title': instance.title,
        'instance': instance,
        'form': form
    }
    return render(request, 'posts/post_form.html', context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect('posts:list')
