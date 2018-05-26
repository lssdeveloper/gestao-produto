from django.forms import ModelForm
from .models import Produto


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['codigo_ean',
                  'nome',
                  'descricao',
                  'preco',
                  'imagem'
                 ]
