from django.db import models


class Post(models.Model):
    _status = (
        ('opn', 'Open', ),
        ('cls', 'Close', ),
        ('prvt', 'Private', ),
        ('rsv', 'Reserved', ),
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)    # 파이썬에서 체크하는 항목 : migration 필요 없음.
    category = models.ForeignKey('Category', blank=True)
    status = models.CharField(max_length=20, choices=_status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self

    class Meta:
        ordering = ['-created_at', '-pk']


class Comment(models.Model):
    post = models.ForeignKey(Post, null=True)   # DB에서 null 허용 : migration 필요. blank=True와 다름.
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
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name