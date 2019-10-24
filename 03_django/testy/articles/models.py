from django.db import models
from django.urls import reverse


# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-pk',)
    
    class __str__(self):
        return self.title

    class get_absolute_url(self):
        return reverse("articles:detail", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-pk',)
    
    
    class __str__(self):
        return self.content