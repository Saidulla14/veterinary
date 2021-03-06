# Generated by Django 3.2.5 on 2021-07-31 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_rename_product_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Текст')),
                ('picture', models.ImageField(blank=True, upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Полезный совет',
                'verbose_name_plural': 'Полезные советы',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Контакт')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='core.contacts')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.RenameModel(
            old_name='Service',
            new_name='Services',
        ),
        migrations.DeleteModel(
            name='Advice',
        ),
    ]
