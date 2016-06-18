from django import forms

from .models import Post


class PostNormalForm(forms.Form):
    title = forms.CharField(help_text='글 제목은 네 글자 이상 넣으세요')
    content = forms.CharField(widget=forms.Textarea)


class PostForm(forms.ModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data

        if '바보' in cleaned_data['title']:
            self.add_error('title', '제목에서 바보 냄새가 난다')

    class Meta:
        model = Post
        fields = ['title', 'content', ]

