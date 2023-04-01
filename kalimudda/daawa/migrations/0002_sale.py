# Generated by Django 4.1.7 on 2023-03-29 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daawa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('amount_received', models.IntegerField(blank=True, default=0, null=True)),
                ('issued_to', models.CharField(blank=True, max_length=50, null=True)),
                ('unit_price', models.IntegerField(blank=True, default=0, null=True)),
                ('sold_at', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daawa.product')),
            ],
        ),
    ]