from typing import Any
from django import forms
from app.models import *



def check_for_char(data):
    if not data[0].isalpha():
        raise forms.ValidationError('the data is invalid yaaar')
    
def check_for_email(value):
    if not value[0].isalpha():
        raise forms.ValidationError('the data is invalid yaaar')



class StudentForm(forms.Form):
    g=[['MALE','male'],['FEMALE','female']]
    c=[['python','python'],['django','django'],('sql','sql')]
    sid=forms.IntegerField()
    sname=forms.CharField(validators=[check_for_char,])
    #sage=forms.IntegerField()
    semail=forms.EmailField(validators=[check_for_email,])
    remail=forms.EmailField()
    #surl=forms.URLField()
    #sfees=forms.DecimalField()
    #spasswrod=forms.CharField(widget=forms.PasswordInput)
    #saddresss=forms.CharField(widget=forms.Textarea())
    #gender=forms.ChoiceField(choices=g)
    #gender=forms.ChoiceField(widget=forms.RadioSelect,choices=g)
    #course=forms.MultipleChoiceField(choices=c)
    #course=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=c)
    
    def clean(self):
        s=self.cleaned_data['semail']
        r=self.cleaned_data['remail']
        if s!=r:
            raise forms.ValidationError('error')
class TopicForm(forms.Form):
    tn=forms.CharField()


class WebpageForm(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField()
    url=forms.URLField()
    email=forms.EmailField()


class AccessRecordForm(forms.Form):
    name=forms.ModelChoiceField(queryset=WebPage.objects.all())
    author=forms.CharField()
    date=forms.DateField()