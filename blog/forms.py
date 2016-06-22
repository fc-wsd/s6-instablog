from django import forms
from .models import Post


class PostNormalForm(forms.Form):
    title = forms.CharField() # title에 대한 validator
    content = forms.CharField(widget=forms.Textarea) # content에 대한 validator


class PostForm(forms.ModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data

        if '바보' in cleaned_data['title']:
            self.add_error('title', '제목에서 바보 냄새가 난다')

    class Meta:
        model = Post
        fields = ['title', 'content', ] # 실제 화면에 보여줄 필드들

