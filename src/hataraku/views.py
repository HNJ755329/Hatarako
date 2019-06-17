from django.shortcuts import render
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def hataraku_index(request):
    uuid_post = Post.objects.all().order_by('-created_on').first()
    posts = Post.objects.all().order_by('-created_on')[:10]
    form = PostForm({})
    context = {
        "uuid_post": uuid_post,
        "posts": posts,
        "form": form,
    }
    return render(request, "hataraku_index.html", context)

def hataraku_uuid(request, uuid):
    uuid_post = Post.objects.get(pk=uuid)
    posts = Post.objects.all().order_by('-created_on')[:10]
    form = PostForm({})
    context = {
        "uuid_post": uuid_post,
        "posts": posts,
        "form": form,
    }
    return render(request, "hataraku_index.html", context)

def hataraku_result(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            """          
            post_formed = Post(
                contents=form.cleaned_data["contents"],
                industory=form.cleaned_data["industory"],
                career=form.cleaned_data["career"],
                age=form.cleaned_data["age"],
                # color=form.cleaned_data["color"],
                color=request.POST.get("color", "#333333"),
            )
            post_formed.save()
            return hataraku_uuid(request, str(post_formed.id))"""
            return hataraku_uuid(request, str(post.id))
            # return redirect(post_formed.get_absolute_url())
            # なぜか302エラーが返ってくるので変更。
        else:
            return hataraku_index(request)
    else:
        return hataraku_index(request)
