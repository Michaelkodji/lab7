from django.shortcuts import redirect
from django.urls import reverse

class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Vérifiez si l'utilisateur est authentifié
        if not request.user.is_authenticated:
            # Redirigez l'utilisateur vers la page de connexion
            return redirect(reverse('admin'))  # Assurez-vous d'avoir configuré le nom de l'URL pour la page de connexion.
        else :
            return redirect(reverse('dashboard'))
        response = self.get_response(request)
        return response
