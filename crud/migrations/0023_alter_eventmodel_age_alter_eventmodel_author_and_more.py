# Generated by Django 4.2.6 on 2023-12-04 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crud', '0022_alter_eventmodel_age_alter_eventmodel_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='age',
            field=models.CharField(blank=True, choices=[('szczenię (do 1 roku życia)', 'szczenię (do 1 roku życia)'), ('dorosły (do 10 roku życia)', 'dorosły (do 10 roku życia)'), ('seniorzy (od 10 lat)', 'seniorzy (od 10 lat)')], max_length=26, null=True, verbose_name='Wiek'),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='eyesColor',
            field=models.CharField(blank=True, choices=[('Żółty/złoty', 'Żółty/złoty'), ('Zielony', 'Zielony'), ('Niebieski', 'Niebieski'), ('Miedź/bursztyn', 'Miedź/bursztyn'), ('Mieszane kolory', 'Mieszane kolory')], max_length=35, null=True, verbose_name='Kolor oczu'),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='found',
            field=models.BooleanField(default=False, help_text='(Zaznacz to pole, jeśli Twój pupil już się ODNALAZŁ. Jeśli znalazłeś zwierzaka, NIE zaznaczaj żadnego z pól.)', verbose_name='Znaleziony zwierzak'),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='furColor',
            field=models.CharField(choices=[('Czarny', 'Czarny'), ('Biały', 'Biały'), ('Rudy', 'Rudy'), ('Szary', 'Szary'), ('Dwa różne kolory', 'Dwa różne kolory'), ('Trzy różne kolory', 'Trzy różne kolory')], help_text='(Dominujący)', max_length=18, verbose_name='Kolor futra'),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='gender',
            field=models.CharField(blank=True, choices=[('Samiec', 'Samiec'), ('Samica', 'Samica')], max_length=9, null=True, verbose_name='Płeć'),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='lost',
            field=models.BooleanField(help_text='(Zaznacz to pole, jeśli Twój zwierzak ZAGINĄŁ. Jeśli znalazłeś zwierzaka, NIE zaznaczaj żadnego z pól.)', verbose_name='Zaginiony zwierzak'),
        ),
    ]
