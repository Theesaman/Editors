# Generated by Django 5.0.7 on 2024-08-01 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_portfolio_single'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery_Single',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='Images/gallery_single')),
            ],
        ),
    ]