# Generated by Django 3.1.7 on 2021-06-04 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipzon', '0006_auto_20210602_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.IntegerField(verbose_name='10')),
                ('query', models.CharField(max_length=500)),
            ],
        ),
    ]
