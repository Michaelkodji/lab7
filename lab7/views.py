from django.http import HttpResponse 
from django.template import loader 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from backlab.models import UserManager;
from django.contrib.auth import login , logout, authenticate


@login_required
def dashboard_view(request): 
    # template= loader.get_template('store/index.html')
    # return render(request, 'backlab/user.html')(template.render(request=request))

    return render(request, 'backlab/dashbaord.html')

@login_required
def user_view(request):
    password = UserManager.objects.make_random_password()
    return render(request, 'backlab/user.html', {'password': password})


@login_required
def profil_view(request):

    return render(request, 'backlab/profil.html')

@login_required
def comment_view(request):
    return render(request, 'backlab/comment.html')

@login_required
def category_view(request):

    return render(request, 'backlab/category.html')

@login_required
def listarticle_view(request): 


    return render(request, 'backlab/listarticle.html')

@login_required
def writearticle_view(request):
    return render(request, 'backlab/writearticle.html')

@login_required
def updatearticle_view(request, id):
    return  HttpResponse


@login_required
def readarticle_view(request, id):
    return  HttpResponse

def deletearticle_view(request, id):
    return  HttpResponse

def votearticle_view(request):
    return render(request, 'backlab/votearticle.html')


def logout_view(request):
    return render(request, 'backlab/user.html')


def setting_view(request):
    return render(request, 'backlab/setting.html')

def message_view(request):

    return render(request, 'backlab/message.html')

def logout_views(request):
    logout(request)
   