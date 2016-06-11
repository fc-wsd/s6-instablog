from django.db import models


class Post(models.Model):
    """게시물을 다루는 모델
    """
    _status = (
        ('opn', 'Opened', ),
        ('clsd', 'Closed', ),
        ('prvt', 'Privated', ),
        ('scheduled', '예약', ),
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(max_length=20, choices=_status,)
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
