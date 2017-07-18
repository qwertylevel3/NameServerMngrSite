# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField()),
                ('registration_time', models.DateTimeField()),
                ('code', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('prov_code', models.IntegerField()),
            ],
            options={
                'db_table': 'city_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CountryList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField()),
                ('registration_time', models.DateTimeField()),
                ('code', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'db_table': 'country_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GroupList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField()),
                ('registration_time', models.DateTimeField()),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'db_table': 'group_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IpSegDat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField()),
                ('registration_time', models.DateTimeField()),
                ('start_ip', models.IntegerField()),
                ('end_ip', models.IntegerField()),
                ('city_code', models.IntegerField()),
                ('net_code', models.IntegerField()),
            ],
            options={
                'db_table': 'ip_seg_dat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NetList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField()),
                ('registration_time', models.DateTimeField()),
                ('code', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'db_table': 'net_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProvList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField()),
                ('registration_time', models.DateTimeField()),
                ('code', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('country_code', models.IntegerField()),
            ],
            options={
                'db_table': 'prov_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServerGroupDat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField()),
                ('registration_time', models.DateTimeField()),
                ('group_id', models.IntegerField()),
                ('server_ids', models.TextField()),
                ('time_out', models.IntegerField()),
            ],
            options={
                'db_table': 'server_group_dat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServerList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField()),
                ('registration_time', models.DateTimeField()),
                ('ip', models.CharField(max_length=32)),
                ('port', models.CharField(max_length=8)),
                ('idc', models.CharField(blank=True, max_length=16, null=True)),
                ('sign', models.CharField(blank=True, max_length=32, null=True)),
                ('is_used', models.IntegerField()),
            ],
            options={
                'db_table': 'server_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServerRuleDat',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('update_time', models.DateTimeField()),
                ('registration_time', models.DateTimeField()),
                ('group_id', models.IntegerField()),
                ('rule', models.CharField(max_length=256)),
                ('rank', models.IntegerField()),
                ('ttl', models.IntegerField()),
                ('compel', models.IntegerField()),
                ('is_use', models.IntegerField()),
            ],
            options={
                'db_table': 'server_rule_dat',
                'managed': False,
            },
        ),
    ]
