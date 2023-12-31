# Generated by Django 4.2.6 on 2023-10-24 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0012_alter_eventmodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmodel',
            name='age',
            field=models.CharField(choices=[('baby', 'baby (until 1 year old)'), ('adult', 'adult (until 10 years old)'), ('senior', 'senior (from 10 years old)')], default='chose one option', max_length=26),
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='contact',
            field=models.EmailField(blank=True, default='youremail@example.com', help_text='(This info will not be displayed, but if the system finds potential candidates, you will receive a warning.)', max_length=254),
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='eyesColor',
            field=models.CharField(choices=[('yellow/golden', 'Yellow/Golden'), ('green', 'green'), ('blue', 'blue'), ('copper/amber', 'Copper/Amber'), ('odd-eyed', 'Odd-Eyed (2 different colors each)'), ('mixed colors', 'Mixed Colors')], default='chose one option', max_length=35),
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='furColor',
            field=models.CharField(choices=[('black', 'Black'), ('white', 'White'), ('orange', 'Orange'), ('grey', 'Grey'), ('2_colors', '2 different colors'), ('3_colors', '3 different colors')], default='chose one option', help_text='(The dominant one.)', max_length=18),
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'female')], default='chose one option', max_length=6),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='lost',
            field=models.BooleanField(help_text='(Mark this field if your pet is LOST. If you found a pet DO NOT mark it.)'),
        ),
    ]
