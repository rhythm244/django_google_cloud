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

class EmployeeForm(forms.ModelForm):
    class Meta:

        model = Employee
        fields = ('rank','first_name_thai','last_name_thai','first_name_eng','last_name_eng','telephone','position','position_other','still_service')

        labels = {
            
            "rank": "ยศ",
            "first_name_thai": "ชื่อ",
            "last_name_thai": "นามสกุล",
            "first_name_eng": "Firstname",
            "last_name_eng": "Lastname",
            "telephone": "เบอร์",
            "position": "ตำแหน่ง",
            "position_other": "ตำแหน่งอื่นๆ",
        }

        widgets = {
            'rank': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'ยศ',
            }),
            'first_name_thai': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
            }),
            'last_name_thai': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
            }),
            'first_name_eng': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
            }),
            'last_name_eng': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
            }),
            'telephone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'เบอร์โทรศัพท์ 10 ตัว ไม่ต้องขีด ไม่ต้องเว้นครับ',
            }),
            'position': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': '',
            }),
            'position_other': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ใส่ตำแหน่งย่อนะครับ :)',
            }),
            
        }

class LessonlearnForm(forms.ModelForm):
    class Meta:

        model = Lessonlearn
        fields = ('title','lesson','date_fly','airport','employee')

        labels = {
            
            "title": "หัวข้อ",
            "lesson": "Lesson learn",
            "date_fly": "วันที่บิน (วัน/เดือน/ปี ค.ศ.)",
            "airport": "สนามบิน", 
            "employee": "ผู้เขียน",
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'หัวข้อเรื่อง',
            }),
            'lesson': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '',
                'col': 30,
            }),
            'mission': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'ในประเทศ / ต่างประเทศ',
            }),
            'date_fly': forms.DateInput(format=('%m/%d/%Y') ,attrs={
                'class':'form-control', 'placeholder':'วัน/เดือน/ปี ค.ศ.', 'type':'date'}),
            
            'airport': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'สนามบิน',
            }),
            'employee': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'ผู้เขียน',
            }),
        }
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['airport'].queryset = Airport.objects.none()

    #     if 'mission' in self.data:
    #         try:
    #             mission_id = int(self.data.get('mission'))
    #             self.fields['airport'].queryset = City.objects.filter(mission_id=mission_id).order_by('airport')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['airport'].queryset = self.instance.mission.airport_set.order_by('name')
        
        




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
#                 'size': '40',
#                 'cols': 5,

#             }),
            
#         }