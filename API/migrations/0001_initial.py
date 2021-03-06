# Generated by Django 3.0.1 on 2019-12-21 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, max_length=20, null=True)),
                ('title', models.CharField(max_length=200)),
                ('ages', models.CharField(max_length=200)),
                ('patientType', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionnaireContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionText', models.CharField(max_length=500)),
                ('answerType', models.CharField(max_length=100)),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaireContent', to='API.Questionnaire')),
            ],
        ),
    ]
