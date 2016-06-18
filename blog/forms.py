from django import forms


class PostNormalForm(forms.Form):
    title = forms.CharField(help_text='글 제목은 네 글자 이상 넣으세요')
    content = forms.CharField(widget=forms.Textarea)


