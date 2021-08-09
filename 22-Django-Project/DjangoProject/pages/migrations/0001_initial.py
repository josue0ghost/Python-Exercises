# Generated by Django 3.2.4 on 2021-08-04 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('slug', models.CharField(max_length=50, unique=True, verbose_name='URL amigable')),
                ('visible', models.BooleanField(verbose_name='Visible')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='ACtualizado el')),
            ],
            options={
                'verbose_name': 'Página',
                'verbose_name_plural': 'Páginas',
            },
        ),
    ]
