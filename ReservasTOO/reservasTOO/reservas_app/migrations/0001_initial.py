# Generated by Django 2.0.5 on 2021-11-02 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('codigo_asig', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_asig', models.CharField(max_length=20)),
                ('uv', models.IntegerField()),
                ('tipo', models.CharField(max_length=20)),
                ('prerrequisito', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('codigo', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre_carrera', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id_director', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre_d', models.CharField(max_length=60)),
                ('apellido_d', models.CharField(max_length=60)),
                ('dui_di', models.CharField(max_length=9)),
                ('fech_nac', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('codigo_doc', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('dui_do', models.CharField(max_length=9)),
                ('nombre_do', models.CharField(max_length=50)),
                ('apellido_do', models.CharField(max_length=50)),
                ('fech_nac_do', models.DateField()),
                ('estado', models.BooleanField()),
                ('email', models.EmailField(max_length=254)),
                ('contrasenha', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id_edificio', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nom_edi', models.CharField(max_length=20)),
                ('ubicacion', models.CharField(max_length=50)),
                ('cant_locales', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('cod_escuela', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre_escuela', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id_local', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre_local', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Pensum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pensum', models.CharField(max_length=10)),
                ('nombre_pensum', models.CharField(max_length=10)),
                ('anho', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='REserva',
            fields=[
                ('id_res', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('estado', models.BooleanField()),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
        ),
    ]
