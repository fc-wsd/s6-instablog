from django.db import models

# Create your models here.



# 글 자체를 저장하는 Post 모델
class Post(models.Model):
    _status = (
        ('opnd', 'Opned',),
        ('clsd', 'Closed',),
        ('prvt', 'Privated',),
    )

    title = models.CharField(max_length=200, default='제목없음')# CharField라는 클래스를 ()로 호출하여 사용.
    content = models.TextField()# 전달인자를 안줘도 에러 안난다.

    # tags = models.ManyToManyField(Tag)# Tag 인자가 없다. 아직 밑에 Tag가 있는지 몰라...
    tags = models.ManyToManyField('Tag')# 문자열로 인자를 넘겨주면 된다!!! 왜???ㅠㅠㅠ못들음 ㅠㅠㅠ
    #
    category = models.ForeignKey('Category')

    status = models.CharField(max_length=20, choices=_status)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return '{}: {}'.format(self.id, self.title)
        return '{}: {}'.format(self.pk, self.title)# self.pk를  권장합니다 왜냠 id가 pk가 아닐수도 있기 때문

    class Meta:
        ordering = ['-created_at', '-pk']# 동시에 데이터가 들어오더라도 pk로 정렬 됨

class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return '{}: {}'.format(self.id, self.title)
        return '{}: {}'.format(self.pk, self.content)  # self.pk를  권장합니다 왜냠 id가 pk가 아닐수도 있기 때문


class Tag(models.Model):
    name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=100, default = '없음')

    def __str__(self):
        return self.title
