from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse

class CustomAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        user = request.user

        if hasattr(user, 'instituicao') and user.instituicao:
            request.session['id_inst'] = user.instituicao.id_inst
        
        # Verifica se o User não tem a Instituicao vinculada a ele
        if not hasattr(user, 'instituicao'):
            # Redireciona exatamente para a sua view existente
            return reverse('cadastrar_instituicao')
            
        # Se já tem, vai para a página inicial
        return super().get_login_redirect_url(request)




