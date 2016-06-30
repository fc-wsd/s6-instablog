from django.db import models


class Post(models.Model):
    _status = (
        ('public', 'Public Post',),
        ('private', 'Private Post',),
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 공개글 비공개글 설정,
    # 추후 이웃 공개 기능 등이 들어갈 수 있으므로 boolean 이 아닌 enum으로 처리
    status = models.CharField(max_length=20, choices=_status, default='public')
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return '{}: {}'.format(self.pk, self.content)

    class Meta:
        ordering = ['-created_at', '-pk']   # 정렬조건


class Comment(models.Model):
    _status = (
        ('public', 'Public Comment',),
        ('private', 'Private Comment',),
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 될 때만 값을 넣어준다
    updated_at = models.DateTimeField(auto_now=True)  # 항상 값을 넣어준다
    # 공개댓글 비공개댓글 설정,
    # 추후 이웃 공개 기능 등이 들어갈 수 있으므로 boolean 이 아닌 enum으로 처리
    status = models.CharField(max_length=20, choices=_status, default='public')

    def __str__(self):
        return '{}: {}'.format(self.pk, self.content)

    class Meta:
        ordering = ['created_at', '-pk']  # 정렬조건


class Category(models.Model):
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.pk, self.title)


class Tag(models.Model):
    title = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.pk, self.title)
