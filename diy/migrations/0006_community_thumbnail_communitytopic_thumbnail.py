# Generated by Django 4.1.5 on 2023-04-10 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diy', '0005_delete_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='diy/community/thumbnail', verbose_name='サムネイル'),
        ),
        migrations.AddField(
            model_name='communitytopic',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='diy/topic/thumbnail', verbose_name='サムネイル'),
        ),
    ]
