# Generated by Django 5.2 on 2025-04-28 18:46

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appspot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('password', models.CharField(max_length=64)),
                ('balance', models.IntegerField()),
                ('role', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
        migrations.DeleteModel(
            name='UserAdmin',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='uid',
        ),
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='category',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appspot.user'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appspot.user'),
        ),
        migrations.DeleteModel(
            name='UserPersonal',
        ),
    ]
