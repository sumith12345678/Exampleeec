# Generated by Django 4.1.6 on 2023-02-09 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_name', models.CharField(max_length=250, null=True)),
                ('price', models.FloatField(null=True)),
                ('category', models.CharField(choices=[('FICTION', 'FICTION'), ('SCIFI', 'SCIFI'), ('ENGINEERING', 'ENGINEERING')], max_length=200, null=True)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('Author', models.CharField(max_length=250, null=True)),
                ('status', models.BooleanField()),
            ],
        ),
    ]