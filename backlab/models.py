from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser

# class UserManager(AbstractBaseUser):
#     def __str__(self) -> str:
#         return super().__str__()
    
# class Profil(models.Model):
#     profil_id = models.IntegerField(primary_key=True)
#     profil_libelle = models.CharField(max_length=255)

# class article(models.Model):
#     article_id=models.BigIntegerField(primary_key=True)
#     article_text=models.TextField()
#     editeur_id=models.ForeignKey("backlab.UserManager", verbose_name=("user_who_edit"), on_delete=models.CASCADE)
#     category_id=models.ForeignKey("backlab.Category", verbose_name=("article_category"), on_delete=models.CASCADE)

# class comment(models.Model):
#     comment_id= models.IntegerField(primary_key=True)
#     comment_text=models.TextField
#     article_id=models.ForeignKey("backlab.article", verbose_name=("article_comment"), on_delete=models.CASCADE)
#     user_id=models.ForeignKey("backlab.UserManager", verbose_name=("user_who_comment"), on_delete=models.CASCADE)


# class observation(models.Model):
#     observation=models.BigIntegerField(primary_key=True)
#     observation_text=models.TextField()
#     article_id=models.ForeignKey("backlab.article", verbose_name=("editor_opinion"), on_delete=models.CASCADE)
#     editeur_id=models.ForeignKey("backlab.UserManager", verbose_name=("user_who_give_opinion"), on_delete=models.CASCADE)


# class voteArtcile(models.Model):
#     vote_id=models.BigIntegerField(primary_key=True)
#     vote_decision = models.BooleanField()
#     article_id = models.ForeignKey("backlab.article", verbose_name=("article_voted"), on_delete=models.CASCADE)
#     editeur_id=models.ForeignKey("backlab.UserManager", verbose_name=("user_who_voted"), on_delete=models.CASCADE)


class Category(models.Model):
    category_id=models.BigIntegerField(primary_key=True)
    category_libelle=models.TextField(max_length=255)

    def __str__(self):
        return self.category_libelle
    
# class test(models.Model):
#     test_libelle=models.TextField(max_length=255)
#     def __str__(self):
#         return self.test_libelle
    