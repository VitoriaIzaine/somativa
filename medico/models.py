from django.db import models


class cadastro_medicos(models.Model):
    nome = models.CharField(max_length=30)
    especialidade = models.CharField(max_length=30)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%y/%m/%d/')

    def __str__(self):
        return self.nome
