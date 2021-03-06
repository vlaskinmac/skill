# Generated by Django 2.2 on 2021-09-04 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя автора:')),
                ('email', models.CharField(max_length=30, verbose_name='E-mail:')),
                ('phone', models.IntegerField(verbose_name='Телефон:')),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок:')),
                ('description', models.TextField(verbose_name='Описание:')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания:')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения:')),
                ('price', models.FloatField(default=0, verbose_name='Цена:')),
                ('views_count', models.IntegerField(default=0, verbose_name='Количество просмотров:')),
                ('author_adv', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='advertisements_app.Author')),
            ],
        ),
    ]
