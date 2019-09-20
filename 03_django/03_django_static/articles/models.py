from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail
from django.urls import reverse
from django.db import models


def article_image_path(instance, filename):
    return f'articles/{instance.pk}/images/{filename}'


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    # image_thumbnail = ImageSpecField(
    #     source = 'image',
    #     processors = [Thumbnail(200, 300)],
    #     format = 'JPEG',
    #     options = { 'quality: 90'},
    # )

    image = ProcessedImageField(
        processors = [Thumbnail(200, 300)],
        format = 'JPEG',
        options = { 'quality': 90},
        upload_to = article_image_path,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return f'/articles/{self.pk}/'
        # return reverse('articles:detail', args=[self.pk]) # /articles/10/
        return reverse('articles:detail', kwargs={'article_pk': self.pk}) # /articles/10/
        # 주의사항
        # reverse 함수에 args 랑 kwargs 를 동시에 인자로 보낼 수 없다.


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        # return self.
        return f'<Article({self.article_id}): Comment({self.pk})-{self.content}'

    