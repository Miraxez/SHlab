from django.contrib.auth import get_user_model
from django.db import models


class OwnedModel(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=0)

    class Meta:
        abstract = True


class Author(OwnedModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


class BlogPost(OwnedModel):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Author', related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
