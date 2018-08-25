# from django import forms

#from .models import Post

# class FormPost(forms.ModelForm):
#
#     class Meta:
#         model=Post
#         fields =[
#             'title' ,
#             'content' ,
#              ]
from django import forms
from .models import Post
from django.shortcuts import render
from django.urls import reverse
from .models import Comment
class FormPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'user',
            'title',
            'content',
            'image',
            'draft',
        ]



class PostFilter(forms.Form):
    choice=(('T','taslak'),('TO','No Taslak'),('A','All'))
    secme= forms.CharField(label='Orphanism degrees',widget=forms.Select(choices=choice,attrs={'class':'PostControl'}))
#id_con

class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=[
            'name',
            'content',
        ]
    widgets={
        'name': forms.Textarea(attrs={'class':'name'})
    }