# Generated by Django 4.1.5 on 2023-04-20 12:08

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('diy', '0006_community_thumbnail_communitytopic_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infomation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日時')),
                ('overview', models.TextField(verbose_name='会社概要')),
                ('term', models.TextField(verbose_name='会社概要')),
            ],
        ),
    ]
