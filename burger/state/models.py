from django.db import models

# Create your models here.
class State(models.Model):
  name = models.CharField(max_length=200)
  sigla = models.CharField(max_length=4)

  class Meta:
    db_table = 'sta_state'

class City(models.Model):
    
  name = models.CharField(max_length=200)
  ibge_code = models.CharField(max_length=20)
  sigla = models.CharField(max_length=10, default="")
  state = models.ForeignKey(State, default=0, on_delete=models.CASCADE)
  
  class Meta:
        db_table = 'cit_city'
        ordering = ['-name']
        verbose_name_plural = "Cities"


