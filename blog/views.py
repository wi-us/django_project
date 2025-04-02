from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm
from django.core.paginator import Paginator


class _PostView(View):
    '''Вывод записи'''
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', {'post_list': posts})

class PostView(View):
    '''Вывод записи'''
    def get(self, request):
        posts = Post.objects.all().order_by('-date')
        paginator = Paginator(posts, 6)
        page = request.GET.get('page')

        #получить номер страницы
        page_obj = paginator.get_page(page)

        return render(request, 'blog/blog.html', {'post_list': page_obj})


class PostDetails(View):
    '''Отдельная страница записи'''
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        print(post, pk, self)
        return render(request, 'blog/blog_details.html', {'post': post})
    
class AddComments(View):
    '''Добавление комментариев'''
    def post(self, request, pk):
        print(request.POST)
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()

        return redirect(f'/{pk}')


def getPosts(request):
    #получить страницу
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')

    #получить номер страницы
    page_obj = paginator.get_page(page)
    return render(request, 'blog/paginator.html', {"data": page_obj})
