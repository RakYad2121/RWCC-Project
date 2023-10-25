from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.title) + ' | ' + str(self.author)
    def get_absolute_url(self):
        return reverse('blog-details', args=(str(self.pk)))