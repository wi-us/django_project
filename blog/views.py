from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm
from django.core.paginator import Paginator

class PostView(View):
    '''Вывод записи'''
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', {'post_list': posts})

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
