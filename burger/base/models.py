from polymorphic.models import PolymorphicModel, PolymorphicManager
from burger.security.models import PermissionLevelMixin
from django.utils.translation import gettext_lazy as _
from taggit.models import TagBase, ItemBase
from django.db.models import Q, signals
from django.db import models

class TopicCategory(models.Model):
  TYPES = (
    ('banner', 'banner'),
    ('slide', 'slide'),
    ('sorteio', 'sorteio'),
    ('sorteio-banner', 'sorteio-banner'),
  )
  identifier = models.CharField(
    _('Nome'),
    max_length=255, 
    default="",
    choices=TYPES)
  slug = models.SlugField(
    _('Slug'),
    max_length=50, 
    unique=True, 
    default="")
  description = models.TextField(
    _('Descrição'),
    default="")
  fa_class = models.CharField(max_length=64, default="fa-times")
  is_active = models.BooleanField(
    _('Ativo'),
    default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return 'Categoria: ' + self.identifier

  class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['-created_at']

  

class TopicType(models.Model):

  identifier = models.CharField(
    max_length=255, 
    default="Público")
  description = models.TextField(
    _('Descrição'),
    default="")
  fa_class = models.CharField(max_length=64, default="fa-times")
  is_active = models.BooleanField(
    _('Ativo'),
    default=True) 
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return 'Tipo: ' + self.identifier
  class Meta:
        verbose_name = "Tipo"
        ordering = ['-created_at']
        verbose_name_plural = "Tipos"

class Contact(models.Model):
  ip = models.CharField(
    max_length=40,
    default=""
  )
  name = models.CharField(
    max_length=255,
    default=""
  )
  email = models.CharField(
    max_length=255,
    default=""
  )
  message = models.TextField(
    max_length=1000,
    default=""
  )

  def __str__(self):
    return "Contato"
  
  class Meta:
    verbose_name = "Contato"
    verbose_name_plural = "Contatos"

class ResourceBase(PolymorphicModel, PermissionLevelMixin, ItemBase):
  
  category_help_text = _("Categoria a qual o evento se encaixa")
  type_help_text = _("Tipo do evento")
  
  category = models.ForeignKey(
    TopicCategory,
    null=True,
    blank=True,
    help_text=category_help_text,
    on_delete=models.SET_NULL)
    
  type_event = models.ForeignKey(
    TopicType,
    null=True,
    blank=True,
    help_text=type_help_text,
    on_delete=models.SET_NULL)
