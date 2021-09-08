from django.db import models


class Advertisement(models.Model):
    title = models.CharField(verbose_name='Заголовок:', max_length=500)
    description = models.TextField(verbose_name='Описание:')
    created_at = models.DateTimeField(verbose_name='Дата создания:', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='Дата изменения:', auto_now=True)
    price = models.FloatField(verbose_name='Цена:', default=0)
    views_count = models.IntegerField(verbose_name='Количество просмотров:', default=0)
    author_adv = models.ForeignKey('Author', null=True, verbose_name='Автор:',on_delete=models.CASCADE, related_name='author')
    rubric_adv = models.ForeignKey('Rubric', verbose_name='Наименование:', null=True, on_delete=models.CASCADE,
                                   related_name='rubric')
    type_adv = models.ForeignKey('TypeAdv', null=True, on_delete=models.CASCADE, related_name='adv_type',
                                 verbose_name='Тип объявления:')

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    phone = models.IntegerField()

    def __str__(self):
        return self.name


class Rubric(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class TypeAdv(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
