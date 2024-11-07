from django.http import HttpResponseForbidden


class FiltraIPMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response
    def __call__(self, request):
        response = self.get_response(request)
        return response
    def process_view(self, request, func, args, kwargs):
        # Lista de IPs autorizados
        ips_autorizados = ['127.0.0.1', '38.50.159.222']
        # IP do usuário
        ip = request.META.get('REMOTE_ADDR')
        # Verifica se o IP do está na lista de IPs autorizados
        if ip not in ips_autorizados:
            # Se usuário não autorizado > HTTP 403 (Não Autorizado)
            return HttpResponseForbidden("IP não autorizado")
        # Se for autorizado, não fazemos nada
        return None