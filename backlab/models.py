from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser

class UserManager(AbstractBaseUser):
    def __str__(self) -> str:
        return super().__str__()
    
class Profil(models.model):
    profil_id = models.IntegerField(primary_key=True)
    profil_libelle = models.CharField(max_length=255)

class article(models.model):
    article_id=models.BigIntegerField(primary_key=True)
    article_text=models.TextField()
    editeur_id=models.ForeignKey("backlab.UserManager", verbose_name=("user_who_edit"), on_delete=models.CASCADE)

class comment(models.model):
    comment_id= models.IntegerField(primary_key=True)
    comment_text=models.TextField
    article_id=models.ForeignKey("backlab.article", verbose_name=("article_comment"), on_delete=models.CASCADE)
    user_id=models.ForeignKey("backlab.UserManager", verbose_name=("user_who_comment"), on_delete=models.CASCADE)


class observation(models.model):
    observation=models.BigIntegerField(primary_key=True)
    observation_text=models.TextField()
    article_id=models.ForeignKey("backlab.article", verbose_name=("editor_opinion"), on_delete=models.CASCADE)
    editeur_id=models.ForeignKey("backlab.UserManager", verbose_name=("user_who_give_opinion"), on_delete=models.CASCADE)


class voteArtcile(models.model):
    vote_id=models.BigIntegerField(primary_key=True)
    vote_decision = models.BooleanField()
    article_id = models.ForeignKey("backlab.article", verbose_name=("article_voted"), on_delete=models.CASCADE)
    editeur_id=models.ForeignKey("backlab.UserManager", verbose_name=("user_who_voted"), on_delete=models.CASCADE)
    