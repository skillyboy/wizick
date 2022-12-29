from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Esign)     
class EsignAdmin(admin.ModelAdmin):
    list_display = ('user','signature') 


@admin.register(ProfileDetail)     
class ProfileDetailAdmin(admin.ModelAdmin):
    list_display = ('username','url','company','email','phone','date_joined','p_img')
 
@admin.register(Category)     
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','temp_class')
 

@admin.register(ClientCategory)     
class ClientCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','temp_class')
        

@admin.register(AdminTemp)   
class AdminTempAdmin(admin.ModelAdmin):
    list_display = ('id','category','title','clause','slug','date_created','question1','last_updated')
    prepopulated_fields =  {'slug': ('title',)}
    # class Media:
    #     js= ('js/admintiny.js',)
        
@admin.register(Generatedtemplate)   
class GeneratedtemplateAdmin(admin.ModelAdmin):
    list_display = ('admintclient','body','title','date_created')
    # prepopulated_fields =  {'slug': ('title',)}

@admin.register(Generatedmytemplate)   
class GeneratedmytemplateAdmin(admin.ModelAdmin):
    list_display = ('body','title','category','date_created')
    # prepopulated_fields =  {'slug': ('title',)}
    

@admin.register(Myeditor)     
class MyeditorAdmin(admin.ModelAdmin):
    list_display = ('title','body','date_created','term')
    
    

@admin.register(Mypdfs)
class MypdfsAdmin(admin.ModelAdmin):
    list_display = ('user','title','pdf','parties','term','liabilitycap','consideration','effectivedate','expirydate','status','comment')

@admin.register(MyDocs)   
class MyDocsAdmin(admin.ModelAdmin):
    list_display = ('user','title','doc','type','parties','term','liabilitycap','consideration','effectivedate','expirydate','status','comment')
# =============================
@admin.register(ClauseLib) 
class ClauseLibAdmin(admin.ModelAdmin):
    list_display = ('name','title','clause')

@admin.register(Terminology) 
class TerminologyAdmin(admin.ModelAdmin):
    list_display = ('title','body')

# @admin.register(Notification) 
# class NotificationAdmin(admin.ModelAdmin):
#     list_display = ('user','viewed','title','message')


    
# @admin.register(ClientTemplates) 
# class ClientTemplatesAdmin(admin.ModelAdmin):
#     list_display = ('clientcategory','category','user','body','question1','question2','question3','question4','question5','question6','question7','question8','title','question9','question10','date_created')
