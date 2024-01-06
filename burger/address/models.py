from django.utils.translation import gettext_lazy as _
from burger.state.models import City
from django.db import models
# Create your models here.

class Address(models.Model):

  street_name = models.CharField(
    _('Nome da Rua'),
    help_text = "Nome de Rua, Avenida, Rodovia",
    null = False,
    unique = False,
    max_length=200)
  cep = models.CharField(
    _('CEP'),
    help_text = "Cep da Rua, Avenida, Rodovia",
    null = False,
    unique = False,
    max_length=12)
  number = models.IntegerField(
    _('Número da Rua'),
    help_text = "Numero da Rua, Avenida, Rodovia",
    null = False,
    unique = False)

  city = models.ForeignKey(
    City, 
    default=0, 
    on_delete=models.CASCADE)


  class Meta:
    verbose_name = 'Endereço'
    db_table = 'add_address'