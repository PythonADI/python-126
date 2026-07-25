from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control mb-2",
                "placeholder": "Title",
            }),
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 2,
                "placeholder": "What's on your mind?",
            }),
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if not title:
            raise forms.ValidationError("Title cannot be empty.")
        if title == title.upper() and title != title.lower():
            raise forms.ValidationError("Please don't SHOUT — turn off Caps Lock.")
        return title


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.TextInput(attrs={
                "class": "form-control form-control-sm rounded-pill",
                "placeholder": "Write a comment...",
            }),
        }
