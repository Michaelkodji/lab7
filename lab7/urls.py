
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from . import views 

from backlab.views import CategoryViewset , ArticleViewset, ProfilViewset

#création du routeur
router =routers.SimpleRouter()

# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register('category', CategoryViewset, basename='category')
router.register('article', ArticleViewset, basename='article')
router.register('profil', ProfilViewset, basename='profil')

urlpatterns = [



    path('admin/', admin.site.urls),
    path('dashboard', views.dashboard_view),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/category/', CategoryAPIView.as_view())

    #ajout de l'url du routeur dans le pattern
    path('api/', include(router.urls))
    
]
