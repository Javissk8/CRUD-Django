from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):

    phone_number = models.CharField(max_length=45, null = False)
    birthday = models.DateField()
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

#hacer relacion 1 a 1

class Category(models.Model):

    name = models.CharField(max_length=45, null = False)

    def __str__(self):
        return 'name: {}'.format(self.name)


class Business(models.Model):

    name = models.CharField(max_length=45, null = False)
    hours = models.CharField(max_length=45, null = False)
    email = models.EmailField(max_length=60, null = False)
    address = models.CharField(max_length=100, null = False, blank = False)
    last_modified = models.DateTimeField(auto_now =True)
    created_at = models.DateTimeField(auto_now_add = True)
    comment_business = models.ManyToManyField(User, through='CommentBusiness')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return 'name: {}'.format(self.name)

class Promo(models.Model):
    name = models.CharField(max_length=45, null = False)
    description = models.TextField(null = False)
    business = models.ForeignKey(Business, on_delete = models.CASCADE)

class CommentBusiness(models.Model):

    comment = models.TextField(null = False)
    created_at = models.DateTimeField(auto_now_add = True)
    score = models.PositiveSmallIntegerField(validators= [MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    

    def __str__(self):
        return 'score: {}'.format(self.score)