# Generated by Django 4.2 on 2023-07-10 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_type',
            field=models.CharField(choices=[('text', 'テキスト'), ('checkbox', 'チェックボックス'), ('file', 'ファイル')], default='text', max_length=20),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CheckboxOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('append_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.task')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='checkboxes',
            field=models.ManyToManyField(blank=True, to='management.checkboxoption'),
        ),
    ]