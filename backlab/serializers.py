from rest_framework.serializers import ModelSerializer

from backlab.models import Category , article , Profil , comment , observation , voteArtcile, UserManager

class UserSerialize(ModelSerializer):
    class Meta :
        model = UserManager
        fields=('__all__')

class CategorySerializer(ModelSerializer):
    class Meta :
        model = Category
        fields =['category_id', 'category_libelle']

class ArticleSerializer (ModelSerializer):
    class Meta :
        model = article
        fields = ['article_id', 'article_text', 'editeur_id','category_id','created_at','updated_at']

class ProfilSerializer(ModelSerializer):
    class Meta :
        model = Profil
        fields =['profil_id', 'profil_libelle']

class CommentSerializer(ModelSerializer):
    class Meta :
        model = comment
        fields = ('__all__')

class ReviewSerialize(ModelSerializer):
    class Meta : 
        model = observation
        fields = ('__all__')

class VoteSerialize(ModelSerializer):
    class Meta :
        model = voteArtcile
        fields = ('__all__')