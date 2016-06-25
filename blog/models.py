from django.db import models
from django.conf import settings


class Post(models.Model):
    _status = (
        ('opn', 'Opened', ),
        ('clsd', 'Closed', ),
        ('prvt', 'Privated', ),
        ('scheduled', '예약', ),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    title = models.CharField(max_length=200, default='제목없음')
    content = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(max_length=20, choices=_status,)

    # 추가~
    image = models.ImageField(null=True, blank=True, upload_to='%Y/%m/%d')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/blog/posts/{}/'.format(self.pk)

    class Meta:
        ordering = ['-created_at', '-pk']


class Comment(models.Model):
    post = models.ForeignKey(Post, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {}'.format(self.pk, self.content)


class Tag(models.Model):
    name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=100, default='없음')

    def __str__(self):
        return self.title
