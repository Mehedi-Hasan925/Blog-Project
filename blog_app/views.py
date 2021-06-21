from django.shortcuts import render,HttpResponseRedirect
from blog_app import models
from blog_app import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse,reverse_lazy
from django.views.generic import CreateView, DeleteView,DetailView,UpdateView,ListView,TemplateView,View
import uuid

# Create your views here.

class BlogList(ListView):
    context_object_name = 'blogs'
    model = models.Blog
    template_name = "blog_list.html"
    queryset = models.Blog.objects.order_by('-publish_time')



class CreateBlog(LoginRequiredMixin, CreateView):
    model = models.Blog
    fields = ('title','content','blog_image')
    template_name = "blog_app/create_blog.html"

    def form_valid(self,form):
        current_user = self.request.user
        
        form_obj = form.save(commit=False)
        form_obj.author = current_user
        blog_title = form_obj.title 
        form_obj.slug = blog_title.replace(" ","-") + "-" + str(uuid.uuid4())

        form.save()
        return HttpResponseRedirect(reverse('index'))



class UpdateBlog(LoginRequiredMixin, UpdateView):
    model = models.Blog
    fields = ('title','content','blog_image')
    template_name = "blog_app/update_blog.html"

    def get_success_url(self,**kwargs):
        return reverse_lazy('blog_app:blog_detail', kwargs={'slug':self.object.slug})




@login_required
def BlogDetail(request,slug):
    blog = models.Blog.objects.get(slug=slug)
    comment_form = forms.CommentForm()

    already_liked = models.like.objects.filter(blog_like=blog,user_like=request.user)
    if already_liked:
        liked = True
    
    else:
        liked = False

    if request.method=='POST':
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) 
            comment.blog_comment = blog   
            comment.user_comment = request.user
            comment.save()   
            return HttpResponseRedirect(reverse('blog_app:blog_detail', kwargs={'slug':slug}))

    diction = {'blog':blog,'comment_form':comment_form,'liked':liked}

    return render(request,'blog_app/blog_detail.html',context=diction)

@login_required
def Liked(request,pk):
    blog = models.Blog.objects.get(pk=pk)
    current_user = request.user

    already_liked = models.like.objects.filter(blog_like=blog,user_like=current_user)
    if not already_liked:
        liked_post = models.like(blog_like=blog,user_like=current_user)
        liked_post.save()
    
    return HttpResponseRedirect(reverse('blog_app:blog_detail',kwargs={'slug':blog.slug}))


@login_required
def unliked(request,pk):
    blog = models.Blog.objects.get(pk=pk)
    current_user = request.user

    already_liked = models.like.objects.filter(blog_like=blog,user_like=current_user)

    already_liked.delete()

    return HttpResponseRedirect(reverse('blog_app:blog_detail',kwargs={'slug':blog.slug}))


class MyBlog(LoginRequiredMixin,TemplateView):
    template_name = "blog_app/my_blogs.html"


