from django.db import models

# Create your models here.

class modalidad(models.Model):
    class Meta:
        verbose_name = 'Modalidad'
        verbose_name_plural = 'Modalidades'
    codigo = models.AutoField(primary_key=True)
    modal = models.CharField(max_length=100, verbose_name='Oferta')
    def __str__(self):
        return self.modal

class oferta(models.Model):
    class Meta:
        verbose_name = "Ingrediente"
        verbose_name_plural = "Ingredientes"
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='items',null=True,blank=True)
    ingredientes = models.CharField(max_length=200,null=True,blank=True)
    moda = models.ForeignKey(modalidad, on_delete=models.CASCADE,blank=False,null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nombre

