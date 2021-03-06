# Generated by Django 2.0.8 on 2018-10-30 01:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateTimeField()),
                ('checkout', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('balance_due', models.IntegerField(default=0)),
                ('is_staff', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year_in_school', models.CharField(choices=[('K', 'Kindergarten'), ('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth'), ('5', 'Fifth'), ('6', 'Sixth'), ('7', 'Seventh'), ('8', 'Eighth')], default='K', max_length=1)),
                ('id_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('student_id', models.PositiveIntegerField()),
                ('is_signedin', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='parent',
            name='students',
            field=models.ManyToManyField(blank=True, to='afterschool.Student'),
        ),
        migrations.AddField(
            model_name='parent',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dailyinfo',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily', to='afterschool.Student'),
        ),
    ]
