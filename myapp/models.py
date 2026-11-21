from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    age = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Programa(models.Model):
    # El campo id lo crea Django automáticamente.
    codigo = models.CharField("código", max_length=20, unique=True)
    nombre = models.CharField("nombre", max_length=200)
    estado = models.BooleanField("estado", default=True)
    facultad = models.CharField("facultad", max_length=200)

    class Meta:
        ordering = ["id"]
        verbose_name = "programa"
        verbose_name_plural = "programas"

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
