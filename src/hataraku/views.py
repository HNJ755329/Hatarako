from django.shortcuts import render
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm
import datetime

# Create your views here.
"""
def hataraku_index(request):
    posts = Post.objects.all().order_by('-created_on')[:10]
    uuid_post = Post.objects.all().order_by('-created_on').first()
    form = PostForm()
    date = datetime.datetime.now()

    context = {
        "uuid_post": uuid_post,
        "posts": posts,
        "form": form,
        "date": date,
    }
    return render(request, "hataraku_index.html", context)
"""

def hataraku_index(request, uuid):
    try:
        uuid_post = Post.objects.get(pk=uuid)
    except:
        uuid_post = Post.objects.all().order_by('-created_on').first()

    posts = Post.objects.all().order_by('-created_on')[:10]
    form = PostForm()
    date = datetime.datetime.now()

    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            
            post = Post(
                contents=form.cleaned_data["contents"],
                industory=form.cleaned_data["industory"],
                career=form.cleaned_data["career"],
                age=form.cleaned_data["age"],
                #color=form.cleaned_data["color"],
                #color=request.POST.get("color", ""),
            )
            post.save()
    """
    context = {
        "uuid_post": uuid_post,
        "posts": posts,
        "form": form,
        "date":date,
    }
    return render(request, "hataraku_index.html", context)

def hataraku_result(request):
    form = PostForm()
    #date = datetime.datetime.now()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():          
            post = Post(
                contents=form.cleaned_data["contents"],
                industory=form.cleaned_data["industory"],
                career=form.cleaned_data["career"],
                age=form.cleaned_data["age"],
                color=request.POST.get("color", ""),
            )
            post.save()
            uuid_post = post
    uuid = str(uuid_post.id)
    """
    posts = Post.objects.all().order_by('-created_on')[:10]
    context = {
        "uuid_post": uuid_post,
        "posts": posts,
        "form": form,
        "date":date,
    }
    #return render(request, "hataraku_index.html", context)
    """    
    return redirect("../" + uuid)
