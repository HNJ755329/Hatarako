from django.shortcuts import render
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def hataraku_index(request):
    posts = Post.objects.all().order_by('-created_on')[:10]
    uuid_post = Post.objects.all().order_by('-created_on').first()
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(
                contents=form.cleaned_data["contents"],
                industory=form.cleaned_data["industory"],
                career=form.cleaned_data["career"],
                age=form.cleaned_data["age"],
            )
            post.save()

    context = {
        "uuid_post": uuid_post,
        "posts": posts,
        "form": form,
    }
    return render(request, "hataraku_index.html", context)


def hataraku_uuid(request, uuid):
    uuid_post = Post.objects.get(pk=uuid)
    posts = Post.objects.all().order_by('-created_on')[:10]
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(
                contents=form.cleaned_data["contents"],
                industory=form.cleaned_data["industory"],
                career=form.cleaned_data["career"],
                age=form.cleaned_data["age"],
            )
            post.save()

    context = {
        "uuid_post": uuid_post,
        "posts": posts,
        "form": form,
    }
    return render(request, "hataraku_index.html", context)

def hataraku_result(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(
                contents=form.cleaned_data["contents"],
                industory=form.cleaned_data["industory"],
                career=form.cleaned_data["career"],
                age=form.cleaned_data["age"],
            )
            post.save()
            uuid_post = post
    posts = Post.objects.all().order_by('-created_on')[:10]
    context = {
        "uuid_post": uuid_post,
        "posts": posts,
        "form": form,
    }
    return render(request, "hataraku_index.html", context)