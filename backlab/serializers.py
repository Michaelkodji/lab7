from rest_framework.serializers import ModelSerializer

from backlab.models import Category

class CategorySerializer(ModelSerializer):
    class Meta :
        model = Category
        fields =['category_id', 'category_libelle']