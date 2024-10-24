from elibrosLoja.models import Carrinho
import re

def carrinho(request):
    try:
        if request.user.is_authenticated:
            carrinho, created = Carrinho.objects.get_or_create(cliente=request.user)
        else:
            carrinho, created = Carrinho.objects.get_or_create(session_id=request.session['session_id'])
    except:
        carrinho = {'total': 0, 'numero_itens': 0}
        print(carrinho)
    
    return {'carrinho': carrinho}

def cliente(request):
    try:
        cliente = request.user
    except:
        cliente = None
    return {'cliente': cliente}

def remove_special_characters(text):
  special_chars = re.compile(r'[^a-zA-Z0-9]')
  return special_chars.sub('', text)