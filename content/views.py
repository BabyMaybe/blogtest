import datetime

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.utils.text import slugify
from django.utils.html import escape, strip_tags
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.models import User
from .models import Post, Comment, UserProfile, Xmas
from .forms import PostForm, CommentForm, LoginForm, SignupForm, ProfileForm


# Create your views here.
# @login_required
class BlogView(ListView):
    model = Post
    template_name = 'content/blog_main.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super (BlogView, self).get_context_data(**kwargs)

        context['post_list'] = Post.objects.filter(active=True)

        return context

    def get (self, request, *args, **kwargs):
        if (not request.user.is_authenticated()):
            return redirect('/signup/')
        return super(BlogView, self).get(request, *args, **kwargs)

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

class NewPost(CreateView):
    model = Post
    fields = ['title', 'rich_content']
    template_name = 'content/newpost.html'

    def form_valid(self, form):
       f = form.cleaned_data
       title = f['title'].title()
       post = f['rich_content']
       timestamp = datetime.datetime.now()
       slug = slugify(title)
       p = Post(title=title, content=post, rich_content=post, date_published=timestamp, slug=slug, author=self.request.user)
       p.save()
       return HttpResponseRedirect('/')

class PostDetail(DetailView, JsonResponse):
    model = Post
    form_class = CommentForm
    initial = {'comment':"Enter comment here!"}
    template_name = 'content/post.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)

        context['comments'] = self.get_object().post_comments.all().filter(active=True).order_by('timestamp')
        context['form'] = self.form_class(initial=self.initial)

        return context

    def get(self, request, *args, **kwargs):

        super(PostDetail, self).get(request, *args, **kwargs)
        form = self.form_class(initial=self.initial)
        context = self.get_context_data()

        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):

        if request.is_ajax():

            if request.POST.get('action') == 'like':
                response = self.like_post(request, *args, **kwargs)

            if request.POST.get('action') == 'comment':
                response = self.add_comment(request, *args, **kwargs)

            if request.POST.get('action') == 'delete':
                response = self.delete_comment(request, *args, **kwargs)

            if request.POST.get('action') == 'edit':
                response = self.edit_comment(request, *args, **kwargs)
            return response

        form = self.form_class(request.POST)

        if form.is_valid():
            print (form.cleaned_data['content'])
            author = request.user
            content = form.cleaned_data['content']
            timestamp = datetime.datetime.now()

            post = self.get_object()
            post.comment_count += 1
            post.save()
            c = Comment(author=author, content=content, timestamp=timestamp, parent_post=post)
            c.save()
            return HttpResponseRedirect(request.path)

    def like_post(self, request, *args, **kwargs):
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

    def add_comment(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if request.user.is_authenticated():
            author = request.user.username
            display_author = author
            prof = UserProfile.objects.get(user = request.user)
            color = prof.color
            uid = prof.pk
            letter = prof.get_letter()
        if form.is_valid():
            content = escape(form.cleaned_data['content'])
            timestamp = datetime.datetime.now()
            post = self.get_object()
            c = Comment(display_author=display_author, author=request.user, content=content, timestamp=timestamp,
                        parent_post=post )
            c.save()
            post.comment_count = post.get_comment_count()
            post.save()
            count = post.get_comment_count()
            data = {"author" : author,
                    "content" : content,
                    "timestamp" : timestamp.strftime("%d %B %Y | %I:%M %p"),
                    "id" : c.pk,
                    "color" : color,
                    "uid" : uid,
                    "letter" : letter,
                    "count" : count
                    }
            return JsonResponse(data)

    def delete_comment(self, request, *args, **kwargs):
        cid = request.POST.get('id')
        c = Comment.objects.get(pk=cid)
        deleted = False
        if c.author == request.user:
            c.active = False
            c.save()
            deleted = True
            post = self.get_object()
            post.comment_count = post.get_comment_count()
            count = post.comment_count
            post.save()

        return JsonResponse({"deleted" : deleted, "cid" : cid, "count" : count})

    def edit_comment(self, request, *args, **kwargs):
        cid = request.POST.get('id')
        new_content = escape(request.POST.get('newContent'))
        c = Comment.objects.get(pk=cid)
        c.content = new_content
        c.save()

        return JsonResponse({"newContent" : new_content})

class ViewProfile(DetailView):
    model = UserProfile
    template_name = 'content/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ViewProfile, self).get_context_data(**kwargs)
        context ['comments_made'] = Comment.objects.filter(author=self.object.user).count()
        context ['posts_made'] = Post.objects.filter(author=self.object.user).count()
        return context

class MakeProfile(CreateView):
    model = UserProfile
    fields = ['age','birthday','addr_street','addr_city','addr_state','addr_zip','color']
    template_name = 'content/signup_details.html'
    success_url = '/'


    def get(self,request, *args, **kwargs):

        return super(MakeProfile, self).get(args, kwargs)

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = User.objects.get(pk=int(self.kwargs['user_id']))
        return super(MakeProfile, self).form_valid(form)

class EditProfile(UpdateView):
    model = UserProfile
    form_class = ProfileForm
    template_name = 'content/signup_details.html'

    def get_success_url(self):
        return reverse('profile', args = (self.object.id,))

class XmasForm(CreateView):
    model = Xmas
    fields = '__all__'
    template_name = 'content/xmas.html'

class Signup(FormView):
    model = User
    form_class = SignupForm
    template_name = 'content/signup.html'


    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        if (form.is_valid()):
            f = form.cleaned_data

            username = f['username']
            email = f['email']
            password = f['password']
            first = f['first_name']
            last = f['last_name']

            User.objects.create_user(username, email, password, first_name=first, last_name=last )

            user = authenticate(username=username, password=password)
            login (self.request, user)

            return redirect('signup_details', user_id=user.id)

        return redirect('/signup/')

    def get_success_url(self):
        return reverse('signup_details',args=(self.object.id,))

class Login(FormView):
    form_class = LoginForm
    template_name = 'content/login.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                # Return a 'disabled account' error message
                return ('disabled account')
        else:
            # Return an 'invalid login' error message.
            return redirect('/login/')



    def form_valid(self, form):
        f = form.cleaned_data
        print (f)

        user = authenticate(username = f['username'], password = f['password'])
        if user is not None:
        # the password verified for the user
            if user.is_active:
                print("User is valid, active and authenticated")
            else:
                print("The password is valid, but the account has been disabled!")
        else:
            # the authentication system was unable to verify the username and password
            print("The username and password were incorrect.")

        return super (Login, self).form_valid(form)

def logout_view(request):
    logout(request)

