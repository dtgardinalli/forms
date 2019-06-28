from django.db import models

# Create your models here.

class Bolo(models.Model):
    sabores_opcoes = [
        ('ch', 'chocolate'),
        ('mr', 'morango'),
        ('pr', 'prestígio'),
        ('bl', 'baunilha'),
        ('nh','ninho'),
        ('cr', 'churros')
    ]
    recheios_opcoes = [
        ('br', 'brigadeiro'),
        ('dl', 'doce de leite'),
        ('fv', 'frutas vermelhas'),
        ('nt', 'nutella'),
        ('bj', 'beijinho'),
        ('nh', 'ninho')
    ]
    coberturas_opcoes = [
        ('gr', 'granulado'),
        ('ct', 'chantylly'),
        ('mr','morango'),
        ('sc', 'sem cobertura')
    ]

    sabor = models.CharField(max_length=2, choices=sabores_opcoes)
    recheio = models.CharField(max_length=2, choices=recheios_opcoes)
    cobertura = models.CharField(max_length=2, choices=coberturas_opcoes, default='sc')
    peso = models.DecimalField(decimal_places=2, max_digits=3, default=1.00)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome 

class Pedido(models.Model):
    pagamento_opcoes = [
        ('av', 'pagamento à vista'),
        ('p2', 'parcelado em 2 vezes'),
        ('p3', 'parcelado em 3 vezes')
    ]

    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    endereco = models.CharField(max_length=200)
    cartao = models.IntegerField()
    pagamento = models.CharField(max_length=2, choices=pagamento_opcoes, default='av')
   


    # def __str__(self):
    #     return self.nome

