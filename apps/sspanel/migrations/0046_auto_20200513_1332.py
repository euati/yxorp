# Generated by Django 3.0.3 on 2020-05-13 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sspanel', '0045_remove_purchasehistory_good'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vmessnode',
            name='port',
        ),
        migrations.AddField(
            model_name='vmessnode',
            name='client_port',
            field=models.IntegerField(default=10086, verbose_name='客户端端口'),
        ),
        migrations.AddField(
            model_name='vmessnode',
            name='service_port',
            field=models.IntegerField(default=10086, verbose_name='服务端端口'),
        ),
    ]
