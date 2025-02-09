from django.db import models
from django.contrib.auth.models import User

class Post(models.Model): # i have Created a new model class
    title = models.CharField(max_length=200) # i have Added a title field
    content = models.TextField() # i have Added a content field
    created_at = models.DateTimeField(auto_now_add=True) # i have Added a created_at field
    image = models.ImageField(upload_to='post_images/', blank=True, null=True) # i have Added an image field
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # i have Added an author field
    categories = models.CharField(max_length=100, blank=True, null=True) # i have Added a categories field
    tags = models.CharField(max_length=100, blank=True, null=True) # i have Added a tags field

    def __str__(self): # i have Added Dunder method
        return self.title # i have Returned a string

class Comment(models.Model): # i have Created a new model class
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') # i have Added a post field
    author = models.ForeignKey(User, on_delete=models.CASCADE) # i have Added an author field
    content = models.TextField() # i have Added a content field
    created_at = models.DateTimeField(auto_now_add=True) # i have Added a created_at field

    def __str__(self): # i have Added Dunder method
        return f"Comment by {self.author} on {self.post.title}" # i have Returned a string
    
    # i have also made migrations and migrated the models to the database
    # python manage.py makemigrations
    # python manage.py migrate
    # i have also created a superuser
    # python manage.py createsuperuser
    # i have also registered the models in the admin.py file
    # admin.site.register(Post)
    # admin.site.register(Comment)
    # i have also created a forms.py file and created two form classes
    # PostForm and CommentForm
    # i have also created a views.py file and created five views
    # home, post_detail, post_create, post_edit, and post_delete
    # i have also created a urls.py file and added URL patterns for the views
    # i have also included the posts app URLs in the project URLs
    # i have also included the users app URLs in the project URLs
    # i have also added the users app to the project
    # i have also added the posts app to the project
    # i have also added the Pillow library to the project