# Generated by Django 5.0.7 on 2024-07-31 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_portfolioitem_delete_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('image', models.ImageField(upload_to='Images/portfolio')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='PortfolioItem',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.portfoliocategory'),
        ),
    ]
