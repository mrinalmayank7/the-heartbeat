# Generated by Django 3.2.5 on 2021-08-16 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAINAPP', '0003_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiagnosisTool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tool_name', models.CharField(max_length=200)),
                ('tool_accuracy', models.CharField(max_length=200)),
                ('tool_technology', models.CharField(max_length=200)),
                ('tool_detail', models.TextField(max_length=4000)),
                ('tool_link', models.CharField(max_length=200)),
            ],
        ),
    ]