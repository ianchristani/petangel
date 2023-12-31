# Generated by Django 4.2.6 on 2023-10-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0006_eventmodel_found'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='neighborhood',
            field=models.CharField(choices=[('bienczyce', 'Bieńczyce'), ('prokocim', 'Bieżanów-Prokocim'), ('bronowice', 'Bronowice'), ('czyzyny', 'Czyżyny'), ('debniki', 'Dębniki'), ('grzegorzki', 'Grzegórzki'), ('krowodrza', 'Krowodrza'), ('lagiewniki_Borek', 'Łagiewniki–Borek Fałęcki'), ('mistrzejowice', 'Mistrzejowice'), ('nowahuta', 'Nowa Huta'), ('podgorze', 'Podgórze'), ('podgorze_duchackie', 'Podgórze Duchackie'), ('pradnik_bialy', 'Prądnik Biały'), ('pradnik_czerwony', 'Prądnik Czerwony'), ('stare_miasto', 'Stare Miasto'), ('swoszowice', 'Swoszowice'), ('wzgorza_krzeslawickie', 'Wzgórza Krzesławickie'), ('zwierzyniec', 'Zwierzyniec')], max_length=25),
        ),
    ]
