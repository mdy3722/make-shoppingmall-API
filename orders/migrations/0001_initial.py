# Generated by Django 5.0.6 on 2024-07-03 02:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('PREPARING', 'Preparing'), ('DONE', 'Done')], default='PREPARING', max_length=100)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
