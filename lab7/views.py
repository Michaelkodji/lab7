from django.http import HttpResponse 

def dashboard_view(request): 
    return HttpResponse('Hello world')