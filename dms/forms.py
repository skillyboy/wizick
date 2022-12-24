# from tkinter import Widget
# from django.forms import ModelForm
# from django.contrib.auth import models
# from django.contrib.contenttypes import fields

from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import *
# from .forms import UploadFileForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email','password1','password2')
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'Last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control'}),
        }
        
class PasswordForm(PasswordChangeForm):
    old_password  = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Enter old password'}))
    new_password1  = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Enter New password'}))
    new_password2  = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Repeat New password'}))
    
    class Meta:
        model = User 
        fields = ('old_password', 'new_password1', 'new_password2')
        
    
    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
    
   

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileDetail
        fields = ('first_name','last_name','url','company','email','phone','p_img')
        Widgets = {
            'first_name': forms.TextInput(attrs={'class': 'inner-div', 'placeholder': 'First Name required'}),
            'last_name': forms.TextInput(attrs={'class': 'inner-div', 'placeholder': 'Last Name required'}),
            'company': forms.TextInput(attrs={'class': 'inner-div', 'placeholder': 'Company Name required'}),
            'url': forms.URLInput(attrs={'class': 'inner-div', 'placeholder': 'Company website required'}),
            'email': forms.EmailInput(attrs={'class': 'inner-div', 'placeholder': 'Email Adrdess required'}),
            'phone': forms.TextInput(attrs={'class': 'inner-div', 'placeholder': 'Phone Number required'}),
            'p_img': forms.FileInput(attrs={'class': 'inner-div', 'placeholder': 'Image upload required'})
        }
    

STATUS = [ 
    ('To do', 'To Do'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
    ]

class MypdfsForm(forms.ModelForm):
    class Meta:
        model = Mypdfs
        fields = ('pdf','parties', 'liabilitycap', 'consideration','term','effectivedate','expirydate','status','comment')
        widgets = {
            'pdf': forms.FileField(),
            'parties': forms.TextInput(attrs={'class': 'col'}),
            'liabilitycap': forms.TextInput(attrs={'class': 'col'}),
            'consideration': forms.TextInput(attrs={'class': 'col'}),
            'term': forms.TextInput(attrs={'class': 'col'}),
            'effectivedate': forms.TextInput(attrs={'class': 'card'}),
            'expirydate': forms.TextInput(attrs={'class': 'card'}),
            'status': forms.Select(attrs={'class': 'card'}, choices=STATUS),
            'comment': forms.TextInput(attrs={'class': 'text-area'}),
        }
    
    
STATUS = [ 
    ('To do', 'To Do'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
    ]    
class MyDocForm(forms.ModelForm):
    class Meta:
        model = MyDocs
        fields = ('doc','parties', 'liabilitycap', 'consideration','term','effectivedate','expirydate','status','comment')
        widgets = {
            'doc': forms.FileInput(attrs={'class': 'inner-div', 'placeholder': 'Image upload required'}),
            'parties': forms.TextInput(attrs={'class': 'col'}),
            'liabilitycap': forms.TextInput(attrs={'class': 'col'}),
            'consideration': forms.TextInput(attrs={'class': 'col'}),
            'term': forms.TextInput(attrs={'class': 'col'}),
            'effectivedate': forms.TextInput(attrs={'class': 'card'}),
            'expirydate': forms.TextInput(attrs={'class': 'card'}),
            'status': forms.Select(attrs={'class': 'card'}, choices=STATUS),
            'comment': forms.TextInput(attrs={'class': 'text-area'}),
        }
        
  
class MyEditorForm(forms.ModelForm):
    class Meta:
        model = Myeditor
        fields = ('parties', 'liabilitycap', 'consideration','term','effectivedate','expirydate','status','comment')
        widgets = {
            'parties': forms.TextInput(attrs={'class': 'col'}),
            'liabilitycap': forms.TextInput(attrs={'class': 'col'}),
            'consideration': forms.TextInput(attrs={'class': 'col'}),
            'term': forms.TextInput(attrs={'class': 'col'}),
            'effectivedate': forms.TextInput(attrs={'class': 'card'}),
            'expirydate': forms.TextInput(attrs={'class': 'card'}),
            'status': forms.Select(attrs={'class': 'card'}, choices=STATUS),
            'comment': forms.TextInput(attrs={'class': 'text-area'}),
        }
        
          
class TemplateForm(forms.ModelForm):
    class Meta:
        model = AdminTempClient
        fields = ('admintemp','date1ans','date2ans','clauseans','question1ans','question2ans','question3ans','question4ans','question5ans','question6ans','question7ans','question8ans','question9ans','question10ans','question11ans','question12ans','question13ans','question14ans','question15ans','question16ans','question17ans','question18ans','question19ans','question20ans','alternate1ans','alternate2ans','alternate3ans','alternate4ans','alternate5ans')
        widgets = {
            'admintemp': forms.TextInput(attrs={'class': 'sect-head'}),
            'date1ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'date2ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'clauseans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question1ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question2ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question3ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question4ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question5ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question6ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question7ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question8ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question9ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question10ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question11ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question12ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question13ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question14ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question15ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question16ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question17ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question18ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question19ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question20ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question21ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question22ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question23ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question24ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question25ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question26ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question27ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question28ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question29ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question30ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question31ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question32ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question33ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question34ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question35ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question36ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question37ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question38ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question39ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'question40ans': forms.TextInput(attrs={'class': 'sect-head'}),
            'alternate1ans': forms.Select(attrs={'class': 'sect-head'}),
            'alternate2ans': forms.Select(attrs={'class': 'sect-head'}),
            'alternate3ans': forms.Select(attrs={'class': 'sect-head'}),
            'alternate4ans': forms.Select(attrs={'class': 'sect-head'}),
            'alternate5ans': forms.Select(attrs={'class': 'sect-head'}),
            'category': forms.Select(attrs={'class': 'sect-head'}),

        }
          
class MyTemplateForm(forms.ModelForm):
    class Meta:
        model = ClientTemplates
        fields = ('body','date1', 'date2','question1', 'question2', 'question3','question4','question5','question6','question7','question8','question9','question10','question11', 'question12', 'question13','question14','question15','question16','question17','question18','question19','question20','question21', 'question22', 'question23','question24','question25','question26','question27','question28','question29','question30','question31', 'question32', 'question33','question34','question35','question36','question37','question38','question39','question40','date1ans','date2ans','question1ans', 'question2ans', 'question3ans','question4ans','question5ans','question6ans','question7ans','question8ans','question9ans','question10ans','question11ans', 'question12ans', 'question13ans','question14ans','question15ans','question16ans','question17ans','question18ans','question19ans','question20ans','question21ans', 'question22ans', 'question23ans','question24ans','question25ans','question26ans','question27ans','question28ans','question29ans','question30ans','question31ans', 'question32ans', 'question33ans','question34ans','question35ans','question36ans','question37ans','question38ans','question39ans','question40ans','category','title','parties', 'liabilitycap', 'consideration','term','effectivedate','expirydate','comment')
        widgets = {
            'body': forms.TextInput(attrs={'class': 'col'}),
            'date1': forms.TextInput(attrs={'class': 'card'}),
            'date2': forms.TextInput(attrs={'class': 'card'}),
            'question1': forms.TextInput(attrs={'class': 'card'}),
            'question2': forms.TextInput(attrs={'class': 'card'}),
            'question3': forms.TextInput(attrs={'class': 'card'}),
            'question4': forms.TextInput(attrs={'class': 'card'}),
            'question5': forms.TextInput(attrs={'class': 'card'}),
            'question6': forms.TextInput(attrs={'class': 'card'}),
            'question7': forms.TextInput(attrs={'class': 'card'}),
            'question8': forms.TextInput(attrs={'class': 'card'}),
            'question9': forms.TextInput(attrs={'class': 'card'}),
            'question10': forms.TextInput(attrs={'class': 'card'}),
            'question11': forms.TextInput(attrs={'class': 'card'}),
            'question12': forms.TextInput(attrs={'class': 'card'}),
            'question13': forms.TextInput(attrs={'class': 'card'}),
            'question14': forms.TextInput(attrs={'class': 'card'}),
            'question15': forms.TextInput(attrs={'class': 'card'}),
            'question16': forms.TextInput(attrs={'class': 'card'}),
            'question17': forms.TextInput(attrs={'class': 'card'}),
            'question18': forms.TextInput(attrs={'class': 'card'}),
            'question19': forms.TextInput(attrs={'class': 'card'}),
            'question20': forms.TextInput(attrs={'class': 'card'}),
            'question21': forms.TextInput(attrs={'class': 'card'}),
            'question22': forms.TextInput(attrs={'class': 'card'}),
            'question23': forms.TextInput(attrs={'class': 'card'}),
            'question24': forms.TextInput(attrs={'class': 'card'}),
            'question25': forms.TextInput(attrs={'class': 'card'}),
            'question26': forms.TextInput(attrs={'class': 'card'}),
            'question27': forms.TextInput(attrs={'class': 'card'}),
            'question28': forms.TextInput(attrs={'class': 'card'}),
            'question29': forms.TextInput(attrs={'class': 'card'}),
            'question30': forms.TextInput(attrs={'class': 'card'}),
            'question31': forms.TextInput(attrs={'class': 'card'}),
            'question32': forms.TextInput(attrs={'class': 'card'}),
            'question33': forms.TextInput(attrs={'class': 'card'}),
            'question34': forms.TextInput(attrs={'class': 'card'}),
            'question35': forms.TextInput(attrs={'class': 'card'}),
            'question36': forms.TextInput(attrs={'class': 'card'}),
            'question37': forms.TextInput(attrs={'class': 'card'}),
            'question38': forms.TextInput(attrs={'class': 'card'}),
            'question39': forms.TextInput(attrs={'class': 'card'}),
            'question40': forms.TextInput(attrs={'class': 'card'}),
            'date1ans': forms.TextInput(attrs={'class': 'card'}),
            'date2ans': forms.TextInput(attrs={'class': 'card'}),
            'question1ans': forms.TextInput(attrs={'class': 'card'}),
            'question2ans': forms.TextInput(attrs={'class': 'card'}),
            'question3ans': forms.TextInput(attrs={'class': 'card'}),
            'question4ans': forms.TextInput(attrs={'class': 'card'}),
            'question5ans': forms.TextInput(attrs={'class': 'card'}),
            'question6ans': forms.TextInput(attrs={'class': 'card'}),
            'question7ans': forms.TextInput(attrs={'class': 'card'}),
            'question8ans': forms.TextInput(attrs={'class': 'card'}),
            'question9ans': forms.TextInput(attrs={'class': 'card'}),
            'question10ans': forms.TextInput(attrs={'class': 'card'}),
            'question11ans': forms.TextInput(attrs={'class': 'card'}),
            'question12ans': forms.TextInput(attrs={'class': 'card'}),
            'question13ans': forms.TextInput(attrs={'class': 'card'}),
            'question14ans': forms.TextInput(attrs={'class': 'card'}),
            'question15ans': forms.TextInput(attrs={'class': 'card'}),
            'question16ans': forms.TextInput(attrs={'class': 'card'}),
            'question17ans': forms.TextInput(attrs={'class': 'card'}),
            'question18ans': forms.TextInput(attrs={'class': 'card'}),
            'question19ans': forms.TextInput(attrs={'class': 'card'}),
            'question20ans': forms.TextInput(attrs={'class': 'card'}),
            'question21ans': forms.TextInput(attrs={'class': 'card'}),
            'question22ans': forms.TextInput(attrs={'class': 'card'}),
            'question23ans': forms.TextInput(attrs={'class': 'card'}),
            'question24ans': forms.TextInput(attrs={'class': 'card'}),
            'question25ans': forms.TextInput(attrs={'class': 'card'}),
            'question26ans': forms.TextInput(attrs={'class': 'card'}),
            'question27ans': forms.TextInput(attrs={'class': 'card'}),
            'question28ans': forms.TextInput(attrs={'class': 'card'}),
            'question29ans': forms.TextInput(attrs={'class': 'card'}),
            'question30ans': forms.TextInput(attrs={'class': 'card'}),
            'question31ans': forms.TextInput(attrs={'class': 'card'}),
            'question32ans': forms.TextInput(attrs={'class': 'card'}),
            'question33ans': forms.TextInput(attrs={'class': 'card'}),
            'question34ans': forms.TextInput(attrs={'class': 'card'}),
            'question35ans': forms.TextInput(attrs={'class': 'card'}),
            'question36ans': forms.TextInput(attrs={'class': 'card'}),
            'question37ans': forms.TextInput(attrs={'class': 'card'}),
            'question38ans': forms.TextInput(attrs={'class': 'card'}),
            'question39ans': forms.TextInput(attrs={'class': 'card'}),
            'question40ans': forms.TextInput(attrs={'class': 'card'}),
            'category': forms.TextInput(attrs={'class': 'card'}),  
            'title': forms.TextInput(attrs={'class': 'card'}),
            'parties': forms.TextInput(attrs={'class': 'card'}),
            'liabilitycap': forms.TextInput(attrs={'class': 'card'}),
            'consideration': forms.TextInput(attrs={'class': 'card'}),
            'term': forms.TextInput(attrs={'class': 'card'}),
            'effectivedate': forms.TextInput(attrs={'class': 'card'}),
            'expirydate': forms.TextInput(attrs={'class': 'card'}),
            'comment': forms.TextInput(attrs={'class': 'text-area'}),           
        }
        