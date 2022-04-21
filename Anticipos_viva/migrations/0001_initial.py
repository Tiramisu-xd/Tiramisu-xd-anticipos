# Generated by Django 4.0.4 on 2022-04-12 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info_solicitante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Fecha_diligenciamiento', models.DateField(auto_now=True)),
                ('Nombre_completo', models.CharField(max_length=50)),
                ('Fecha_nacimiento', models.DateField()),
                ('Tipo_cc', models.CharField(max_length=50)),
                ('Numero_cc', models.IntegerField()),
                ('Area_trabajo', models.CharField(max_length=50)),
                ('Compania', models.CharField(max_length=50)),
                ('Email_personal', models.CharField(max_length=100)),
                ('Numero_cel', models.IntegerField()),
                ('Tipo_colaborador', models.CharField(max_length=50)),
                ('Evento_aog', models.CharField(max_length=10)),
                ('Entrenamiento_crew', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Info_solicitante',
                'verbose_name_plural': 'Info_solicitantes',
            },
        ),
        migrations.CreateModel(
            name='Registro_ida',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Oroigen', models.CharField(max_length=60)),
                ('Destino', models.CharField(max_length=60)),
                ('Fecha_vuelo', models.DateField()),
            ],
            options={
                'verbose_name': 'Registro_ida',
                'verbose_name_plural': 'Registros_ida',
            },
        ),
        migrations.CreateModel(
            name='Registro_regreso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Oroigen', models.CharField(max_length=60)),
                ('Destino', models.CharField(max_length=60)),
                ('Fecha_vuelo', models.DateField()),
                ('Hora_vuelo', models.TimeField()),
            ],
            options={
                'verbose_name': 'Registro_regreso',
                'verbose_name_plural': 'Registros_regreso',
            },
        ),
        migrations.CreateModel(
            name='Datos_viaje',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Alojamiento', models.CharField(max_length=10)),
                ('Alimentacion', models.CharField(max_length=10)),
                ('Transporte', models.CharField(max_length=10)),
                ('Renta_vehiculo', models.CharField(max_length=10)),
                ('Comparte_habitacion', models.CharField(max_length=10)),
                ('Nombre_companero', models.CharField(max_length=50)),
                ('Finalidad_viaje', models.CharField(max_length=100)),
                ('Observaciones', models.CharField(max_length=100)),
                ('Registro_ida_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Anticipos_viva.registro_ida')),
                ('Registro_regreso_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Anticipos_viva.registro_regreso')),
            ],
            options={
                'verbose_name': 'Dato_viaje',
                'verbose_name_plural': 'Datos_vije',
            },
        ),
        migrations.CreateModel(
            name='Anticipos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Tipo_moneda', models.CharField(max_length=20)),
                ('Valor_dia', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
                ('Numero_dias', models.IntegerField()),
                ('Total_gasto', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
                ('Datos_viaje_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Anticipos_viva.datos_viaje')),
            ],
            options={
                'verbose_name': 'Anticipo',
                'verbose_name_plural': 'Anticipos',
            },
        ),
    ]