from django.shortcuts import render
from app.forms import PedidoForm

# Create your views here.

def mostrar_index(request):
    formulario = PedidoForm(request.POST or None)
    mensagem = ''
    if formulario.is_valid():
        formulario.save()
        formulario = PedidoForm
        mensagem = 'pedido realizado com sucesso'

    contexto = {
        'form': formulario,
        'mensagem': mensagem,
    }
    return render(request, 'index.html', contexto)

