# Generated by Django 2.0.1 on 2018-08-08 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year_released', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('birth_date', models.CharField(default='', max_length=100)),
                ('biggest_hit', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('album', models.ManyToManyField(to='history.Album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='history.Artist')),
            ],
        ),
    ]
