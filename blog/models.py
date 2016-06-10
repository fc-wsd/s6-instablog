from django.db import models

class Post(models.Model):
    _status =(
        ('opn','Open',),    #실제로는 앞에 코드값이 들어가고 보여줄땐 get_필드명_display()로 뒤에 값이 나옴 언더바는 private를 표현
        ('clsd','Closed',),
        ('prvt','Privated',),
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(max_length=20,choices =_status)
    category = models.ForeignKey('Category')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    def __str__(self):
        return '{} : {}'.format(self.pk,self.title)

    class Meta:
        ordering = ['-created_at','-pk']

class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '{} : {}'.format(self.pk,self.content)

class Tag(models.Model):
    name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '{} : {}'.format(self.pk,self.name)

class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '{} : {}'.format(self.pk,self.name)
        
