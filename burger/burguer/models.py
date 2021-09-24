from django.utils.translation import ugettext_lazy as _
from burger.security.models import PermissionLevelMixin
from django.core.exceptions import ValidationError
from burger.people.models import Profile
from django.utils.text import slugify
from django.conf import settings
from django.db import models
from PIL import Image 
import numpy as np
import datetime
import time
import uuid
import os

class Burguer(models.Model, PermissionLevelMixin):

    POINT = (
        (1, 'Mal Passado'),
        (2, 'No Ponto'),
        (3, 'Bem Passado'),
    )
    TYPES = (
        (1, 'Burger Unico'),
        (2, 'Combo Simples'),
        (3, 'Combo Duplo'),
    )
    code = models.CharField(
        _("Código"),
        help_text="Código do Hamburguer",
        null=False,
        default="",
        max_length=20
    )
    name = models.CharField(
        _('Nome do Hamburguer'),
        help_text="Nome do Hamburguer",
        null=False,
        default="",
        max_length=40
    )
    description = models.CharField(
        _("Descrição do Hamburguer"),
        help_text="Descrição do Hamburger",
        null=False,
        default="",
        max_length=500
    )
    price = models.DecimalField(
        _("Preço"),
        help_text="Preço do Hamburguer",
        max_digits=10, 
        decimal_places=2, 
        default=0.00
    )
    discount = models.IntegerField(
        _("Desconto(%)"),
        help_text="Desconto que será dada em (%) ao Hamburguer",
        default=0
    )
    weight = models.DecimalField(
        _("Peso"),
        help_text="Peso total do Hamburguer",
        max_digits=10,
        decimal_places=0,
        default=0.00
    )
    energetic_value = models.DecimalField(
        _("Valor Energético"),
        help_text="Valor Energético",
        max_digits=10,
        decimal_places=0,
        default=0.00
    )
    point = models.IntegerField(
        _("Estado do Hamburguer"),
        help_text="Estado do Hamburguer",
        default=2,
        choices=POINT
    )
    burger_type = models.IntegerField(
        _("Tipo do produto vendido"),
        help_text="Tipo do produto vendido",
        default=1,
        choices=TYPES
    )
    available = models.BooleanField(
        _("Ativo"),
        default=True
    )
    image_file = models.ImageField(
        _("Imagem Principal"),
        help_text = "Imagem do hamburguer",
        null = False,
        default="",
        upload_to = "burgers"
    )
    hash_id = models.TextField(
        default=str(uuid.uuid4()), unique=True
    )
    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    @property
    def get_total_value(self):
        return float(self.price) - (float(self.price) * (self.discount/100))

    def __str__(self):
      return self.code + ' : ' + self.name

    def save(self, *args, **kwargs):

        super(Burguer, self).save()
        image = Image.open(self.image_file)
        (width, height) = image.size  

        size = ( 278, 250)

        if self.burger_type == 2:
            size = ( 278, 247)

        image = image.resize(size, Image.ANTIALIAS)
        image.save(os.path.join(settings.PROJECT_ROOT,'uploaded/' + str(self.image_file)))

    class Meta:
        verbose_name = 'Burger'
        db_table = 'bur_burguer'


class Photo(models.Model):
    burguer = models.ForeignKey(Burguer, null=True, blank=True, on_delete=models.SET_NULL)
    image_file =  models.ImageField(
        _("Imagem"),
        help_text = "Imagem do Hamburguer",
        null = False,
        default="",
        upload_to = "burgers"
    )
    is_active = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.burguer.name + ' : ' + str(self.image_file)
    
    def save(self, *args, **kwargs):

        super(Photo, self).save()
        image = Image.open(self.image_file)
        (width, height) = image.size  

        size = ( 278, 250)

        image = image.resize(size, Image.ANTIALIAS)
        image.save(os.path.join(settings.PROJECT_ROOT,'uploaded/' + str(self.image_file)))

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"
        db_table = "pho_photo"


class Ingredient(models.Model):
    burguer = models.ForeignKey(Burguer, null=True, blank=True,default=0, on_delete=models.SET_NULL)
    product = models.CharField(
        _("Produto"),
        help_text="Produto",
        null=False,
        max_length=200
    )
    quantity = models.IntegerField(
        _("Quantidade"),
        help_text="Quantidade do Item",
        default=1
    )

    class Meta:
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'
        db_table = 'ing_ingredient'

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    burguer = models.ForeignKey(Burguer, null=True, blank=True,default=0, on_delete=models.SET_NULL)
    user = models.ForeignKey(Profile, null=True, blank=True,default=0, on_delete=models.SET_NULL)
    comment = models.CharField(
        _("Comentário"),
        help_text="Comentário adicionado ao produto",
        max_length=200
    )
    rating = models.IntegerField(
        _("Estrelas"),
        help_text="Estrela que o produto recebeu",
        choices=RATING_CHOICES
    )

    class Meta:
        verbose_name = 'Review'
        db_table = 'rev_review'
