from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse

class CustomAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        user = request.user

        if hasattr(user, 'usuario') and user.usuario:
            request.session['id_usuario'] = user.usuario.id_usuario
        
        # Verifica se o User não tem a Usuario vinculada a ele
        if not hasattr(user, 'usuario'):
            # Redireciona exatamente para a sua view existente
            return reverse('cadastrar_usuario')
            
        # Se já tem, vai para a página inicial
        return super().get_login_redirect_url(request)




