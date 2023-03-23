# Generated by Django 2.2.16 on 2022-11-05 09:15

from django.db import migrations, models
import django.db.models.deletion
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_auto_20221103_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genretitle',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.Genre'),
        ),
        migrations.AlterField(
            model_name='genretitle',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.Title'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.SmallIntegerField(db_index=True, validators=[reviews.validators.validate_year], verbose_name='Год'),
        ),
    ]
