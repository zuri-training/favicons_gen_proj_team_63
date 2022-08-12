# Generated by Django 4.0.6 on 2022-08-11 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('favigen', '0002_remove_favicon_url_favicon_favicon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favicon',
            name='favicon',
        ),
        migrations.RemoveField(
            model_name='favicon',
            name='favourite',
        ),
        migrations.RemoveField(
            model_name='favicon',
            name='file_size',
        ),
        migrations.RemoveField(
            model_name='favicon',
            name='file_type',
        ),
        migrations.RemoveField(
            model_name='favicon',
            name='new_file_name',
        ),
        migrations.RemoveField(
            model_name='favicon',
            name='old_file_name',
        ),
        migrations.RemoveField(
            model_name='favicon',
            name='uploaded_at',
        ),
        migrations.RemoveField(
            model_name='favicon',
            name='uploaded_by',
        ),
        migrations.AddField(
            model_name='favicon',
            name='embed_link',
            field=models.TextField(null=True),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_image', models.ImageField(blank=True, null=True, upload_to='team/')),
                ('old_file_name', models.CharField(max_length=256)),
                ('new_file_name', models.CharField(max_length=256)),
                ('file_type', models.CharField(default=None, max_length=10)),
                ('file_size', models.IntegerField(default=0)),
                ('favourite', models.BooleanField(default=False)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='favicon',
            name='image',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='favigen.image'),
        ),
    ]