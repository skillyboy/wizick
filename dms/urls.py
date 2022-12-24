from django.urls import path 
from .views import *


urlpatterns = [
#=================== Home =====================
    path('', index, name='index'),
    path('home', home, name='home'),
    path('dashboard', dashboard, name='dashboard'),
    
    path('saveeditor', saveeditor, name='saveeditor'),
# ================== Auth and Login System======================
    path('signin', signin, name='signin'),
    path('register', register, name='register'),
    path('logoutfunc', logoutfunc, name='logoutfunc'),
    path('reset', reset, name='reset'),
    path('resetfunc', resetfunc, name='resetfunc'),
    path('demo', demo, name='demo'),
    path('demologin', demologin, name='demologin'),
# ================== TEMPLATE ====================================
    path('allmanager', allmanager, name='allmanager'),
    path('docmanager', docmanager, name='docmanager'),
    path('pdfmanager', pdfmanager, name='pdfmanager'),
    path('editormanager', editormanager, name='editormanager'),
    
    path('clause', clause, name='clause'),
    path('tinymce', tinymce, name='tinymce'),
    path('insight', insight, name='insight'),
    path('legal', legal, name='legal'),
    path('editor', editor, name='editor'),
    path('withoutinsight', withoutinsight, name='withoutinsight'),
    path('profile', profile, name='profile'),
    path('uploadprofile', uploadprofile, name='uploadprofile'),
    path('passwordupdate', passwordupdate, name='passwordupdate'),
    
    path('createdocinsight', createdocinsight, name='createdocinsight'),
    path('createdocinsightform', createdocinsightform, name='createdocinsightform'),
    
    path('createpdfinsight', createpdfinsight, name='createpdfinsight'),
    path('createpdfinsightform', createpdfinsightform, name='createpdfinsightform'),
    
    path('createdraftinsight', createdraftinsight, name='createdraftinsight'),
    path('createdraftinsightform', createdraftinsightform, name='createdraftinsightform'),
    
    path('admintemp', admintemp, name='admintemp'),
    path('admintempdetails/<str:id>', admintempdetails, name='admintempdetails'),
    path('clienttemp', clienttemp, name='clienttemp'),
    path('clienttempdetails/<str:id>', clienttempdetails, name='clienttempdetails'),
    path('gentemp', gentemp, name='gentemp'),
    path('gentempdetails/<str:id>', gentempdetails, name='gentempdetails'),
    path('newtempeditor/', newtempeditor, name='newtempeditor'),
    path('templist', templist, name='templist'),
    path('question/<str:id>', question, name='question'),
    
    path('addtemp', addtemp, name='addtemp'),
    path('mytempmanager', mytempmanager, name='mytempmanager'),
    path('mytemplate', mytemplate, name='mytemplate'),
    path('clientquestion/<str:id>', clientquestion, name='clientquestion'),
    path('useragreementcntxt', useragreementcntxt, name='useragreementcntxt'),
    
    
    path('createtempinsight', createtempinsight, name='createtempinsight'),
    path('createtempinsightform', createtempinsightform, name='createtempinsightform'),
    
    path('mygentempdetails/<str:id>', mygentempdetails, name='mygentempdetails'),
    
    path('uploaddocfile', uploaddocfile, name='uploaddocfile'),
    path('uploadpdffile', uploadpdffile, name='uploadpdffile'),
    path('deletepdffile', deletepdffile, name='deletepdffile'),
    
    
    
    
    
    
    
    
    
    
    # path('deletefile', deletefile, name='deletefile'),
    # path('uploadtemplate', uploadtemplate, name='uploadtemplate'),
    
    path('agreementcntxt', agreementcntxt, name='agreementcntxt'),
    path('editormanager', editormanager, name='editormanager'),
    path('notification', notification, name='notification'),

    path('esign/<int:pk>', ProfileDetailListView.as_view(), name='esigning')
    

]
