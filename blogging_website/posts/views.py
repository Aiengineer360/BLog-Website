from django.shortcuts import render, get_object_or_404, redirect 
from .models import Post, Comment # i have Imported the Post and Comment models
from .forms import PostForm, CommentForm # i have Imported the PostForm and CommentForm classes from the forms module
from django.template.loader import get_template # i have Imported the get_template function from django.template.loader 
from django.conf import settings
from django.contrib.auth.decorators import login_required  # i have Imported the login_required decorator 


@login_required # i have Added the login_required decorator
def home(request): # i have Added a home view
    posts = Post.objects.all() # i have Retrieved all posts
    return render(request, 'home.html', {'posts': posts}) # i have Rendered the home.html template with the posts

@login_required # i have Added the login_required decorator
def post_detail(request, pk): # i have Added a post_detail view
    post = get_object_or_404(Post, pk=pk) # i have Retrieved the post
    comments = post.comments.all() # i have Retrieved all comments for the post
    if request.method == 'POST': # i have Added a condition for the POST method
        form = CommentForm(request.POST) # i have Created a CommentForm instance with the submitted data
        if form.is_valid(): # i have Added a condition to check if the form is valid
            comment = form.save(commit=False) # i have Saved the form data to the database
            comment.post = post # i have Assigned the post to the comment
            comment.author = request.user # i have Assigned the author to the comment
            comment.save() # i have Saved the comment
            return redirect('post_detail', pk=post.pk) # i have Redirected to the post_detail view
    else:
        form = CommentForm() # i have Created a new CommentForm instance
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form}) # i have Rendered the post_detail.html template with the post, comments, and form

@login_required # i have Added the login_required decorator
def post_create(request): # i have Added a post_create view
    if request.method == 'POST': # i have Added a condition for the POST method
        form = PostForm(request.POST, request.FILES) # i have Created a PostForm instance with the submitted data
        if form.is_valid(): # i have Added a condition to check if the form is valid
            post = form.save(commit=False) # i have Saved the form data to the database
            post.author = request.user # i have Assigned the author to the post
            post.save() # i have Saved the post
            return redirect('home') # i have Redirected to the home view
    else:
        form = PostForm() # i have Created a new PostForm instance
    return render(request, 'post_form.html', {'form': form}) # i have Rendered the post_form.html template with the form

@login_required # i have Added the login_required decorator
def post_edit(request, pk): # i have Added a post_edit view
    post = get_object_or_404(Post, pk=pk) # i have Retrieved the post
    if request.user != post.author: # i have Added a condition to check if the user is the author of the post
        return redirect('home') # i have Redirected to the home view
    if request.method == 'POST': # i have Added a condition for the POST method
        form = PostForm(request.POST, request.FILES, instance=post) # i have Created a PostForm instance with the submitted data and the post instance
        if form.is_valid(): # i have Added a condition to check if the form is valid
            form.save() # i have Saved the form data to the database
            return redirect('post_detail', pk=post.pk) # i have Redirected to the post_detail view
    else:
        form = PostForm(instance=post) # i have Created a new PostForm instance with the post instance
    return render(request, 'post_form.html', {'form': form}) # i have Rendered the post_form.html template with the form

@login_required # i have Added the login_required decorator
def post_delete(request, pk): # i have Added a post_delete view
    post = get_object_or_404(Post, pk=pk) # i have Retrieved the post
    if request.user != post.author: # i have Added a condition to check if the user is the author of the post
        return redirect('home') # i have Redirected to the home view
    post.delete() # i have Deleted the post
    return redirect('home') # i have Redirected to the home view

