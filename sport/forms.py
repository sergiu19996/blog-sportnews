from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='Content', widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))

    class Meta:
        model = Comment
        fields = ['content', 'author'] 

    def clean_content(self):
        content = self.cleaned_data['content']
        return content