from django.shortcuts import render, redirect
from blog.models import Post, Category
from blog.forms import CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def all_blogs(request):
    posts = Post.objects.all()
    p = Paginator(posts, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    return render(request, 'blog/all_blogs.html', {'posts': posts, 'page_obj':page_obj})

def post_detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        post = None

    if request.method == 'POST':
    	form = CommentForm(request.POST)

    	if form.is_valid():
    		comment = form.save(commit=False)
    		comment.post = post
    		comment.save()

    		return redirect('post_detail', slug=post.slug)
    else:
    	form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    
    return render(request, 'blog/categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})

