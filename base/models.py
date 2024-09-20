from django.db import models

# Create your models here.
class Test(models.Model):
    full_name = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    number = models.CharField(
        max_length=255,
        verbose_name="Номер телефона"
    )
    date = models.DateTimeField(
        verbose_name="Дата"
    )

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Основные настройки"