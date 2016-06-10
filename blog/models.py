from django.db import models

# loaddata를 통해 PK 1을 만들어 둔다.
class Category(models.Model):
    _category_status = (
        ('opn', 'Opened', ),
        ('clsd', 'Closed', ),
    )

    name = models.CharField(max_length=40)
    priority = models.IntegerField()
    status = models.CharField(max_length=20, choices=_category_status)
    hierarchy = models.CharField(max_length=12)

    def __str__(self):
        bar = '-' * (len(self.hierarchy) // 4 - 1)
        return '{bar} {name}'.format(bar=bar, name=self.name)

    class Meta:
        ordering = [ 'hierarchy', 'priority', 'pk']

class Post(models.Model):
    _post_status = (
        ('opn', 'Opened', ),
        ('clsd', 'Closed', ),
        ('prvt', 'Privated', ),
    )

    category = models.ForeignKey(Category, default=1)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=_post_status)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return '{pk} : {category_name} - {title}'.format(pk=self.pk, category_name=self.category.name, title=self.title)

    class Meta:
        ordering = ['-created_at', '-pk']

class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{pk} : {post_title} - {content}'.format(pk=self.pk, post_title=self.post.title, content=self.content)

class Tag(models.Model):
    name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
