from django import forms
from django.forms import ModelForm
from .models import *
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.db import models

class PictureForm(forms.ModelForm):
    class Meta:

        model = Picture
        fields = ('employee_image',)


# class ListingForm(forms.ModelForm): #จะเขียนว่า class CreateList(ModelForm) เฉยๆก็ได้
#     class Meta:
#         model = Listing
#         #เนื่องจากตัว max_price มี class IntegerRangeField ที่เป็นตัวกำหนดค่าของ max, min ragne มาด้วย ทำให้ต้อง import IntegerRange มาด้วย
#         fields = ('title', 'start_bid', 'max_price','descript', 'photo', 'category')

# class BidForm(forms.ModelForm):
#     class Meta:
#         model = Bid
#         fields = ['bid']

#         labels = {
#             "bid": "",
#         }

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['comment']

#         label = {
#             'comment': 'comment',
#         }

#         widgets = {

#             'comment': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'post a comment',
#                 'rows': 5,
#                 'cols': 5,

#             }),
            
#         }