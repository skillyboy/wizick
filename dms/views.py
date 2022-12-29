import base64
from http import client
from xml.dom.minidom import DocumentFragment
from django.shortcuts import render,redirect,get_object_or_404

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
# from xhtml2pdf import pisa
# from .forms import UploadFileForm  
# from io import BytesIO
# import PyPDF2 
# from django.utils.crypto import get_random_string
# from django.core.paginator import Paginator
# from django.template.loader import render_to_string
# from docx import Document

# from django.views.generic import View
# from django.http import JsonResponse
# from django.views import View
# from django.views import generic

# email sending 
from django.core.mail import EmailMessage
from django.conf import settings
# email sending done
from django.utils import timezone
# password reset modules 
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
# password reset modules done

# ==========AUTH==========================================
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import update_session_auth_hash
# from django.contrib import auth
# from multiprocessing.connection import Client
import re
from . models import *
from . forms import *

from . serializers import *
from . models import * 
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.validators import ValidationError
# from rest_framework.response import Response
# from rest_framework import status

# import os
# import urllib.parse


# class ProfileDetailListView (RetrieveUpdateDestroyAPIView):
#     queryset = ProfileDetail.objects.all()
#     serializer_class = ProfileDetailSerializer 
#     def delete (self, request, pk):
#         profile= get_object_or_404(ProfileDetail, pk)
#         if profile == 1:
#             raise ValidationError(' Sorry Cannot delete this objects')
#         profile.delete()
#         return Response ('hello im here' )



# class AdminTemplist(ListCreateAPIView):
#     queryset = AdminTemp.objects.all()
#     serializers_class = AdminTempSerializer
    
#     def get_queryset(self):
#         return AdminTemp.objects.all()

# class AdminTemplist(ListCreateAPIView):
#     queryset = AdminTemp.objects.all()
#     serializersclass = AdminTempSerializer
    
#     def get_queryset(self):
#         return AdminTemp.objects.all()











# Create your views here.
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    temp= {}
    list = []
    allcontract= 0
    
    generated = Generatedmytemplate.objects.all().count()
    mygenerated = Generatedtemplate.objects.all().count()
    allcontract = int(generated + mygenerated)
    

    clientcategory = ClientCategory.objects.all()
    for temp in clientcategory :  
        count = ClientTemplates.objects.filter(clientcategory_id=temp.id).count()
        list.append(count)
    print(list)
    print(temp)
    print(allcontract)
    
    context={
        'profile': profile,
        'clientcategory' :clientcategory,
        'temp' :temp,
        'list' :list,
        'allcontract' :allcontract,
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='signin')
def home (request):      
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    mypdf = Mypdfs.objects.filter(user__username = request.user.username)
    mydocs = MyDocs.objects.filter(user__username = request.user.username)
    terminology = Terminology.objects.all()
    clauses = ClauseLib.objects.all()
    doctype = FileType.objects.all()   
    context={
    
        'profile': profile,
        'doctype': doctype,
        'mypdf': mypdf,
        'mydocs': mydocs,
        'terminology': terminology,
        'clauses':clauses, 
        # 'clienttemps':clienttemps,  
    }
    return render(request, 'homepage.html', context)

def clause(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    clauses = ClauseLib.objects.all()
    context={
        'profile':profile, 
        'clauses':clauses, 
        
    }    
    
    return render(request, 'clause.html', context)

def tinymce(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    tinymce = ClauseLib.objects.all()
    context={
        'profile':profile, 
        'tinymce':tinymce, 
    }    
    
    return render(request, 'tinymce.html', context)

def insight(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    mypdf = Mypdfs.objects.filter(user__username= request.user.username )
    mydocs = MyDocs.objects.filter(user__username= request.user.username)
    mydrafts = Myeditor.objects.filter(user__username= request.user.username)
    
    context={
        'profile':profile, 
        'mydocs':mydocs, 
        'mypdf':mypdf, 
        'mydrafts':mydrafts, 
    }    
    
    return render(request, 'insight.html', context)



def legal(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    legal = Terminology.objects.all()
    context={
        'legal':legal, 
        'profile':profile, 
    }    
    return render(request, 'legal.html', context)

def editor(request):
    editor = Terminology.objects.all()
    context={
        'editor':editor, 
    }    
    return render(request, 'editor.html', context)


def notification(request):
    notification = Terminology.objects.all()
    context={
        'notification':notification, 
    }    
    
    return render(request, 'notification.html', context)

def admintemp(request):
    cattemps = Category.objects.all()
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    
    context={
        'cattemps': cattemps,
        'profile': profile,
    } 
    return render(request, 'admintemp.html', context)


def admintempdetails(request, id):
    profile = ProfileDetail.objects.get(username__username= request.user.username)

    admintemp = AdminTemp.objects.filter(category_id = id)
    
    context={
        'admintemp':admintemp,
        'profile': profile,
        
    }
    return render(request, 'admintempdetails.html', context)


def clienttemp(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    cattemps = ClientCategory.objects.all()
    mytemp = ClientTemplates.objects.filter(user__username= request.user.username)
    
    context={
        'mytemp':mytemp,
        'profile': profile,
        'cattemps': cattemps,
        
        
    }
    return render(request, 'clienttemp.html', context)


def clienttempdetails(request, id):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    cat = ClientCategory.objects.get(pk= id)
    mytemplate = ClientTemplates.objects.filter(category= cat.temp_class).all()
    
    context={
        'mytemplate':mytemplate,
        'profile': profile,
    }
    return render(request, 'clienttempdetails.html', context)



def gentemp(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    cattemps = Generatedtemplate.objects.all()
    mytemps = Generatedmytemplate.objects.all()
    
    
    context={
        'cattemps':cattemps,
        'profile': profile,
        'mytemps': mytemps,
        
        
    }
    return render(request, 'gentemp.html', context)


def gentempdetails(request, id):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    gentemps = Generatedtemplate.objects.get(pk=id)
    
    
    
    context={
        'gentemps':gentemps,
        'profile': profile,
    }
    return render(request, 'clienteditor.html', context)

def mygentempdetails(request, id):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    gentemps = Generatedmytemplate.objects.get(pk=id)
    
    
    
    context={
        'gentemps':gentemps,
        'profile': profile,
    }
    return render(request, 'clienteditor.html', context)

def templist(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)

    context={
        'profile': profile,
    }
    return render(request, 'templist.html', context)

def question (request,id):
    admintemp = AdminTemp.objects.get(pk=id)
    clauses = ClauseLib.objects.all()

    context={
        'admintemp': admintemp,
        # 'admintempclient': admintempclient,
        'clauses': clauses,
        # 'admintempclient': admintempclient,
        
    }
    return render(request, 'question.html', context)


# def replace(source, replacements):
#     finder = re.compile("|".join(re.escape(k) for k in replacements.keys())) # matches every string we want replaced
#     result = []
#     pos = 0
#     while True:
#         match = finder.search(source, pos)
#         if match:
#             # cut off the part up until match
#             result.append(source[pos : match.start()])
#             # cut off the matched part and replace it in place
#             result.append(replacements[source[match.start() : match.end()]])
#             pos = match.end()
#         else:
#             # the rest after the last match
#             result.append(source[pos:])
#             break
#     return "".join(result)
 







    


# def savetemp(request):
#     user = User.objects.get(username=request.user)
#     if request.method =='POST':
#         profile = User.objects.get(username= request.user)
#         body= request.POST.get('body')
#         if body:
#             newcopy = MyTemplate.objects.create(body=body)  
#             newcopy.user = user
#             newcopy.save()
#             messages.success(request, "Document saved successfully")
#     return redirect('mytemplate')



def addtemp(request):
    form = TemplateForm()
    if request.method == "POST":
        body = request.POST['body']
        # category = request.POST['category']
        # title = request.POST['title']
        form = TemplateForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            new.save()
            
            messages.success(request, 'Template saved')
            return redirect('mytemplate')
        else:
            messages.error(request, form.errors)
            return redirect('mytemplate')
    return render(request, 'mytemplate.html')





# def clienteditor(request):
#     # user = User.objects.get(username=request.user)
         
            
#     # allkeys = ["{Q1}","{Q2}","{Q3}", "{Q4}", "{Q5}","{Q6}", "{Q7}","{Q8}","{Q9}","{Q10}","{Q11}","{Q12}","{Q13}","{Q14}", "{Q15}","{Q16}", "{Q17}", "{Q18}", "{Q19}","{20}","{ALT1}","{ALT2}","{ALT3}","{ALT4}","{ALT5}","{D1}","{D2}","{CLS}"]
#     # questions = [(question1),(question2), (question3), (question4), (question5),(question6),(question7), (question8), (question9), (question10),(question11),(question12), (question13), (question14), (question15),(question16),(question17), (question18), (question19), (question20),(alternate1ans),(alternate2ans),(alternate3ans),(alternate4ans),(alternate5ans),(date1ans),(date2ans),(clauseans-)]
#     # replacements = {key: value for key, value in zip(allkeys, questions)}
#     # newtemp= (str(replace(body, replacements)))
    
#     return render(request, 'docmanager.html')

def saveeditor(request):
    user = User.objects.get(username=request.user)
    url = request.POST.get('HTTP_REFERER')
    if request.method =='POST':
        profile = User.objects.get(username= request.user)
        body= request.POST.get('body')
        if body== '':
            messages.warning(request, "This is an empty folder")
        else: 
            newcopy = Myeditor.objects.create(body=body)  
            newcopy.project_done = False
            newcopy.user = user
            newcopy.profile = profile
            newcopy.save()
            messages.success(request, "Document saved successfully")
            # return redirect(url)
    return redirect('editormanager')



def withoutinsight(request):
    user = User.objects.get(username=request.user)
    url = request.POST.get('HTTP_REFERER')
    if request.method =='POST':
        profile = User.objects.get(username= request.user)
        body= request.POST.get('body')
        if body== '':
            messages.warning(request, "This is an empty folder")
        else: 
            newcopy = Myeditor.objects.create(body=body)  
            newcopy.project_done = False
            newcopy.user = user
            newcopy.profile = profile
            newcopy.save()
            messages.success(request, "withoutinsight")
            # return redirect(url)
    return redirect('home')

# ============================
        # Insight
# ============================
def allmanager(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    
    mydocs = MyDocs.objects.filter(user__username = request.user.username)
    mypdf = Mypdfs.objects.filter(user__username = request.user.username)
    editor = Myeditor.objects.filter(user__username = request.user.username)
    
    context={
        'profile': profile,
        
        'mydocs': mydocs,
        'mypdf': mypdf,
        'editor': editor,              
    }   
    return render(request, 'docmanager.html', context)


def docmanager(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    mydocs = MyDocs.objects.filter(user__username = request.user.username)
    context={
        'profile': profile,
        'mydocs': mydocs,
        
    }   
    return render(request, 'docmanager.html', context)

def pdfmanager(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    mypdf = Mypdfs.objects.filter(user__username = request.user.username)

    context={
        'mypdf': mypdf,
        'profile': profile,
    }   
    return render(request, 'pdfmanager.html', context)

def deletepdffile(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        delfile = request.POST['itemid']
        Mypdfs.objects.filter(pk=delfile).delete()
        return redirect(url)

def editormanager(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    editor = Myeditor.objects.filter(user__username = request.user.username)
    
    context={
        'editor': editor,
        'profile': profile,
    }   
    return render(request, 'editormanager.html', context)

def mytempmanager(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    mytemp = ClientTemplates.objects.filter(user__username = request.user.username).all()
    context={
        'profile': profile,
        'mytemp': mytemp
    }   
    return render(request, 'mytempmanager.html', context)
# ==========================PDF ===============================================
def createpdfinsight(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    modifypdf = request.POST['modifypdf']
    insight = Mypdfs.objects.get(pk=modifypdf)
    
    context={
        'profile': profile,
        'insight': insight,
        
    }   
    return render(request, 'pdfinsight.html', context)

def createpdfinsightform(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    modifypdf = request.POST['modifypdf']
    insight = Mypdfs.objects.get(pk=modifypdf)
    form = MypdfsForm(instance= insight)
    if request.method == "POST":
        form = MypdfsForm(request.POST, instance=insight)
        if form.is_valid():
            form.save()
            return redirect('pdfmanager')
        else:
            messages.error(request, form.errors)
            return redirect('createpdfinsight')
    context={
        'profile': profile,
        'insight': insight,        
    }   
    return render(request, 'pdfinsight.html', context)


# ========================DOC INSIGHT=========================================
def createdocinsight(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    modifydoc = request.POST['modifydoc']
    insight = MyDocs.objects.get(pk=modifydoc)
    
    context={
        'profile': profile,
        'insight': insight,
        
    }   
    return render(request, 'docinsight.html', context)

def createdocinsightform(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    modifydoc = request.POST['modifydoc']
    insight = MyDocs.objects.get(pk=modifydoc)
    form = MyDocForm(instance= insight)
    if request.method == "POST":
        form = MyDocForm(request.POST, instance=insight)
        if form.is_valid():
            form.save()
            return redirect('docmanager')
        else:
            messages.error(request, form.errors)
            return redirect('createdocinsight')
    context={
        'profile': profile,
        'insight': insight,        
    }   
    return render(request, 'docinsight.html', context)


# ======================== Draft INSIGHT=========================================
def createdraftinsight(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    modifydraft = request.POST['modifydraft']
    insight = Myeditor.objects.get(pk=modifydraft)
    
    context={
        'profile': profile,
        'insight': insight,
        
    }   
    return render(request, 'editinsight.html', context)

def createdraftinsightform(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    modifydraft = request.POST['modifydraft']
    insight = Myeditor.objects.get(pk=modifydraft)
    form = MyEditorForm(instance= insight)
    if request.method == "POST":
        form = MyEditorForm(request.POST, instance=insight)
        if form.is_valid():
            form.save()
            return redirect('editormanager')
        else:
            messages.error(request, form.errors)
            return redirect('createeditinsight')
    context={
        'profile': profile,
        'insight': insight,        
    }   
    return render(request, 'insightedit.html', context)



# ======================== Mytemplate INSIGHT=========================================
def createtempinsight(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    modifytemp = request.POST['modifytemp']
    insight = ClientTemplates.objects.get(pk=modifytemp)
    
    context={
        'profile': profile,
        'insight': insight,
        
    }   
    return render(request, 'tempinsight.html', context)

def createtempinsightform(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    modifytemp = request.POST['modifytemp']
    insight = ClientTemplates.objects.get(pk=modifytemp)
    form = MyTemplateForm(instance= insight)
    if request.method == "POST":
        form = MyTemplateForm(request.POST, instance=insight)
        if form.is_valid():
            form.save()
            return redirect('mytempmanager')
        else:
            messages.error(request, form.errors)
            return redirect('createtempinsight')
    context={
        'profile': profile,
        'insight': insight,        
    }   
    return render(request, 'insighttemp.html', context)






# =================================================================
def saveeditwithinsight(request):
    body = ''
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    insight = Myeditor.objects.get(user__username = request.user.username)
    form = MyEditorForm(instance= insight)
    if request.method == "POST":
        form = MyEditorForm(request.POST, instance=insight)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request, form.errors)
            return redirect('home')
        
    context={
        'profile': profile,
    }      
    return render(request, 'insightedit.html', context)

# ==========================================================
def demo(request):
    return render(request, 'demo.html')

def signin(request):  
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        # welcome = user.first_name.title()
        if user:
            login(request, user)
            messages.success(request, f' welcome!')
            return redirect('home')
        else:
            messages.info(request, 'Email/Password incorrect')
            return redirect('signin')
    return render (request, 'signin.html')

def logoutfunc(request):
    logout(request)
    return redirect('signin')


def register(request):
    form = SignupForm()
    if request.method == "POST":
        username = request.POST['username']
        company = request.POST['company']
        phone = request.POST['phone']
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.email = username
            new_user.save()
            new_profile = ProfileDetail(username= new_user)
            new_profile.first_name = new_user.first_name
            new_profile.last_name= new_user.last_name
            new_profile.email = username
            new_profile.company = company
            new_profile.phone = phone
            new_profile.date_joined = timezone.localtime(timezone.now())
            new_profile.save()

            login(request, new_user)
            messages.success(request, 'Signup Successful!')
            return redirect('home') 
        else:
            messages.error(request, form.errors)
            return redirect('register')
    return render(request, 'register.html')



def reset(request):
    return render(request, 'reset.html')


# def password(request):
    # if request.method == 'POST':
    #     cpassword = request.POST.get('cpassword')
    #     password1 = request.POST.get('password1')
    #     password2 = request.POST.get('password2')        
          
    #     if password1!= password2:
    #         messages.error(request,"Passwords do not match")
    #         return redirect('register')
        
    #     if  User.objects.get(password=cpassword):
    #         user = User.objects.get(password=cpassword)
    #         if user:
    #             user.password=password1
    #             user.save  
    #             messages.success(request,"Passwords reset succesful")
    #         else:
    #             messages.error(request,"Wrong Password")
                      
    # return render(request, 'reset.html', context)


def resetfunc(request):
    update = PasswordChangeForm(request.user)
    if request.method == 'POST':
        update = PasswordChangeForm(request.user, request.POST)
        if update.is_valid():
            user=update.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password update successful!')
            return redirect('home')
        else:
            messages.error(request, update.errors)
            return redirect('home')

    return render(request, 'homepage.html')


def demologin(request):  
    if request.method =='POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=email,password=password)
        if user:
            login(request, user)
            
            # check if the free trial expired
            username = User.objects.get(username=request.user)
            demouser = DemoUser.objects.get(username=username)
            date_joined = DemoUser.objects.get(date_joined=demouser)
            
            expired = date_joined + 3
            
            today= timezone.localtime(timezone.now())
            expired = today > expired
            if expired:
                demouser = DemoUser.objects.get(user=request.user)
                demouser.delete()
                messages.success(request, 'Free Trial Expired, Kindly subscribe')
                return redirect('demo')
            else:
                messages.success(request, 'Free trial session logged in')
                return redirect('home')

        else:
            # messages.warning(request, 'username/password incorrect')
            return redirect('signin')
    return render (request, 'demo.html')

def profile(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    
    context={
        'profile':profile, 
    }    
    return render(request, 'profile.html', context)




def passwordupdate(request):
    user_profile = ProfileDetail.objects.get(username__username=request.user.username)
    passwform = PasswordForm(request.user)
    if request.method == 'POST':
        passwform = PasswordForm(request.user, request.POST)
        if passwform.is_valid():
            user = passwform.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Profile update successful')
            return redirect('profile')
        else:
            messages.error(request, passwform.errors)
            return redirect('passwordupdate')
    
    context = {
        'user_profile':user_profile,
        'passwform':passwform,
    }
    return render(request, 'passwordupdate.html', context)
    # return redirect('home')

    
def uploadprofile(request):
    user_profile = ProfileDetail.objects.get(username__username=request.user.username)
    pixform = ProfileForm(instance = request.user.profiledata)
    if request.method == 'POST':
        pixform = ProfileForm(request.POST, request.FILES, instance = request.user.profiledata)
        if pixform.is_valid():
            pixform.save()
            messages.success(request, 'Profile update successful')
            return redirect('profile')
        else:
            messages.error(request, pixform.errors)
            return redirect('profile')
    
    context = {
        'user_profile':user_profile,
        'pixform':pixform,
    }
    return render(request, 'profile.html', context)
    # return redirect('home')

    
# =================TEMPLATES==================

def replace(source, replacements):
    finder = re.compile("|".join(re.escape(k) for k in replacements.keys())) # matches every string we want replaced
    result = []
    pos = 0
    while True:
        match = finder.search(source, pos)
        if match:
            # cut off the part up until match
            result.append(source[pos : match.start()])
            # cut off the matched part and replace it in place
            result.append(replacements[source[match.start() : match.end()]])
            pos = match.end()
        else:
            # the rest after the last match
            result.append(source[pos:])
            break
    return "".join(filter(lambda x: x if x is not None else '', result))
    # return "".join(result)


def agreementcntxt(request):
    form = TemplateForm()
    if request.method == "POST":
        body = request.POST['admintemp']
        category = request.POST['category']
        title = request.POST['title']
        form = TemplateForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            new.save()
            
            question1ans= new.question1ans
            question2ans= new.question2ans
            question3ans= new.question3ans
            question4ans= new.question4ans
            question5ans= new.question5ans
            question6ans= new.question6ans
            question7ans= new.question7ans
            question8ans= new.question8ans
            question9ans= new.question9ans
            question10ans= new.question10ans
            question11ans= new.question11ans
            question12ans= new.question12ans
            question13ans= new.question13ans
            question14ans= new.question14ans
            question15ans= new.question15ans
            question16ans= new.question16ans
            question17ans= new.question17ans
            question18ans= new.question18ans
            question19ans= new.question19ans
            question20ans= new.question20ans
            question21ans= new.question21ans
            question22ans= new.question22ans
            question23ans= new.question23ans
            question24ans= new.question24ans
            question25ans= new.question25ans
            question26ans= new.question26ans
            question27ans= new.question27ans
            question28ans= new.question28ans
            question29ans= new.question29ans
            question30ans= new.question30ans
            question31ans= new.question31ans
            question32ans= new.question32ans
            question33ans= new.question33ans
            question34ans= new.question34ans
            question35ans= new.question35ans
            question36ans= new.question36ans
            question37ans= new.question37ans
            question38ans= new.question38ans
            question39ans= new.question39ans
            question40ans= new.question40ans            
            alternate1ans= new.alternate1ans
            alternate2ans= new.alternate2ans
            alternate3ans= new.alternate3ans
            alternate4ans= new.alternate4ans
            alternate5ans= new.alternate5ans
            date1ans = str(new.date1ans)
            date2ans = str(new.date2ans)
            clauseans= new.clauseans
            
            allkeys = ["{Q1}","{Q2}","{Q3}", "{Q4}", "{Q5}","{Q6}", "{Q7}","{Q8}","{Q9}","{Q10}","{Q11}","{Q12}","{Q13}","{Q14}", "{Q15}","{Q16}", "{Q17}", "{Q18}", "{Q19}","{Q20}","{Q21}","{Q22}","{Q23}", "{Q24}", "{Q25}","{Q26}", "{Q27}","{Q28}","{Q29}","{Q30}","{Q31}","{Q32}","{Q33}","{Q34}", "{Q35}","{Q36}", "{Q37}", "{Q38}", "{Q39}","{Q40}","{ALT1}","{ALT2}","{ALT3}","{ALT4}","{ALT5}","{D1}","{D2}","{CLS}"]
            answers = [(question1ans),(question2ans), (question3ans), (question4ans), (question5ans),(question6ans),(question7ans), (question8ans), (question9ans), (question10ans),(question11ans),(question12ans), (question13ans), (question14ans), (question15ans),(question16ans),(question17ans), (question18ans), (question19ans), (question20ans),(question21ans),(question22ans), (question23ans), (question24ans), (question25ans),(question26ans),(question27ans), (question28ans), (question29ans), (question30ans),(question31ans),(question32ans), (question33ans), (question34ans), (question35ans),(question36ans),(question37ans), (question38ans), (question39ans), (question40ans),(alternate1ans),(alternate2ans),(alternate3ans),(alternate4ans),(alternate5ans),(date1ans),(date2ans),(clauseans)]
            replacements = {key: value for key, value in zip(allkeys, answers)}
            body = (str(replace(body, replacements)))
            
            genform = Generatedtemplate(admintclient = new)
            genform.body = body
            genform.category = category
            genform.title = title
            genform.save()
            messages.success(request, 'Template saved')
            return redirect('gentemp')
        else:
            messages.error(request, form.errors)
            return redirect('admintemp')
    return render(request, 'admintemp.html')



 
    
# =================MY TEMPLATES==================
def newtempeditor(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    form = MyTemplateForm()
    
    if request.method == "POST":
        form = MyTemplateForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            body = new.body
            title = new.title
            category = new.category
            
            
            request.session['body'] = body
            request.session['title'] = title
            request.session['category'] = category
            
            return redirect('mytemplate')
        else:
            messages.error(request, form.errors)
            return redirect('editor')
    context={
        'profile':profile, 
    }  
    return render(request, 'editor.html', context)

def mytemplate(request):
    profile = ProfileDetail.objects.get(username__username= request.user.username)
    form = MyTemplateForm()
    if request.method == "POST":
        form = MyTemplateForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            if request.session['category']:
                new.category = request.session['category'].lower()
            else:
                new.category = 'Others'
            category,_ = ClientCategory.objects.get_or_create( temp_class=new.category)
            new.clientcategory = category
            if request.session['title']:
                new.title= request.session['title'].lower()
            else:
                new.title = 'Untitled'            
            new.save() 
            del request.session['body']
            del request.session['title']
            del request.session['category']
            messages.success(request, 'Template saved')
            return redirect('clienttemp')
        else:
            messages.error(request, form.errors)
            return redirect('mytemplate')
        
    # context['body']= request.session['body']
    context={
        'profile': profile,
    }
        

    return render(request, 'mytemplate.html', context) 
        
    # return render(request, 'mytemplate.html',{'category':category, 'profile':profile})   



def clientquestion (request,id):
    mytemplate = ClientTemplates.objects.get(pk=id)

    context={
        'mytemplate': mytemplate,
        
    }
    return render(request, 'clientquestion.html', context)



def useragreementcntxt(request):
    form = MyTemplateForm()
    if request.method == "POST":
        form = MyTemplateForm(request.POST)
        tempid = request.POST['tempid']
        print (tempid)
        mytemplate = ClientTemplates.objects.get(pk=tempid)
        if form.is_valid():
            new = form.save(commit=False)
            
            body= new.body
            date1 = str(new.date1ans)
            date2 = str(new.date2ans)            
            question1= new.question1ans
            question2= new.question2ans
            question3= new.question3ans
            question4= new.question4ans
            question5= new.question5ans
            question6= new.question6ans
            question7= new.question7ans
            question8= new.question8ans
            question9= new.question9ans
            question10= new.question10ans
            question11= new.question11ans
            question12= new.question12ans
            question13= new.question13ans
            question14= new.question14ans
            question15= new.question15ans
            question16= new.question16ans
            question17= new.question17ans
            question18= new.question18ans
            question19= new.question19ans
            question20= new.question20ans
            question21= new.question21ans
            question22= new.question22ans
            question23= new.question23ans
            question24= new.question24ans
            question25= new.question25ans
            question26= new.question26ans
            question27= new.question27ans
            question28= new.question28ans
            question29= new.question29ans
            question30= new.question30ans
            question31= new.question31ans
            question32= new.question32ans
            question33= new.question33ans
            question34= new.question34ans
            question35= new.question35ans
            question36= new.question36ans
            question37= new.question37ans
            question38= new.question38ans
            question39= new.question39ans
            question40= new.question40ans            

            allkeys = ["{Q1}","{Q2}","{Q3}", "{Q4}", "{Q5}","{Q6}", "{Q7}","{Q8}","{Q9}","{Q10}","{Q11}","{Q12}","{Q13}","{Q14}", "{Q15}","{Q16}", "{Q17}", "{Q18}", "{Q19}","{Q20}","{Q21}","{Q22}","{Q23}", "{Q24}", "{Q25}","{Q26}", "{Q27}","{Q28}","{Q29}","{Q30}","{Q31}","{Q32}","{Q33}","{Q34}", "{Q35}","{Q36}", "{Q37}", "{Q38}", "{Q39}","{Q40}","{D1}","{D2}"]
            answers = [(question1),(question2), (question3), (question4), (question5),(question6),(question7), (question8), (question9), (question10),(question11),(question12), (question13), (question14), (question15),(question16),(question17), (question18), (question19), (question20),(question21),(question22), (question23), (question24), (question25),(question26),(question27), (question28), (question29), (question30),(question31),(question32), (question33), (question34), (question35),(question36),(question37), (question38), (question39), (question40),(date1),(date2)]
            replacements = {key: value for key, value in zip(allkeys, answers)}
            body = (str(replace(body, replacements)))
            genform = Generatedmytemplate(body = new)
            genform.user = request.user
            genform.body = body
            genform.title = mytemplate.title
            genform.category = mytemplate.category
            genform.save()
            messages.success(request, 'Template saved')
            return redirect('gentemp')
        else:
            messages.error(request, form.errors)
            return redirect('admintemp')
    return render(request, 'admintemp.html')

# =============================

# ================================================
def uploadpdffile(request):
    user_profile = ProfileDetail.objects.get(username__username=request.user.username)
    if request.method == 'POST':
        # pdfform = MypdfsForm(request.POST)
        pdf = request.FILES.get('image_upload')
        
        if pdfform.is_valid():
            new = pdfform.save(commit=False)
            new.user = request.user
            # new.pdf = file
            new.date_created = timezone.localtime(timezone.now())
            new.save()
            messages.success(request, 'PDF FILE UPLOADED successful')
            return redirect('pdfmanager')
        else:
            messages.error(request, pdfform.errors)
            return redirect('home')
    
    context = {
        'user_profile':user_profile,
        'pdfform':pdfform,
    }
    return render(request, 'home.html', context)

def uploaddocfile(request):
    user_profile = ProfileDetail.objects.get(username__username=request.user.username)
    if request.method == 'POST':
        pdfform = MyDocForm(request.POST)
        if pdfform.is_valid():
            pdfform.save()
            messages.success(request, 'wORD FILE UPLOADED successful')
            return redirect('docmanager')
        else:
            messages.error(request, pdfform.errors)
            return redirect('docmanager')
    
    context = {
        'user_profile':user_profile,
        'pdfform':pdfform,
    }
    return render(request, 'home.html', context)
# ================================================















 
        
# def uploadtemplate(request):
#     if request.method == 'POST':
#         # categoryname = request.POST['categoryname']
#         file = request.FILES.get('filename')
#         a = MyTemplate(file=file, profile=request.user)
#         a.save()
#         messages.success(request, 'Files Submitted successfully!')
#         return redirect('home')
#     else:
#     	messages.error(request, 'Files was not Submitted successfully!')
#         # return redirect('home')

# # def deleteadminfile(request):
# #     url = request.META.get('HTTP_REFERER')
# #     if request.method == 'POST':
# #         delfile = request.POST['aditemid']
# #         AdminTemp.objects.filter(pk=delfile).delete()
# #         return redirect(url)


# def deletefile(request):
#     url = request.META.get('HTTP_REFERER')
#     if request.method == 'POST':
#         delfile = request.POST['itemid']
#         MyTemplate.objects.get(pk=delfile).delete()
#     return redirect(url)




# def password_reset_request(request):
# 	if request.method == "POST":
# 		password_reset_form = PasswordResetForm(request.POST)
# 		if password_reset_form.is_valid():
# 			data = password_reset_form.cleaned_data['email']
# 			associated_users = User.objects.filter(Q(email=data))
# 			if associated_users.exists():
# 				for user in associated_users:
# 					subject = "Password Reset Requested"
# 					email_template_name = "password/password_reset_email.txt"
# 					c = {
# 					"email":user.email,
# 					'domain':'44.204.229.238',
# 					'site_name': 'Refill',
# 					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
# 					"user": user,
# 					'token': default_token_generator.make_token(user),
# 					'protocol': 'http',
# 					}
# 					email = render_to_string(email_template_name, c)
# 					try:
# 						send_mail(subject, email, settings.EMAIL_HOST_USER, [data], fail_silently=False)
# 					except BadHeaderError:
# 						return HttpResponse('Invalid header found.')
# 					return redirect ("password_reset/done/")
# 	password_reset_form = PasswordResetForm()
# 	return render(request=request, template_name="password/password_reset.html", context={
#         "password_reset_form":password_reset_form
#         })



# def get_access_code(request):
    
#     base_url = "https://account-d.docusign.com/oath/auth"
#     auth_url = "{0}?response_type=code&scope=signature&client_id={1}&redirect_url={2}".format(base_url,
#         CLIENT_AUTH_ID, request.build_absolute_url(reverse('auth_login')))
#     return HttpResponseRedirect(auth_url)

# def auth_login(request):
#     base_url = 'https://account-d.docusign.com/oauth/token'
#     auth_code_string = '{0}:{1}'.format(CLIENT_AUTH_ID, CLIENT_SECRET_KEY)
#     auth_token = base64.b64encode(auth_code_string.encode())
    
#     req_headers = {"Authorization": "Basic{0}".format(auth_token.decode('utf-8'))}
#     post_data = {'grant_type': 'authorization_code', 'code': request.GET.get('code')}
#     r = requests.post(base_url, data=post_data, header=req_headers)
    
#     response = r.json()
#     return HttpResponse(response['access_token'])
    
#     if not 'error' in response:
#         return HttpResponse(response['error'])
    
# def embedded_signing_ceremony(request):
#     signer_email = 'fakoredeabbas@gmail.com'
#     signer_name = ' Fakorede Abbas'
    
#     with open (os.path.join(BASE_DIR, 'static/', 'esign-document.pdf'), "rb") as file:
#         content_bytes = file.read()
#     base64_file_content = based64.b64encode(content_bytes).decode('ascii')
    
#     document= Document(
#         document_based64 = base64_file_content,
#         name= 'Example document',
#         file_extension = 'pdf',
#         document_id= 1
#     )
    
#     signer = Signer(
#         email = signer_email, name= signer_name, recipient_id="1", routing_order="1",
#         client_user_id = client_user_id,
#     )

#     sign_here = SignHere(
#         document_id = '1', page_number = '1', recipient_id ='1', tab_label='SignHereTab',
#         x_position='195', y_position= '147')

#     signer.tabs(sign_here_tabs=[sign_here])
    
#     envelope_definition = EnvelopeDefinition(
#         email_subject= "Please sign this document sent from the python SDK",
#         documents=[document],
#         recipients= Recipients(signers=[signer]),
#         status="sent"
#     )
    
#     api_client = ApiClient()
#     api_client.host = base_path
#     api_client.set_default_header("Authorization", "Bearer" + reuest.GET.get('token'))
    
#     envelope_api = EnvelopeApi(api_client)
#     results = envelope_api.create_envelope(account_id, envelope_definition=envelope_definition)

#     envelope_id = results.envelope_id
#     recipient_view_request = RecipientViewRequest(
#         authentication_method = authentication_method, client_user_id=client_user_id,
#         recipient_id = '1', return_url=request.build_absolute_url(reverse('sign_completed')),
#         user_name=signer_name, email= signer_email
#     )
    
#     results = envelope_api.create_recipient_view(account_id, envelope_id,
#                                                  recipient_view_request=recipient_view_request)
    
#     return HttpResponse(results.url)
    
# def sign_complete(request):
    
#     return HttpResponse('Signing Completed Successfully')
    