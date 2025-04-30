from .models import Escola

def escola_info(request):
    try:
        escola_item = Escola.objects.first()
    except Escola.DoesNotExist:
        escola_item = None
    return {'escola_item': escola_item}