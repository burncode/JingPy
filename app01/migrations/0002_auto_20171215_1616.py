# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 08:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=32, verbose_name='主机名')),
                ('ip', models.GenericIPAddressField(protocol='ipv4', verbose_name='IP')),
                ('port', models.IntegerField(verbose_name='端口')),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(default=1, max_length=32, verbose_name='邮箱'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='password',
            field=models.CharField(default=1, max_length=32, verbose_name='密码'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='role',
            field=models.ManyToManyField(default=1, to='app01.Role', verbose_name='用户角色'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='ut',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app01.UserType', verbose_name='用户类型'),
        ),
    ]
