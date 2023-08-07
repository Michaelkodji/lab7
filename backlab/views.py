# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response

# from backlab.models import Category
# from backlab.serializers import CategorySerializer

# class CategoryAPIView(APIView):
#     def get (self , *args, **kwargs):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)


from rest_framework.viewsets import ModelViewSet 
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.http import HttpResponse

from backlab.models import Category , article , Profil
from backlab.serializers import CategorySerializer, ArticleSerializer, ProfilSerializer

class CategoryViewset(ModelViewSet):
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.all()

class ProfilViewset(ModelViewSet):
    serializer_class = ProfilSerializer
    def get_queryset(self):
        return Profil.objects.all()


#rechercher un article spécifiquement par sa catégorie (categorie_id)
# class ArticleViewset(ReadOnlyModelViewSet):
#     serializer_class = ArticleSerializer
#     def get_queryset(self):
#         queryset = article.objects.all()
#         category_id = self.request.GET.get('category_id')
#         if category_id is not None :
#             queryset = queryset.filter(category_id=category_id)
#         return queryset

class ArticleViewset(ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer
    def get_queryset(self):

        #ici on récupère tout les articles
        queryset = article.objects.all()

        #recupérer l'id de l'article envoyé en paramètres dans l'url 
        article_id = self.request.GET.get('article_id')
        # vérifie si article_id est vide ou pas
        if article_id is not None :
            #applique le filtre sur la sélection obtenue danq queryset
            queryset = queryset.filter(article_id=article_id)

        #recupérer l'id de la catégorie envoyé en paramètres dans l'url catégorie (categorie_id)
        category_id = self.request.GET.get('category_id')
        # vérifie si categorie_id est vide ou pas
        if category_id is not None :
            #applique le filtre sur la sélection obtenue danq queryset
            queryset = queryset.filter(category_id=category_id)
        return queryset


