# Generated by Django 3.2.1 on 2021-05-14 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iterview', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendar',
            name='entrevistado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='iterview.entrevistado'),
        ),
        migrations.AddField(
            model_name='agendar',
            name='entrevistador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='iterview.entrevistador'),
        ),
    ]
