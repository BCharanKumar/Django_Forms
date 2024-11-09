from typing import Any
from django import forms
from app.models import *

class DemoError(BaseException):
    def __init__(self,msg):
        self.msg=msg


def check_for_char(data):
    if not data[0].isalpha():
        #raise  forms.DemoError('you details are invalid yaar...!')
        raise forms.ValidationError('the data is invalid yaaar')
    
def check_for_email(value):
    if not value[0].isalpha():
        raise forms.ValidationError('the data is invalid yaaar')


from django.core.validators import *
class StudentForm(forms.Form):
    g=[['MALE','male'],['FEMALE','female']]
    c=[['python','python'],['django','django'],('sql','sql')]
    sid=forms.IntegerField(validators=[MaxValueValidator(1000),MinValueValidator(250)])
    sname=forms.CharField(validators=[check_for_char,MinLengthValidator(6),MaxLengthValidator(25)])
    #sage=forms.IntegerField()
    semail=forms.EmailField(validators=[check_for_email,])
    remail=forms.EmailField()
    phone=forms.CharField(max_length=10,min_length=10,validators=[RegexValidator('[6-9]\d{9}')])
    botcatcher=forms.CharField(max_length=100)#,widget=forms.HiddenInput,required=False)
    #surl=forms.URLField()
    #sfees=forms.DecimalField()
    #spasswrod=forms.CharField(widget=forms.PasswordInput)
    #saddresss=forms.CharField(widget=forms.Textarea())
    #gender=forms.ChoiceField(choices=g)
    #gender=forms.ChoiceField(widget=forms.RadioSelect,choices=g)
    #course=forms.MultipleChoiceField(choices=c)
    #course=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=c)
    


    def clean_botcatcher(self):
        bc=self.cleaned_data['botcatcher']
        if len(bc)>10:
            raise forms.ValidationError('errir')        


    def clean(self):
        s=self.cleaned_data['semail']
        r=self.cleaned_data['remail']
        if s!=r:
            raise forms.ValidationError('error')



class TopicForm(forms.Form):
    tn=forms.CharField(validators=[check_for_char,])


class WebpageForm(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField(validators=[check_for_char,])
    url=forms.URLField()
    email=forms.EmailField()


class AccessRecordForm(forms.Form):
    name=forms.ModelChoiceField(queryset=WebPage.objects.all())
    author=forms.CharField()
    date=forms.DateField()