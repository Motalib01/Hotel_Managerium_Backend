# Generated by Django 5.2 on 2025-04-25 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('room_number', models.CharField(max_length=10)),
                ('type', models.CharField(choices=[('single', 'Single'), ('double', 'Double'), ('suite', 'Suite')], max_length=10)),
                ('features', models.TextField()),
                ('discount_used', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='hotel.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='RoomPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='room_pictures/')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='rooms.room')),
            ],
        ),
    ]
