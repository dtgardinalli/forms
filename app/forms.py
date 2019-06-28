from django import forms
from app.models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'cpf',
            'email',
            'endereco',
            'cartao',
            'pagamento',
        ]