from django import forms
from .models import Post, Comment # i have Imported the Post and Comment models

class PostForm(forms.ModelForm): # i have Created a new form class
    class Meta:
        model = Post # i have Set the model to Post
        fields = ['title', 'content', 'image', 'categories', 'tags'] # i have Added the image, categories, and tags fields

class CommentForm(forms.ModelForm): # i have Created a new form class
    class Meta:
        model = Comment # i have Set the model to Comment
        fields = ['content'] # i have Added the content field