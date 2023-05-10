# Generated by Django 4.2 on 2023-05-05 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('msg', models.TextField()),
                ('like', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('proid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cmt', to='product.fruits')),
            ],
        ),
    ]
