from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils.text import slugify
from tinymce import models as tinymce_models     

# ===========================================================
                        # User-Auth/Roles System
# ===========================================================        
# class Esign(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     signature = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.signature




class Dash(models.Model):
    name = models.CharField(max_length=150, null=True)
    age = models.PositiveIntegerField()

class Company(models.Model):
    company_name = models.CharField(max_length=150, null=True)
    company_uuid = models.CharField(null=True,blank=True, max_length=100)
    email = models.EmailField(null=True)
    url = models.URLField(null=True)
    
    class Meta:
        db_table = 'company'
        managed = True
        verbose_name = 'company'
        verbose_name_plural = 'company'

    def __str__(self):
        return self.company_name  
    


    
class ProfileDetail(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    company = models.CharField(max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=150, blank=True, null=True)
    date_joined = models.DateTimeField(blank=True, null=True)
    p_img = models.ImageField(upload_to='profile', default='profile/avatar.png', blank=True, null=True)

    class Meta:
        db_table = 'profiledetail'
        managed = True
        verbose_name = 'profileDetail'
        verbose_name_plural = 'profileDetails'

    def __str__(self):
        return self.username.username
    
    
class DemoUser(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    fullname = models.CharField(max_length=150, null=True)
    url = models.URLField(null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=150, null=True)
    date_joined = models.DateTimeField(blank=True, null=True)
    date_expired = models.DateTimeField(blank=True, null=True)
    profile_pic = models.ImageField(default='default.jpg')

    class Meta:
        db_table = 'demouser'
        managed = True
        verbose_name = 'demouser'
        verbose_name_plural = 'demo profiles'

    def __str__(self):
        return self.username.username
# ===========================================================
                        # Content System
# ===========================================================

class FileType(models.Model):
    type = models.CharField(max_length=100)
    
    def __str__(self):
        return self.type
       
class Category(models.Model): 
    temp_class = models.CharField(blank=True, max_length=100)

    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'category'
        verbose_name_plural = 'categories'
           
    def __str__(self):
        return self.temp_class 

class AdminTemp(models.Model): 
    body = tinymce_models.HTMLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    slug= models.SlugField(max_length=500, unique=True, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    # QUESTIONS FROM THE ADMIN
    clause = models.CharField(max_length=200, null='True', blank='True')
    date1 = models.CharField(max_length=200, null='True', blank='True')
    date2 = models.CharField(max_length=200, null='True', blank='True')
    question1 = models.CharField(max_length=200, null='True', blank='True')  
    question2 = models.CharField(max_length=200, null='True', blank='True')
    question3 = models.CharField(max_length=200, null='True', blank='True')
    question4 = models.CharField(max_length=200, null='True', blank='True')
    question5 = models.CharField(max_length=200, null='True', blank='True')
    question6 = models.CharField(max_length=200, null='True', blank='True')  
    question7 = models.CharField(max_length=200, null='True', blank='True')
    question8 = models.CharField(max_length=200, null='True', blank='True')
    question9 = models.CharField(max_length=200, null='True', blank='True')
    question10 = models.CharField(max_length=200, null='True', blank='True') 
    question11 = models.CharField(max_length=200, null='True', blank='True')  
    question12 = models.CharField(max_length=200, null='True', blank='True')
    question13 = models.CharField(max_length=200, null='True', blank='True')
    question14 = models.CharField(max_length=200, null='True', blank='True')
    question15 = models.CharField(max_length=200, null='True', blank='True')
    question16 = models.CharField(max_length=200, null='True', blank='True')  
    question17 = models.CharField(max_length=200, null='True', blank='True')
    question18 = models.CharField(max_length=200, null='True', blank='True')
    question19 = models.CharField(max_length=200, null='True', blank='True')
    question20 = models.CharField(max_length=200, null='True', blank='True') 
    question21 = models.CharField(max_length=200, null='True', blank='True')  
    question22 = models.CharField(max_length=200, null='True', blank='True')
    question23 = models.CharField(max_length=200, null='True', blank='True')
    question24 = models.CharField(max_length=200, null='True', blank='True')
    question25 = models.CharField(max_length=200, null='True', blank='True')
    question26 = models.CharField(max_length=200, null='True', blank='True')  
    question27 = models.CharField(max_length=200, null='True', blank='True')
    question28 = models.CharField(max_length=200, null='True', blank='True')
    question29 = models.CharField(max_length=200, null='True', blank='True')
    question30 = models.CharField(max_length=200, null='True', blank='True')    
    question31 = models.CharField(max_length=200, null='True', blank='True')  
    question32 = models.CharField(max_length=200, null='True', blank='True')
    question33 = models.CharField(max_length=200, null='True', blank='True')
    question34 = models.CharField(max_length=200, null='True', blank='True')
    question35 = models.CharField(max_length=200, null='True', blank='True')
    question36 = models.CharField(max_length=200, null='True', blank='True')  
    question37 = models.CharField(max_length=200, null='True', blank='True')
    question38 = models.CharField(max_length=200, null='True', blank='True')
    question39 = models.CharField(max_length=200, null='True', blank='True')
    question40 = models.CharField(max_length=200, null='True', blank='True')    
    alternate1 = models.TextField(max_length=200, null='True', blank='True')
    alternate1optionA = models.CharField(max_length=200, null='True', blank='True')
    alternate1optionB = models.CharField(max_length=200, null='True', blank='True')
    alternate1optionC = models.CharField(max_length=200, null='True', blank='True')
    alternate1optionD = models.CharField(max_length=200, null='True', blank='True')
    alternate1optionE = models.CharField(max_length=200, null='True', blank='True') 
    alternate1optionF = models.CharField(max_length=200, null='True', blank='True')    
       
    alternate2 = models.TextField(max_length=200, null='True', blank='True')
    alternate2optionA = models.CharField(max_length=200, null='True', blank='True')
    alternate2optionB = models.CharField(max_length=200, null='True', blank='True')
    alternate2optionC = models.CharField(max_length=200, null='True', blank='True')
    alternate2optionD = models.CharField(max_length=200, null='True', blank='True')
    alternate2optionE = models.CharField(max_length=200, null='True', blank='True')
    alternate3 = models.TextField(max_length=200, null='True', blank='True')
    alternate3optionA = models.CharField(max_length=200, null='True', blank='True')
    alternate3optionB = models.CharField(max_length=200, null='True', blank='True')
    alternate3optionC = models.CharField(max_length=200, null='True', blank='True')
    alternate3optionD = models.CharField(max_length=200, null='True', blank='True')
    alternate3optionE = models.CharField(max_length=200, null='True', blank='True')
    alternate4 = models.TextField(max_length=200, null='True', blank='True')
    alternate4optionA = models.CharField(max_length=200, null='True', blank='True')
    alternate4optionB = models.CharField(max_length=200, null='True', blank='True')
    alternate4optionC = models.CharField(max_length=200, null='True', blank='True')
    alternate4optionD = models.CharField(max_length=200, null='True', blank='True')
    alternate4optionE = models.CharField(max_length=200, null='True', blank='True')
    alternate5 = models.TextField(max_length=200, null='True', blank='True')
    alternate5optionA = models.CharField(max_length=200, null='True', blank='True')
    alternate5optionB = models.CharField(max_length=200, null='True', blank='True')
    alternate5optionC = models.CharField(max_length=200, null='True', blank='True')
    alternate5optionD = models.CharField(max_length=200, null='True', blank='True')
    alternate5optionE = models.CharField(max_length=200, null='True', blank='True')
    # utility Variable
    # uniqueId = models.BigAutoField(primary_key=True, unique=True)
    
    def __str__(self):
        return self.category.temp_class
    
    class Meta:
        db_table = 'Admin template'
        managed = True
        verbose_name = 'Admin template'
        verbose_name_plural = 'Admin templates'    


##=========== TEMPLATE ATTRIBUTES========================##
class AdminTempClient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now=True)
    admintemp = models.TextField()
    date1ans = models.DateField(max_length=200, null='True', blank='True')    
    date2ans = models.DateField(max_length=200, null='True', blank='True')    
    clauseans = models.CharField(max_length=200, null='True', blank='True', default='add clause?')
    question1ans = models.CharField(max_length=200, null='True', blank='True')  
    question2ans = models.CharField(max_length=200, null='True', blank='True')
    question3ans = models.CharField(max_length=200, null='True', blank='True')
    question4ans = models.CharField(max_length=200, null='True', blank='True')
    question5ans = models.CharField(max_length=200, null='True', blank='True')
    question6ans = models.CharField(max_length=200, null='True', blank='True')  
    question7ans = models.CharField(max_length=200, null='True', blank='True')
    question8ans = models.CharField(max_length=200, null='True', blank='True')
    question9ans = models.CharField(max_length=200, null='True', blank='True')
    question10ans = models.CharField(max_length=200, null='True', blank='True') 
    question11ans = models.CharField(max_length=200, null='True', blank='True')  
    question12ans = models.CharField(max_length=200, null='True', blank='True')
    question13ans = models.CharField(max_length=200, null='True', blank='True')
    question14ans = models.CharField(max_length=200, null='True', blank='True')
    question15ans = models.CharField(max_length=200, null='True', blank='True')
    question16ans = models.CharField(max_length=200, null='True', blank='True')  
    question17ans = models.CharField(max_length=200, null='True', blank='True')
    question18ans = models.CharField(max_length=200, null='True', blank='True')
    question19ans = models.CharField(max_length=200, null='True', blank='True')
    question20ans = models.CharField(max_length=200, null='True', blank='True')    
    question21ans = models.CharField(max_length=200, null='True', blank='True')  
    question22ans = models.CharField(max_length=200, null='True', blank='True')
    question23ans = models.CharField(max_length=200, null='True', blank='True')
    question24ans = models.CharField(max_length=200, null='True', blank='True')
    question25ans = models.CharField(max_length=200, null='True', blank='True')
    question26ans = models.CharField(max_length=200, null='True', blank='True')  
    question27ans = models.CharField(max_length=200, null='True', blank='True')
    question28ans = models.CharField(max_length=200, null='True', blank='True')
    question29ans = models.CharField(max_length=200, null='True', blank='True')
    question30ans = models.CharField(max_length=200, null='True', blank='True')    
    question31ans = models.CharField(max_length=200, null='True', blank='True')  
    question32ans = models.CharField(max_length=200, null='True', blank='True')
    question33ans = models.CharField(max_length=200, null='True', blank='True')
    question34ans = models.CharField(max_length=200, null='True', blank='True')
    question35ans = models.CharField(max_length=200, null='True', blank='True')
    question36ans = models.CharField(max_length=200, null='True', blank='True')  
    question37ans = models.CharField(max_length=200, null='True', blank='True')
    question38ans = models.CharField(max_length=200, null='True', blank='True')
    question39ans = models.CharField(max_length=200, null='True', blank='True')
    question40ans = models.CharField(max_length=200, null='True', blank='True')    
    alternate1ans = models.TextField(max_length=200, null='True', blank='True')
    alternate2ans = models.TextField(max_length=200, null='True', blank='True')
    alternate3ans = models.TextField(max_length=200, null='True', blank='True')    
    alternate4ans = models.CharField(max_length=200, null='True', blank='True')
    alternate5ans = models.CharField(max_length=200, null='True', blank='True')
  
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify('{}'.format(self.admintemp.title))
        super(AdminTempClient, self).save(*args, **kwargs)  
        
    class Meta:
        db_table = 'AdminTemp Client'
        managed = True
        verbose_name = 'AdminTempClient'
        verbose_name_plural = 'AdminTempClient'  


       
class Generatedtemplate(models.Model):
    body = tinymce_models.HTMLField(null=True)
    admintclient = models.ForeignKey(AdminTempClient, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200,blank=True, null=True,)
      
    # utility Variable
    date_created = models.DateField(auto_now_add=True)
             
    def __str__(self):
        return self.category
        
    class Meta:
        db_table = 'Generated Template'
        managed = True
        verbose_name = 'Generated Template'
        verbose_name_plural = 'Generated Templates'             


class Generatedmytemplate(models.Model):
    body = tinymce_models.HTMLField(null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200,blank=True, null=True,)
      
    # utility Variable
    date_created = models.DateField(auto_now_add=True)
             
    def __str__(self):
        return self.body
        
    class Meta:
        db_table = 'Generated my Template'
        managed = True
        verbose_name = 'Generated my Template'
        verbose_name_plural = 'Generated my Templates'       
        
              

class Myeditor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, default='New Document')
    body = models.CharField(max_length=100, null=True)
    parties = models.CharField(max_length=100, blank=True, null=True)
    term = models.CharField(max_length=1000, blank=True, null=True)
    liabilitycap = models.CharField(max_length=1000, blank=True, null=True)
    consideration = models.CharField(max_length=1000, blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    effectivedate = models.DateField(max_length=1000,blank=True, null=True)
    expirydate = models.DateField(max_length=1000,blank=True, null=True)
    status = models.CharField(max_length=100, null=True, default='TO DO')
    comment = models.TextField(max_length=255, blank=True, null=True )

    def __str__(self):
        return self.title

# # =======================UPLOADED DOCUMENT======================           

class Mypdfs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True, default='New Document')
    pdf = models.FileField(upload_to='user_uploads/pdf/', blank=False, null=False )
    # type = models.ForeignKey(FileType, on_delete=models.CASCADE, null=True)
    parties = models.CharField(max_length=100, blank=True, null=True)
    term = models.CharField(max_length=1000, blank=True, null=True)
    liabilitycap = models.CharField(max_length=1000, blank=True, null=True)
    consideration = models.CharField(max_length=1000, blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    effectivedate = models.DateField(max_length=1000,blank=True, null=True)
    expirydate = models.DateField(max_length=1000,blank=True, null=True)
    status = models.CharField(max_length=100, null=True, blank='True')
    comment = models.TextField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class MyDocs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True, default='New Document')
    doc = models.FileField(upload_to='user_uploads/docx/' , blank=True, null=True)
    type = models.ForeignKey(FileType, on_delete=models.CASCADE, null=True)
    parties = models.CharField(max_length=100, blank=True, null=True)
    term = models.CharField(max_length=1000, blank=True, null=True)
    liabilitycap = models.CharField(max_length=1000, blank=True, null=True)
    consideration = models.CharField(max_length=1000, blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    effectivedate = models.DateField(max_length=1000,blank=True, null=True)
    expirydate = models.DateField(max_length=1000,blank=True, null=True)
    status = models.CharField(max_length=100,blank=True, null=True)
    comment = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title 
    
# ===========================================================
class ClauseLib(models.Model): 
    name = models.CharField(blank=True, max_length=500) 
    title = models.CharField(blank=True, max_length=500)  
    clause = models.CharField(blank=True, max_length=500)
    def __str__(self):
        return self.title
    
class Terminology(models.Model): 
    title = models.CharField(blank=True, max_length=100)
    body = models.TextField(blank=True, max_length=1000)
    def __str__(self):
        return self.title
  
    
class Notification(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Notification'
        managed = True
        verbose_name = 'Notification'
        verbose_name_plural = 'Notification'

    def __str__(self):
        return self.title
   
# class Notification(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     # navigate_url = models.CharField(max_length=300, default="/")
#     viewed = models.BooleanField(default=False)
#     title = models.CharField(max_length=50,default="title")
#     message = models.CharField(max_length=100,default="message")
#     # time = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title
   
   
class ClientCategory(models.Model): 
    temp_class = models.CharField(blank=True, max_length=100)

    class Meta:
        db_table = 'clientcategory'
        managed = True
        verbose_name = 'clientcategory'
        verbose_name_plural = 'clientcategories'
           
    def __str__(self):
        return self.temp_class   
   
class ClientTemplates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True)
    question1 = models.CharField(max_length=200, null='True', blank='True')  
    question2 = models.CharField(max_length=200, null='True', blank='True')
    question3 = models.CharField(max_length=200, null='True', blank='True')
    question4 = models.CharField(max_length=200, null='True', blank='True')
    question5 = models.CharField(max_length=200, null='True', blank='True')
    question6 = models.CharField(max_length=200, null='True', blank='True')  
    question7 = models.CharField(max_length=200, null='True', blank='True')
    question8 = models.CharField(max_length=200, null='True', blank='True')
    question9 = models.CharField(max_length=200, null='True', blank='True')
    question10 = models.CharField(max_length=200, null='True', blank='True') 
    question11 = models.CharField(max_length=200, null='True', blank='True')  
    question12 = models.CharField(max_length=200, null='True', blank='True')
    question13 = models.CharField(max_length=200, null='True', blank='True')
    question14 = models.CharField(max_length=200, null='True', blank='True')
    question15 = models.CharField(max_length=200, null='True', blank='True')
    question16 = models.CharField(max_length=200, null='True', blank='True')  
    question17 = models.CharField(max_length=200, null='True', blank='True')
    question18 = models.CharField(max_length=200, null='True', blank='True')
    question19 = models.CharField(max_length=200, null='True', blank='True')
    question20 = models.CharField(max_length=200, null='True', blank='True')    
    question21 = models.CharField(max_length=200, null='True', blank='True')  
    question22 = models.CharField(max_length=200, null='True', blank='True')
    question23 = models.CharField(max_length=200, null='True', blank='True')
    question24 = models.CharField(max_length=200, null='True', blank='True')
    question25 = models.CharField(max_length=200, null='True', blank='True')
    question26 = models.CharField(max_length=200, null='True', blank='True')  
    question27 = models.CharField(max_length=200, null='True', blank='True')
    question28 = models.CharField(max_length=200, null='True', blank='True')
    question29 = models.CharField(max_length=200, null='True', blank='True')
    question30 = models.CharField(max_length=200, null='True', blank='True')    
    question31 = models.CharField(max_length=200, null='True', blank='True')  
    question32 = models.CharField(max_length=200, null='True', blank='True')
    question33 = models.CharField(max_length=200, null='True', blank='True')
    question34 = models.CharField(max_length=200, null='True', blank='True')
    question35 = models.CharField(max_length=200, null='True', blank='True')
    question36 = models.CharField(max_length=200, null='True', blank='True')  
    question37 = models.CharField(max_length=200, null='True', blank='True')
    question38 = models.CharField(max_length=200, null='True', blank='True')
    question39 = models.CharField(max_length=200, null='True', blank='True')
    question40 = models.CharField(max_length=200, null='True', blank='True')  
    date1 = models.CharField(max_length=200, null='True', blank='True')    
    date2 = models.CharField(max_length=200, null='True', blank='True')    
    
    question1ans = models.CharField(max_length=200, null='True', blank='True')  
    question2ans = models.CharField(max_length=200, null='True', blank='True')
    question3ans = models.CharField(max_length=200, null='True', blank='True')
    question4ans = models.CharField(max_length=200, null='True', blank='True')
    question5ans = models.CharField(max_length=200, null='True', blank='True')
    question6ans = models.CharField(max_length=200, null='True', blank='True')  
    question7ans = models.CharField(max_length=200, null='True', blank='True')
    question8ans = models.CharField(max_length=200, null='True', blank='True')
    question9ans = models.CharField(max_length=200, null='True', blank='True')
    question10ans = models.CharField(max_length=200, null='True', blank='True') 
    question11ans = models.CharField(max_length=200, null='True', blank='True')  
    question12ans = models.CharField(max_length=200, null='True', blank='True')
    question13ans = models.CharField(max_length=200, null='True', blank='True')
    question14ans = models.CharField(max_length=200, null='True', blank='True')
    question15ans = models.CharField(max_length=200, null='True', blank='True')
    question16ans = models.CharField(max_length=200, null='True', blank='True')  
    question17ans = models.CharField(max_length=200, null='True', blank='True')
    question18ans = models.CharField(max_length=200, null='True', blank='True')
    question19ans = models.CharField(max_length=200, null='True', blank='True')
    question20ans = models.CharField(max_length=200, null='True', blank='True')    
    question21ans = models.CharField(max_length=200, null='True', blank='True')  
    question22ans = models.CharField(max_length=200, null='True', blank='True')
    question23ans = models.CharField(max_length=200, null='True', blank='True')
    question24ans = models.CharField(max_length=200, null='True', blank='True')
    question25ans = models.CharField(max_length=200, null='True', blank='True')
    question26ans = models.CharField(max_length=200, null='True', blank='True')  
    question27ans = models.CharField(max_length=200, null='True', blank='True')
    question28ans = models.CharField(max_length=200, null='True', blank='True')
    question29ans = models.CharField(max_length=200, null='True', blank='True')
    question30ans = models.CharField(max_length=200, null='True', blank='True')    
    question31ans = models.CharField(max_length=200, null='True', blank='True')  
    question32ans = models.CharField(max_length=200, null='True', blank='True')
    question33ans = models.CharField(max_length=200, null='True', blank='True')
    question34ans = models.CharField(max_length=200, null='True', blank='True')
    question35ans = models.CharField(max_length=200, null='True', blank='True')
    question36ans = models.CharField(max_length=200, null='True', blank='True')  
    question37ans = models.CharField(max_length=200, null='True', blank='True')
    question38ans = models.CharField(max_length=200, null='True', blank='True')
    question39ans = models.CharField(max_length=200, null='True', blank='True')
    question40ans = models.CharField(max_length=200, null='True', blank='True')      
    date1ans = models.DateField(max_length=200, null='True', blank='True')    
    date2ans = models.DateField(max_length=200, null='True', blank='True')    
    category = models.CharField(max_length=150, null=True, blank=True)
    clientcategory = models.ForeignKey(ClientCategory, on_delete=models.CASCADE, null=True , blank= True ) 
    title = models.CharField(max_length=150, null=True, blank=True)
    date_created = models.DateField(auto_now=True)
    type = models.ForeignKey(FileType, on_delete=models.CASCADE, null=True)
    parties = models.CharField(max_length=100, blank=True, null=True)
    term = models.CharField(max_length=1000, blank=True, null=True)
    liabilitycap = models.CharField(max_length=1000, blank=True, null=True)
    consideration = models.CharField(max_length=1000, blank=True, null=True)
    effectivedate = models.CharField(max_length=1000,blank=True, null=True)
    effectivedate = models.CharField(max_length=1000,blank=True, null=True)
    expirydate = models.CharField(max_length=1000,blank=True, null=True)
    comment = models.TextField(max_length=255, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True )

    class Meta:
        db_table = 'ClientTemplate'
        managed = True
        verbose_name = 'ClientTemplate'
        verbose_name_plural = 'ClientTemplates'

    def __str__(self):
        return self.body
    
