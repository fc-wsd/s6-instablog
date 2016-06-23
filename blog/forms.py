from django import forms

from .models import Post
from .models import Category


class PostNormalForm(forms.Form):
    title = forms.CharField(required =False , help_text ='글제목은 네글자 이상!')
    content = forms.CharField(widget = forms.Textarea)  #widget 은 Textarea로 표현해주기 위한것



class PostForm(forms.ModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data

        if '바보' in cleaned_data['title']:
            self.add_error('title','제목에서 바보스멜이 난다요')
        elif '겐지' in cleaned_data['title']:
            self.add_error('title','겐지가 함께한다')
    class Meta:
        model = Post
        fields = ['title','content','category','status']
        #fields = __all__   모델필드의 전체 필드를 폼으로 만듦
