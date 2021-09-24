from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import ugettext_lazy as _
from burger.security.models import PermissionLevelMixin
from django.contrib.auth.hashers import make_password
from burger.offer.models import TicketRaffle
from burger.address.models import Address
from django.urls import reverse
from datetime import datetime
from django.db import models
import uuid


class Company(models.Model, PermissionLevelMixin):
    id = models.UUIDField(
        primary_key=True,
        default="722ecc2c-9ccb-4439-b9d2-42e8ee5a7844",
        editable=False
    )
    code = models.IntegerField(
        _("Código da Empresa"),
        help_text="Código da Empresa",
        unique=True,
        default=1,
    )
    name = models.CharField(
        _('Nome da Empresa'),
        help_text="Nome da Empresa",
        null=False,
        default="América Burger",
        max_length=40
    )

    class Meta:
        verbose_name = 'Empresa'
        db_table = 'people_company'

class ProfileUserManager(UserManager):
    def get_by_natural_key(self, username):
        return self.get(username__iexact=username)
    
class Profile(AbstractUser):
    hash_id = models.TextField(
        _("ID Unico do Usuário"),
        default=str(uuid.uuid4()), 
        unique=True,
        blank=False,
        null=False
    )
    profile = models.TextField(
        _("Profile"),
        null=True,
        blank=True
    )
    first_name = models.CharField(
        _("Primeiro nome"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("O primeiro nome do usuário")
    )
    last_name = models.CharField(
        _("Sobrenome do usuário"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Sobrenome do usuário")
    )
    phone_number = models.CharField(
        _("Número do Telefone"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Número do telefone pessoal")
    )
    birthday = models.DateTimeField(
        _('Data de Nascimento'),
        default= datetime.now()
    )
    cpf = models.CharField(
        _("CPF do usuário"),
        max_length=11,
        blank=True,
        null=True,
        help_text=_("Cpf do usuário")
    )
    address = models.ForeignKey(Address,null=True, on_delete=models.SET_NULL)
    company = models.ForeignKey(Company,null=True, on_delete=models.SET_NULL)
    tickets =  models.ManyToManyField(TicketRaffle)
    
    def get_absolute_url(self):
        return reverse("profile_detail", args=[self.username])
    
    def class_name(self, value):
        return value.__class__.__name__
    
    @property
    def name_long(self):
        if self.first_name and self.last_name:
            return '%s %s (%s)' % (self.first_name,
                                   self.last_name, self.username)
        elif (not self.first_name) and self.last_name:
            return '%s (%s)' % (self.last_name, self.username)
        elif self.first_name and (not self.last_name):
            return '%s (%s)' % (self.first_name, self.username)
        else:
            return self.username
    
    def save(self, *args, **kwargs):
        list_hash_id = Profile.objects.values_list('hash_id', flat=True)
        company = Company.objects.get(code=1)
        
        if self.hash_id in list_hash_id:
            self.hash_id = str(uuid.uuid4())

        super(Profile, self).save()
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        
    
    
def get_anonymous_user_instance(user_model):
    return user_model(pk=-1, username='AnonymousUser')
    