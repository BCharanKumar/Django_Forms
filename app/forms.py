from django import forms


class StudentForm(forms.Form):
    g=[['MALE','male'],['FEMALE','female']]
    c=[['python','python'],['django','django'],('sql','sql')]
    sid=forms.IntegerField()
    sname=forms.CharField()
    sage=forms.IntegerField()
    semail=forms.EmailField()
    surl=forms.URLField()
    sfees=forms.DecimalField()
    spasswrod=forms.CharField(widget=forms.PasswordInput)
    saddresss=forms.CharField(widget=forms.Textarea())
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(widget=forms.RadioSelect,choices=g)
    #course=forms.MultipleChoiceField(choices=c)
    course=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=c)
    


