# Generated by Django 4.2.6 on 2023-10-11 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_alter_eventmodel_neighborhood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='neighborhood',
            field=models.CharField(choices=[('bienczyce', 'Bieńczyce'), ('Bronowice', 'bronowice'), ('Czyżyny', 'czyzyny'), ('Dębniki', 'debniki'), ('Grzegórzki', 'grzegorzki'), ('Krowodrza', 'krowodrza'), ('Łagiewniki–Borek Fałęcki', 'lagiewniki_Borek'), ('Mistrzejowice', 'mistrzejowice'), ('Nowa Huta', 'nh'), ('Podgórze', 'podgorze'), ('Podgórze Duchackie', 'podgorze_duchackie'), ('Prądnik Biały', 'pradnik_bialy'), ('Prądnik Czerwony', 'pradnik_czerwony'), ('Bieżanów-Prokocim', 'prokocim'), ('Stare Miasto', 'stare_miasto'), ('Swoszowice', 'swoszowice'), ('Wzgórza Krzesławickie', 'wzgorza_krzeslawickie'), ('Zwierzyniec', 'zwierzyniec')], max_length=25),
        ),
    ]
