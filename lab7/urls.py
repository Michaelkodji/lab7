
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


    path('', views.login_view, name='login'),
    path('admin/', admin.site.urls , name='admin'),
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('profil', views.profil_view, name='profil'),
    path('login', views.login_view, name='login'),
    path('setting', views.setting_view, name='setting'),
    path('message', views.message_view, name='message'),
    path('logout', views.logout_view, name='logout'),

    path('user', views.user_view, name='user'),
    path('listuser', views.user_view, name='listuser'),
    path('updateuser/<int:id>/', views.user_view, name='updateuser'),
   
   

    path('comment', views.comment_view, name='comment'),
    path('listcomment', views.comment_view, name='listcomment'),
    path('Deltecomment/<int:id>/', views.comment_view, name='deletecomment'),

    path('category', views.category_view, name='category'),
    path('listcategory', views.category_view, name='listcategory'),
    path('Updatecategory/<int:id>/', views.category_view, name='updatecategory'),
    path('Deletecategory/<int:id>/', views.category_view, name='deletecategory'),


    path('writearticle', views.writearticle_view, name='writearticle'),
    path('listarticle', views.listarticle_view, name='listarticle'),
    path('votearticle', views.votearticle_view, name='votearticle'),
    path('readarticle/<int:id>/', views.readarticle_view, name='readarticle'),
    path('updatearticle/<int:id>/', views.updatearticle_view, name='updatearticle'),
    path('deletearticle/<int:id>/', views.deletearticle_view, name='deletearticle'),


    path('api-auth/', include('rest_framework.urls')),
    # path('api/category/', CategoryAPIView.as_view())

    #ajout de l'url du routeur dans le pattern
    path('api/', include(router.urls))
    
]
