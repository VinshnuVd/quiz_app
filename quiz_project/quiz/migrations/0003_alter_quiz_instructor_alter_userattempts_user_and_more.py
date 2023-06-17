# Generated by Django 4.2.2 on 2023-06-17 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_managers_remove_user_date_joined_and_more'),
        ('quiz', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.user'),
        ),
        migrations.AlterField(
            model_name='userattempts',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attempted_user', to='users.user'),
        ),
        migrations.AlterField(
            model_name='userresponses',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rensponse_provided_by', to='users.user'),
        ),
    ]
