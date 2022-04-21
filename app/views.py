from django.shortcuts import render
from post.models import Post
from django.views import View
from post.forms import PostForm
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# @login_required(login_url='login')
class HomePage(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'home'
    
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-date')
        
        form = PostForm()
        context = {'posts' : posts, 'form': form}
        return render(request, "index.html", context)

