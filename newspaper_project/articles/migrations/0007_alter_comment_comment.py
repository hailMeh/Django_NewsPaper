# Generated by Django 4.0.3 on 2022-04-03 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(default=True, max_length=150, null=True),
        ),
    ]
