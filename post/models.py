import string as str
from random import choice

from django.db import models
from django.urls import reverse
# from django.utils.encoding import python_2_unicode_compatible

from account.models import User


def generate_id():
        n = 10
        random = str.ascii_uppercase + str.ascii_lowercase + str.digits
        return ''.join(choice(random) for _ in range(n))


class Post(models.Model):
    author = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=10, default=generate_id)
    photo = models.FileField(upload_to='posts_photo')
    caption = models.CharField(max_length=50, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ['-date_created', ]

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('post:view', kwargs={'slug': self.slug})


class DesignRating(models.Model):
  post = models.ForeignKey(Post, related_name='rated_post_design', on_delete=models.CASCADE)
  user = models.ForeignKey(User, related_name='design_rater', on_delete=models.CASCADE)
  date_created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return '{} : {}'.format(self.user, self.post)


class UsabilityRating(models.Model):
  post = models.ForeignKey(Post, related_name='rated_post_usability', on_delete=models.CASCADE)
  user = models.ForeignKey(User, related_name='usability_rater', on_delete=models.CASCADE)
  date_created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return '{} : {}'.format(self.user, self.post)


class ContentRating(models.Model):
  post = models.ForeignKey(Post, related_name='rated_post_content', on_delete=models.CASCADE)
  user = models.ForeignKey(User, related_name='content_rater', on_delete=models.CASCADE)
  date_created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return '{} : {}'.format(self.user, self.post)