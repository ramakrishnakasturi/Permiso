# Generated by Django 3.2.9 on 2021-12-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permiso', '0004_alter_permission_grant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Approved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('req', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
