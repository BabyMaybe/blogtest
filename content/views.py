import datetime

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormView
from django.utils.text import slugify
from django.utils.html import escape, strip_tags

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.models import User
from .models import Post, Comment, UserProfile
from .forms import PostForm, CommentForm


# Create your views here.
class BlogView(ListView):
    model = Post
    template_name = 'content/blog_main.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super (BlogView, self).get_context_data(**kwargs)

        context['post_list'] = Post.objects.filter(active=True)

        return context

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            post_pk = request.POST.get("pk")
            post = Post.objects.get(pk=post_pk)
            if request.POST.get('action') == 'like':
                if not request.user.is_anonymous():
                    # do something
                    if (request.user in post.likes.all()):
                        post.likes.remove(request.user)
                    else:
                        post.likes.add(request.user)
                    post.like_count = post.likes.count()
                    post.save()
            data = {"likes" : post.like_count, "pk" : post_pk}
            return JsonResponse(data)

class PostDetail(DetailView, JsonResponse):
    model = Post
    form_class = CommentForm
    initial = {'comment':"Enter comment here!"}
    template_name = '/content/base.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)

        context ['comments'] = self.get_object().comment_set.all().filter(active=True)
        context ['form'] = self.form_class(initial=self.initial)

        return context

    def get(self, request, *args, **kwargs):

        super(PostDetail, self).get(request, *args, **kwargs)
        form = self.form_class(initial=self.initial)

        # context = self.get_context_data()
        # context ['comments'] = Comment.objects.filter(post=kwargs.get('pk')).filter(active=True)

        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):

        if request.is_ajax():

            if request.POST.get('action') == 'like':
                self.like_post(request)

            if request.POST.get('action') == 'comment':
                self.add_comment(request)

            if request.POST.get('action') == 'delete':
                self.delete_comment(request)

            if request.POST.get('action') == 'edit':
                self.edit_comment(request)

        form = self.form_class(request.POST)
        if form.is_valid():

            author = form.cleaned_data['author']
            content = form.cleaned_data['comment']
            timestamp = datetime.datetime.now()

            post = self.get_object()
            post.comment_count += 1
            post.save()
            c = Comment(author=author, content=content, timestamp=timestamp, post=post)
            c.save()
            return HttpResponseRedirect(request.path)

    def like_post(self, request):
        post = self.get_object()
        if not request.user.is_anonymous():
            if (request.user in post.likes.all()):
                post.likes.remove(request.user)
            else:
                post.likes.add(request.user)

            post.like_count = post.likes.count()
            post.save()

        data = {"likecount" : post.like_count, "error" : ""}

        if request.user.is_anonymous():
            data["error"] = "please log in to comment"

        return JsonResponse(data)

    def add_comment(self, request):
        form = self.form_class(request.POST)

        display_author = "anonymous coward"

        if request.user.is_authenticated():
            author = request.user.username

        content = escape(form.cleaned_data['content'])
        timestamp = datetime.datetime.now()

        post = self.get_object()

        c = Comment(display_author=display_author, content=content, timestamp=timestamp,
                    post=post, author=request.user)
        c.save()

        post.commentCount = post.comment_set.count()
        post.save()

        data = {"author" : author,
                "comment" : comment,
                "timestamp" : timestamp,
                "id" : c.pk
                }

        return JsonResponse(data)

    def delete_comment(self, request):
        cid = request.POST.get('id')
        c = Comment.objects.get(pk=cid)
        deleted = False
        if c.author == request.user:
            c.active = False
            c.save()
            deleted = True
        return JsonResponse({"deleted" : deleted, "cid" : cid})

    def edit_comment(self, request):
        cid = request.POST.get('id')
        new_content = escape(request.POST.get('newContent'))

        c = Comment.objects.get(pk=cid)
        c.content = new_content
        c.save()

        return JsonResponse({"newContent" : newContent})
        return render(request, self.template_name, self.get_context_data())

class MakeProfile(CreateView):
    model = UserProfile
    fields = ['age','birthday','addr_street','addr_city','addr_state','addr_zip','prof_pic']
    template_name = 'content/signup_details.html'
    success_url = '/'

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = User.objects.get(pk=1) #need to get user from previous page
        return super(MakeProfile, self).form_valid(form)

class Signup(CreateView):
    model = User
    fields = ['username','password','email','first_name','last_name']
    template_name = 'content/signup.html'
    success_url = '/signup_details'








