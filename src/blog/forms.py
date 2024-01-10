from django import forms
from django.forms import ModelForm, Textarea, TextInput

from .models import Article, Author, Category, Comment, ContactUs, Subscriber


class ArticleForm(ModelForm):
    author = forms.ModelChoiceField(
        queryset=Author.objects.all().order_by('first_name'),
        empty_label='Select author...',
        widget=forms.Select(attrs={
            'class': 'form_body_item_input',
        }),
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all().order_by('name'),
        empty_label='Select category...',
        widget=forms.Select(attrs={
            'class': 'form_body_item_input',
        }),
    )

    class Meta:
        model = Article
        fields = ['title', 'description', 'content', 'author', 'category']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form_body_item_input',
                'placeholder': 'title',
            }),
            'description': TextInput(attrs={
                'class': 'form_body_item_input',
                'placeholder': 'description',
            }),
            'content': Textarea(attrs={
                'class': 'form_body_item_input',
                'placeholder': 'text',
            })
        }


class SubscriberForm(ModelForm):
    author_id = forms.ModelChoiceField(
        queryset=Author.objects.all().order_by('first_name'),
        empty_label='Выберите автора...',
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
    )

    class Meta:
        model = Subscriber
        fields = ['name', 'email_to', 'author_id']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name подписчика'
            }),
            'email_to': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email подписчика',
            })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        widgets = {
            'comment_text': forms.Textarea(attrs={
                'rows': 4,
                'class': 'form_body_item_input',
                'placeholder': 'comment',
            }),
        }


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form_body_item_input',
                'placeholder': 'name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form_body_item_input',
                'placeholder': 'email',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form_body_item_input',
                'placeholder': 'subject',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form_body_item_input',
                'placeholder': 'message',
            }),
        }
