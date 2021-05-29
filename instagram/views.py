from django.shortcuts import render
from django.views import View
from .models import Post
from .forms import PostForm

# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')

        context = {
            'post_list': posts,
        }

        return render(request, 'post_list.html', context)


    def post(self, request, *args, **kwargs):
        posts = Post.objects.all()
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        context = {
            'post_list': posts,
            'form': form,
        }
        return render(request, 'post_list.html', context)