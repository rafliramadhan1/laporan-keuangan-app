# Generated by Django 3.1.3 on 2021-02-09 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('tipe', models.CharField(choices=[('pemasukan', 'Pemasukan'), ('pengeluaran', 'Pengeluaran')], max_length=20)),
                ('nominal', models.IntegerField()),
                ('deskripsi', models.TextField()),
                ('bukti', models.FileField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Administration',
            },
        ),
    ]