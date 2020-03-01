from django.contrib.auth import get_user_model
from django.db import models


class OwnedModel(models.Model):

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=0)

    class Meta:
        abstract = True


class BlogPost(OwnedModel):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title


