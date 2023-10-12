from django import forms
from .models import Post

# choices = [('coding','coding'),('sports','sports'),('entertainment','entertainment')]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','body')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control col-2'}),
            # 'header_image' : forms.ImageField(attrs={'class': 'form-control col-2'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control col-2 '}),
            'author' : forms.Select(attrs={'class': 'form-control col-2'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
            # 'snippet' : forms.Textarea(attrs={'class': 'form-control col-5'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control col-2'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control col-2 '}),
            # 'author' : forms.Select(attrs={'class': 'form-control col-2'}),
            'body' : forms.Textarea(attrs={'class': 'form-control rows-5'}),
            # 'snippet' : forms.Textarea(attrs={'class': 'form-control col-5'}),
        }