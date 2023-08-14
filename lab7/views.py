from django.http import HttpResponse 
from django.template import loader 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages;
from backlab.models import UserManager, Profil
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import login , logout, authenticate
from django import forms
from django.contrib.auth.hashers import make_password
import secrets, string , pprint


def login_view(request):
    message=''
    if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            # pprint(username)
            user_info = UserManager.objects.filter(email = username)

            # pprint(user_info)
            user = authenticate(request,username=username,password=password)
            # if user.first_connexion == 0 :
            #      return render(request, 'backlab/changepassword.html')

            # else : 
            if user is  not None:
                if user.is_active ==0:
                    message= 'Compte inactif'

            else:
                message="Username or Password is incorrect"

    return render(request, 'backlab/login.html', {'message' : message})



@login_required 
def dashboard_view(request): 
    # template= loader.get_template('store/index.html')
    # return render(request, 'backlab/user.html')(template.render(request=request))

    return render(request, 'backlab/dashbaord.html')

@login_required 
def user_view(request):
    profils = Profil.objects.all()
    characters = string.ascii_letters + string.digits 
    random_password = ''.join(secrets.choice(characters) for _ in range(8))
    user = UserManager.objects.all()

    if request.POST : 
        form = request.POST 
        new_user = UserManager(
            first_name = form['name'],
            password = make_password(form['password']),
            email = form['email'],
            profil_id = form['profil'],
            first_connexion =0,
            is_active =1

        )
        new_user.save()
        message ='ajout réussi'
        # return render (request , 'task/listUser.html', {'message': message })
  
    return render(request, 'backlab/user.html', {'profils': profils, 'random_password': random_password, 'user' : user})



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

@login_required 
def deletearticle_view(request, id):
    return  HttpResponse

@login_required 
def votearticle_view(request):
    return render(request, 'backlab/votearticle.html')


# def logout_view(request):
#     return render(request, 'backlab/user.html')

@login_required 
def setting_view(request):
    return render(request, 'backlab/setting.html')

@login_required 
def message_view(request):
    return render(request, 'backlab/message.html')

def logout_view(request):
    logout(request)
    return redirect('login')
   