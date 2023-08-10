from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,AbstractUser

class UserManager(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    first_connexion = models.BooleanField(default=True)
    profil = models.OneToOneField("backlab.Profil", verbose_name=("user_profil"), on_delete=models.CASCADE, default=1)
    date_joined=  models.DateTimeField(auto_now=True,blank=True, null=True)
    username = None 
    last_name = None
    is_staff= None
    is_superuser= None
    
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['first_name' , 'is_active' ,'date_joined' , 'profil']
    
class Profil(models.Model):
    profil_id = models.AutoField(primary_key=True)
    profil_libelle = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class article(models.Model):
    article_id=models.AutoField(primary_key=True)
    article_text=models.TextField()
    editeur=models.ForeignKey("backlab.UserManager", verbose_name=("user_who_edit"), on_delete=models.CASCADE)
    category=models.ForeignKey("backlab.Category", verbose_name=("article_category"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class comment(models.Model):
    comment_id= models.AutoField(primary_key=True)
    comment_text=models.TextField
    article_id=models.ForeignKey("backlab.article", verbose_name=("article_comment"), on_delete=models.CASCADE)
    user=models.ForeignKey("backlab.UserManager", verbose_name=("user_who_comment"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class observation(models.Model):
    observation_id=models.AutoField(primary_key=True)
    observation_text=models.TextField()
    article=models.ForeignKey("backlab.article", verbose_name=("editor_opinion"), on_delete=models.CASCADE)
    editeur=models.ForeignKey("backlab.UserManager", verbose_name=("user_who_give_opinion"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class voteArtcile(models.Model):
    vote_id=models.AutoField(primary_key=True)
    vote_decision = models.BooleanField()
    article = models.ForeignKey("backlab.article", verbose_name=("article_voted"), on_delete=models.CASCADE)
    editeur=models.ForeignKey("backlab.UserManager", verbose_name=("user_who_voted"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_libelle=models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_libelle

class File(models.Model):
    file_id=models.AutoField(primary_key=True)
    file_urls= models.URLField()
    article = models.ForeignKey("backlab.article", verbose_name=("article_file"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# class test(models.Model):
#     test_libelle=models.TextField(max_length=255)







#     def __str__(self):
#         return self.test_libelle
    