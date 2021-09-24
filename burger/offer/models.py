from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from burger.base.models import ResourceBase
from django.utils.text import slugify
from django.conf import settings
from django.db import models
from PIL import Image 
import shortuuid
import datetime
import time
import uuid
import os

class Offer(ResourceBase):

  start_date = models.DateTimeField(
    _('Data de Inicio'),
    help_text = "Data que inicia o oferta",
    null = True,
    unique = False
  )
  end_date = models.DateTimeField(
    _('Data do Fim'),
    help_text = "Data que finaliza a oferta",
    null = True,
    unique = False
  )
  title = models.CharField(
    _('Título da Oferta'),
    help_text="Titulo da oferta",
    null=False,
    default="",
    max_length=40
  )
  short_description = models.CharField(
    _('Pequena Descrição'),
    help_text = "Pequeno resumo da oferta",
    null = False,
    unique = False,
    max_length=500
  )
  image_file = models.ImageField(
    _('Imagem da Oferta'),
    help_text = "Imagem da oferta que aparecera no site",
    null = False,
    default="",
    upload_to = "offers"
  )
  available = models.BooleanField(
      _('Ativo'),
      default=True
    )
  upload_session = models.ForeignKey('UploadSession', blank=True, null=True, on_delete=models.SET_NULL, default=None)
  slug = models.SlugField(default='', blank=True)
  hash_id = models.TextField(default=str(uuid.uuid4()), unique=True)
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  update_at = models.DateTimeField(auto_now=True, blank=True)

  @property
  def get_date(self):
    return datetime.datetime.strftime(self.end_date, "%m/%d/%Y, %H:%M:%S")

  def save(self, *args, **kwargs):
    if self.end_date < self.start_date:
        raise ValidationError("End date is before start date")

    super(Offer, self).save()
    image = Image.open(self.image_file)
    (width, height) = image.size  

    if self.category.identifier == 'slide' or self.category.identifier == 'sorteio':   
      size = ( 1200, 440)
    elif self.category.identifier == 'sorteio-banner':
      size = (590, 253)
    else:
      size = ( 387, 200)

    image = image.resize(size, Image.ANTIALIAS)
    image.save(os.path.join(settings.PROJECT_ROOT,'uploaded/' + str(self.image_file)))

  class Meta:
    verbose_name = 'Oferta'
    verbose_name_plural = 'Ofertas'
    db_table = "off_offer"
  
  def __str__(self):
      return self.title
    

class TicketRaffle(models.Model):
  code = models.TextField(
    default=shortuuid.ShortUUID().random(length=6).upper(), unique=True
  )
  active = models.BooleanField(
    default = False
  )
  offer = models.ForeignKey(Offer,blank=True, null=True, on_delete=models.SET_NULL, default=None)

  def save(self, *args, **kwargs):
    list_ticket = TicketRaffle.objects.values_list('code', flat=True)

    # while(self.code not in list_ticket):
    #   self.code = shortuuid.ShortUUID().random(length=6).upper()

    super(TicketRaffle, self).save()


  class Meta:
    verbose_name = "Cupom"
    verbose_name_plural = "Cupons"
    db_table = "tic_ticket"

  def __str__(self):
    used = "Não usado"
    if(self.active == 1):
      used = "Usado"
    return "Cupom - " + self.code + " - " + used



class UploadSession(models.Model):

  
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    processed = models.BooleanField(default=False)
    error = models.TextField(blank=True, null=True)
    traceback = models.TextField(blank=True, null=True)
    context = models.TextField(blank=True, null=True)