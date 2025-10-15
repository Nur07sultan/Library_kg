from django.db import models

class Category(models.Model):
    name = models.CharField("Название категории", max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Clothes(models.Model):
    title = models.CharField("Название одежды", max_length=200)
    description = models.TextField("Описание", blank=True, null=True)
    price = models.DecimalField("Цена", max_digits=8, decimal_places=2)
    categories = models.ManyToManyField(Category, verbose_name="Категории", related_name='clothes')
    image = models.ImageField("Фото", upload_to='clothes/', blank=True, null=True)

    class Meta:
        verbose_name = "Одежда"
        verbose_name_plural = "Одежда"

    def __str__(self):
        return self.title

