# Generated by Django 2.2 on 2021-09-04 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0004_auto_20210904_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='rubric_adv',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rubric', to='advertisements_app.Rubric'),
        ),
    ]
