from django.shortcuts import render,HttpResponseRedirect,redirect,get_object_or_404,Http404
from .forms import FormPost,PostFilter,CommentForm
from .models import Post
from django.utils import timezone
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
# Create your views here.

def index_view(request):
    print("yeap")
    form_list=PostFilter(request.GET or None)
    post = Post.objects.all()
    query=request.GET.get('q')
    if query:
        post=post.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(user__first_name__icontains=query)
        ).distinct()

    if form_list.is_valid():
        secme=form_list.cleaned_data['secme']

        if secme=='T':
            post=post.filter(draft=True)

        elif secme=='TO':
            post = post.filter(draft=False)
        elif secme=='A':
            post=Post.objects.all()
        else:
            return render(request,'404.html')


    context={
        'post':post,
        'form_list': form_list
    }
    return render(request, 'index.html' , context)
def detail_view(request, slug):
    post=get_object_or_404(Post, slug=slug)

    form = CommentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context={
    'post':post,
    'form':form
    }
    return render(request, 'details.html' , context)
def create_view(request):
    # title=request.Post.get('title')
    # content=request.Post.get('content')
    # Post.object.create(title=title , content=content)
    if not request.user.is_authenticated:
        return render(request, '404.html')
    else:
        form=FormPost(request.POST or None,  request.FILES or None)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return HttpResponseRedirect(post.get_absolute_url())

        context={
            'form':form
        }
        return render(request , 'forms.html' , context)
def update_view(request, slug):
    if not request.user.is_authenticated:
        return render(request, '404.html')
    else:
        post = get_object_or_404(Post, slug=slug)
        form = FormPost(request.POST or None, instance=post)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(post.get_absolute_url())
        context = {
            'form': form,
        }
        return render(request, 'forms.html', context)
def delete_view(request,slug):
    if not request.user.is_authenticated:
        return render(request, '404.html')
    else:
        post=get_object_or_404(Post, slug=slug)
        post.delete()
        return redirect('app:index' )
