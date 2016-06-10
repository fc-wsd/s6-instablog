from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return '{}:{}'.format(self.id, self.title)

class Comment(models.Model):
    post = models.ForeignKey(Post, models.CASCADE)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.post.title, self.comment)

class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return '{}:{}'.format(self.id, self.tag)
