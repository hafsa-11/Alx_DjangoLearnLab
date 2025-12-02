from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Tag
from .models import Comment
from taggit.forms import TagWidget

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 3})
        }
class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Separate tags with commas")

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

    def save(self, commit=True):
        post = super().save(commit=False)

        if commit:
            post.save()

        tag_list = self.cleaned_data["tags"]
        tag_names = [t.strip() for t in tag_list.split(",") if t.strip()]

        for name in tag_names:
            tag, created = Tag.objects.get_or_create(name=name)
            post.tags.add(tag)

        return post
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
        widgets = {
            "tags": TagWidget(),  
        }
