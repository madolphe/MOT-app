# Generated by Django 3.0.5 on 2020-05-13 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0003_auto_20200513_0922'),
    ]

    operations = [
        migrations.CreateModel(
            name='DynamicProps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study', models.CharField(default='', max_length=10)),
                ('base_html', models.CharField(default='', max_length=50)),
                ('greet', models.CharField(default='Salut, User !', max_length=50)),
                ('task_url', models.CharField(default='', max_length=50)),
                ('style', models.CharField(default='', max_length=50)),
            ],
        ),
    ]