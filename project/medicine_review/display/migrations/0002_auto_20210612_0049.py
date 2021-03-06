# Generated by Django 3.2.3 on 2021-06-11 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('display', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine_data',
            name='Disease',
            field=models.CharField(blank='True', max_length=100),
        ),
        migrations.AlterField(
            model_name='medicine_data',
            name='Dosage',
            field=models.CharField(blank='True', max_length=300),
        ),
        migrations.AlterField(
            model_name='medicine_data',
            name='Patient_Review',
            field=models.CharField(blank='True', max_length=10),
        ),
        migrations.AlterField(
            model_name='medicine_data',
            name='Prescribed_medicine',
            field=models.CharField(blank='True', max_length=100),
        ),
        migrations.AlterField(
            model_name='medicine_data',
            name='Price',
            field=models.IntegerField(blank='True'),
        ),
        migrations.AlterField(
            model_name='medicine_data',
            name='SNo',
            field=models.IntegerField(blank='True'),
        ),
        migrations.AlterField(
            model_name='medicine_data',
            name='Side_Effects',
            field=models.CharField(blank='True', max_length=500),
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
