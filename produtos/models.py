from django.db import models


class Produto(models.Model):
    codigo_ean = models.IntegerField()
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=15, decimal_places=2)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='produtos_fotos', null=True, blank=True)

    def __str__(self):
        return self.codigo_ean + ' - ' + self.nome
