# Generated by Django 4.2.6 on 2023-11-29 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crud', '0021_alter_eventmodel_age_alter_eventmodel_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='age',
            field=models.CharField(blank=True, choices=[('dziecko (do 1 roku życia)', 'dziecko (do 1 roku życia)'), ('dorosły (do 10 roku życia)', 'dorosły (do 10 roku życia)'), ('seniorzy (od 10 lat)', 'seniorzy (od 10 lat)')], max_length=26, null=True, verbose_name='Wiek'),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='contact',
            field=models.EmailField(blank=True, default='youremail@example.com', help_text='(Informacja ta wyświetli się tylko w Wyszukiwarce Zwierzaków, jeśli system znajdzie potencjalnych kandydatów.)', max_length=254, verbose_name='Kontakt'),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='event',
            field=models.TextField(max_length=250, verbose_name='Opis'),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='eyesColor',
            field=models.CharField(blank=True, choices=[('Żółty/złoty', 'Żółty/złoty'), ('Zielony', 'Zielony'), ('Niebieski', 'Niebieski'), ('Miedź/bursztyn', 'Miedź/bursztyn'), ('Dziwne oczy', 'Dziwne oczy'), ('Mieszane kolory', 'Mieszane kolory')], max_length=35, null=True, verbose_name='Kolor oczu'),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='found',
            field=models.BooleanField(default=False, help_text='(Zaznacz to pole, jeśli ZNALEZIONO Twoje zwierzę)', verbose_name='Znaleziono zwierzęta'),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='furColor',
            field=models.CharField(choices=[('Czarny', 'Czarny'), ('Biały', 'Biały'), ('Pomarańczy', 'Pomarańczy'), ('Szary', 'Szary'), ('Dwa różne kolory', 'Dwa różne kolory'), ('Try różne kolory', 'Try różne kolory')], help_text='(Dominujący)', max_length=18, verbose_name='Kolor futra'),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='gender',
            field=models.CharField(blank=True, choices=[('Mężczyzna', 'Mężczyzna'), ('Kobieta', 'Kobieta')], max_length=9, null=True, verbose_name='Płeć'),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='lost',
            field=models.BooleanField(help_text='(Zaznacz to pole, jeśli TWÓJ zwierzak zaginął. Jeśli znalazłeś zwierzaka, NIE zaznaczaj go.)', verbose_name='Zaginął zwierzęta'),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='neighborhood',
            field=models.CharField(choices=[('Bieńczyce', 'Bieńczyce'), ('Bieżanów-Prokocim', 'Bieżanów-Prokocim'), ('Bronowice', 'Bronowice'), ('Czyżyny', 'Czyżyny'), ('Dębniki', 'Dębniki'), ('Grzegórzki', 'Grzegórzki'), ('Krowodrza', 'Krowodrza'), ('Łagiewniki–Borek Fałęcki', 'Łagiewniki–Borek Fałęcki'), ('Mistrzejowice', 'Mistrzejowice'), ('Nowa Huta', 'Nowa Huta'), ('Podgórze', 'Podgórze'), ('Podgórze Duchackie', 'Podgórze Duchackie'), ('Prądnik Biały', 'Prądnik Biały'), ('Prądnik Czerwony', 'Prądnik Czerwony'), ('Stare Miasto', 'Stare Miasto'), ('Swoszowice', 'Swoszowice'), ('Wzgórza Krzesławickie', 'Wzgórza Krzesławickie'), ('Zwierzyniec', 'Zwierzyniec')], help_text='(Ostatni raz widziano zwierzaka.)', max_length=25, verbose_name='Sąsiedztwo'),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Zdjęcie'),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Tytuł'),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='type',
            field=models.CharField(choices=[('kot', 'kot'), ('pies', 'pies'), ('inny', 'inny')], max_length=5, verbose_name='Typ zwierzaka'),
        ),
    ]
