from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100) # i have created a model for the user
    email = models.EmailField(max_length=100) # the user will have a name, email, password, created_at and updated_at
    password = models.CharField(max_length=100) # the name will be a character field with a max length of 100
    created_at = models.DateTimeField(auto_now_add=True) # the email will be an email field with a max length of 100
    updated_at = models.DateTimeField(auto_now=True) # the password will be a character field with a max length of 100

    def __str__(self): # i have used the dunder str method to return the name of the user
        return self.name # this will return the name of the user


 