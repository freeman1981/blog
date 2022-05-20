from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CheckConstraint, Q
from django_extensions.db.models import TimeStampedModel


class User(AbstractUser):
    # https://docs.djangoproject.com/en/4.0/topics/auth/customizing/
    pass


def short_string(s: str, len_: int = 10) -> str:
    return s if len(s) <= len_ + 3 else s[:len_] + '...'


class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)
    name_en = models.CharField(max_length=32, blank=True, default='')

    def __str__(self):
        return short_string(self.name)


class Post(TimeStampedModel):
    name = models.CharField(max_length=128)
    name_en = models.CharField(max_length=128, blank=True, default='')
    content = models.TextField()
    content_en = models.TextField(blank=True, default='')
    owner = models.ForeignKey(User, models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    related = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return short_string(self.name)


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, models.CASCADE, null=True, blank=True)
    content = models.TextField()
    parent = models.ForeignKey('self', models.CASCADE, null=True, blank=True)
    owner = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return short_string(self.content)

    class Meta:
        constraints = [
            CheckConstraint(check=Q(post__isnull=False) | Q(parent__isnull=False), name='not_all_null')
        ]
