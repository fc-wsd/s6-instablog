from django.db import models


class Post(models.Model):
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
    category = models.ForeignKey('Category')

    def __str__(self):
        return '{}: {}'.format(self.pk, self.title)

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
    name = models.CharField(max_length=20, null=False, unique=True)

    def __str__(self):
        return self.name