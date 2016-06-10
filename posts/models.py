from django.db import models

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, null=False)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    regdate = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category_rel = models.ManyToManyField('Category')

    class Meta:
        db_table = 'blog_post'

    def __str__(self):
        return '{}:{}'.format(self.pk, self.title)

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, null=False)
    memo = models.CharField(max_length=200, null=False)
    regdate = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    post_fk = models.ForeignKey(Post)

    class Meta:
        db_table = 'blog_comment'

    def __str__(self):
        return '{}:{}'.format(self.pk, self.memo)

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, null=False)

    class Meta:
        db_table = 'blog_category'

    def __str__(self):
        return '{}:{}'.format(self.pk, self.name)