from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .models import Post
from .models import profile
from .models import Offers
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from .forms import RegisterForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.template.defaultfilters import slugify

#updated
def index(request):

    all_post = Post.objects.all().order_by('-id') #updated

    context = allPaginate(request, all_post, 10)

    query = request.GET.get("q") #updated

    if query: #updated
        all_post = allQuery(request, query, all_post)
        posts = all_post
        context['posts'] = posts
        context['query'] = query
        return render(request, 'homepage/Mainhpage.html', context)

    return render(request, 'homepage/Mainhpage.html', context)#updated



#updated
def user(request, user_num):
    sUser = get_object_or_404(User,id=user_num)
    all_post = sUser.post_set.all().order_by('-id') #updated
    context = allPaginate(request, all_post, 5)
    context['user'] = sUser

    return render(request, 'homepage/user.html', context)




#updated
def login_user(request):
    posts = Post.objects.all().order_by('-id') #updated

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                context = allPaginate(request, posts, 10)
                return render(request, 'homepage/Mainhpage.html', context)
            else:
                return render(request, 'homepage/Mainhpage.html')
        else:
            context = allPaginate(request, posts, 10)
            return render(request, 'homepage/Mainhpage.html', context)


def logout_user(request):
    logout(request)

    return render(request, 'homepage/logoutpage.html')
class createPost(CreateView):
    model = Post
    fields = ['item_name', 'thumbnail', 'quantity', 'post_condition', 'post_type', 'tags']

    def form_valid(self, form):
        form.instance.op = self.request.user
        return super(createPost,self).form_valid(form)

class createOffer(CreateView):
    model = Offers
    fields = ['ifPurchase', 'amount', 'item',]

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(createOffer, self).form_valid(form)




#update
def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.degree = form.cleaned_data.get('degree')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user.save()

            login_user
    else:
        form = RegisterForm()
    return render(request, 'homepage/register.html', {'form': form})



#updated
def post_detail(request, post_num):
    sPost = get_object_or_404(Post,id=post_num)
    return render(request, 'homepage/post_detail.html', {'post' : sPost, 'log_user': request.user , 'post_condition' : slugify(sPost.post_condition)})




#updated
def indexPaginate(request, page_num):
    all_post = Post.objects.all().order_by('-id') #updated

    context = allPaginate(request, all_post, page_num)

    return render(request, 'homepage/Mainhpage.html', context)


def qPaginate(request, query, page_num):
    all_post = Post.objects.all().order_by('-id')
    all_post = allQuery(request, query, all_post)
    context = allPaginate(request, all_post, page_num)
    context['query'] = query
    return render(request, 'homepage/Mainhpage.html', context)


def allPaginate(request, obj, page_num):
    paginator = Paginator(obj, page_num)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts, 'page': page, 'log_user': request.user
    }
    return context


def allQuery(request, query, all_post):
    all_post = all_post.filter(
            Q(item_name__icontains=query) |
            Q(tags__slug__icontains=query) |
            Q(post_type__icontains=query) |
            Q(post_condition__icontains=query)
        ).distinct()
    return all_post

def TCTSearch(request, tag_name):
    all_post = Post.objects.all().order_by('-id')
    all_post = allQuery(request, tag_name, all_post)

    context = allPaginate(request, all_post, 10)
    context['query'] = tag_name
    return render(request, 'homepage/Mainhpage.html', context)
