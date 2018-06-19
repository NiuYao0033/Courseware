# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-19 00:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LenongApps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(max_length=50, verbose_name='轮播图')),
                ('bimage', models.ImageField(max_length=250, upload_to='static/images')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gcontent',
            field=models.TextField(verbose_name='详细介绍'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gjianjie',
            field=models.CharField(max_length=200, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gkucun',
            field=models.IntegerField(verbose_name='库存'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpic',
            field=models.ImageField(upload_to='df_goods', verbose_name='图片位置'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gprice',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gtitle',
            field=models.CharField(max_length=20, verbose_name='商品名称'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LenongApps.TypeInfo', verbose_name='商品分类'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gunit',
            field=models.CharField(default='500g', max_length=20, verbose_name='单位'),
        ),
    ]
