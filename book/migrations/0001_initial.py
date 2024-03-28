# Generated by Django 3.0.5 on 2024-03-28 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=224)),
                ('author', models.CharField(max_length=224)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='images/books')),
                ('description', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('book_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
