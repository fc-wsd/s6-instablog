from django.db import models

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    writer = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.TextField()
    regdate = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    fk_category_id = models.ManyToManyField('Category')

    def __str__(self):
        return '{}:{}'.format(self.pk, self.title, self.writer)

    class Meta:
        db_table = 'hskim_post'

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    writer = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)
    memo = models.CharField(max_length=200)
    regdate = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    fk_post_id = models.ForeignKey(Post)

    def __str__(self):
        return '{}:{}:{}'.format(self.pk, self.memo, self.writer)

    class Meta:
        db_table = 'hskim_comment'

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return '{}:{}'.format(self.pk, self.name)

    class Meta:
        db_table = 'hskim_category'