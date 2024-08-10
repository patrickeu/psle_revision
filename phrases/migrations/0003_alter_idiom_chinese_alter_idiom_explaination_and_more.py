# Generated by Django 5.0.6 on 2024-08-03 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phrases', '0002_idiom_chinese_idiomsample'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idiom',
            name='chinese',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='idiom',
            name='explaination',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='idiom',
            name='word',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='idiomsample',
            name='sampleSentence',
            field=models.TextField(verbose_name='sample sentense'),
        ),
    ]
