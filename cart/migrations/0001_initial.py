# Generated by Django 3.0.5 on 2024-03-28 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InforBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(null=True)),
                ('price', models.FloatField(null=True)),
            ],
            options={
                'db_table': 'inforbook',
            },
        ),
    ]
