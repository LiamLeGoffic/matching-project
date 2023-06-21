# Generated by Django 4.2 on 2023-06-15 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(choices=[('1', 'Basic'), ('2', 'Intermediate'), ('3', 'Expert')])),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('office', models.CharField(max_length=10)),
                ('role', models.IntegerField(choices=[('RM', 'Ressource Manager'), ('RH', 'Human Ressource'), ('Com', 'Commercial')])),
            ],
        ),
        migrations.DeleteModel(
            name='Commercial',
        ),
        migrations.DeleteModel(
            name='Competence',
        ),
        migrations.DeleteModel(
            name='RH',
        ),
        migrations.DeleteModel(
            name='RM',
        ),
        migrations.RemoveField(
            model_name='consultant',
            name='idConsultant',
        ),
        migrations.RemoveField(
            model_name='mission',
            name='idMission',
        ),
        migrations.AddField(
            model_name='consultant',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mission',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mission',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requirement',
            name='mission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matching.mission'),
        ),
        migrations.AddField(
            model_name='requirement',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matching.skill'),
        ),
        migrations.AddField(
            model_name='consultant',
            name='skills',
            field=models.ManyToManyField(to='matching.skill'),
        ),
        migrations.AddField(
            model_name='mission',
            name='skills',
            field=models.ManyToManyField(through='matching.Requirement', to='matching.skill'),
        ),
        migrations.AddField(
            model_name='mission',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='matching.user'),
        ),
    ]