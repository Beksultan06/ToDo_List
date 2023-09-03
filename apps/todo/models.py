from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовка"
    )
    description = models.TextField(
        max_length="Описание"
    )
    is_completed = models.BooleanField(
        verbose_name="Выполнена"
    )
    created_at = models.BooleanField(
        verbose_name="Создана"
    )
    image = models.ImageField(
        upload_to=True,
        verbose_name="Фотография"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Таск"
        verbose_name_plural = "Таски"
