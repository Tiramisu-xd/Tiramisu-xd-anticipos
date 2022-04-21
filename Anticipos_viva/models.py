from django.db import models

# Create your models here.
class Info_solicitante(models.Model):

    id= models.AutoField(primary_key=True)

    Fecha_diligenciamiento=models.DateField(auto_now = True, auto_now_add= False)

    Nombre_completo=models.CharField(max_length=50, blank= False, null= False)

    Fecha_nacimiento=models.DateField()

    Tipo_cc=models.CharField(max_length=50, blank= False, null= False)
    
    Numero_cc=models.IntegerField()
    
    Area_trabajo=models.CharField(max_length=50, blank= False, null= False)
    
    Compania=models.CharField(max_length=50, blank= False, null= False)
    
    Email_personal=models.CharField(max_length=100, blank= False, null= False)
    
    Numero_cel=models.IntegerField()
    
    Tipo_colaborador=models.CharField(max_length=50, blank= False, null= False)
    
    Evento_aog=models.CharField(max_length=10, blank= False, null= False)
    
    Entrenamiento_crew=models.CharField(max_length=10, blank= False, null= False)

    # Class Meta: Para definir el nombre del modelo en el sitio de administrador.

    class Meta:

        verbose_name = 'Info_solicitante'

        verbose_name_plural = 'Info_solicitantes'

    # Def: Para definir el nombre del modelo en el sitio de administrador.

    def __str__(self):

        return self.puesto_reservadpo

class Registro_ida(models.Model):

    id= models.AutoField(primary_key=True)

    Origen=models.CharField(max_length=60, blank= False, null= False)

    Destino=models.CharField(max_length=60, blank= False, null= False)

    Fecha_vuelo=models.DateField()
    
    Hora_vuelo=models.TimeField
    
     # Class Meta: Para definir el nombre del modelo en el sitio de administrador.

    class Meta:

        verbose_name = 'Registro_ida'

        verbose_name_plural = 'Registros_ida'

    # Def: Para definir el nombre del modelo en el sitio de administrador.

    def __str__(self):

        return self.puesto_reservadpo
        
class Registro_regreso(models.Model):

    id= models.AutoField(primary_key=True)

    Origen=models.CharField(max_length=60, blank= False, null= False)

    Destino=models.CharField(max_length=60, blank= False, null= False)

    Fecha_vuelo=models.DateField()
    
    Hora_vuelo=models.TimeField()
    
     # Class Meta: Para definir el nombre del modelo en el sitio de administrador.

    class Meta:

        verbose_name = 'Registro_regreso'

        verbose_name_plural = 'Registros_regreso'

    # Def: Para definir el nombre del modelo en el sitio de administrador.

    def __str__(self):

        return self.puesto_reservadpo

class Datos_viaje(models.Model):

    id= models.AutoField(primary_key=True)

    Registro_ida_id=models.ForeignKey(Registro_ida, on_delete= models.CASCADE)

    Registro_regreso_id=models.ForeignKey(Registro_regreso, on_delete= models.CASCADE)

    Alojamiento=models.CharField(max_length=10, blank= False, null= False)

    Alimentacion=models.CharField(max_length=10, blank= False, null= False)

    Tipo_moneda=models.CharField(max_length=20, blank= False, null= False)

    Transporte=models.CharField(max_length=10, blank= False, null= False)
    
    Renta_vehiculo=models.CharField(max_length=10, blank= False, null= False)
    
    Comparte_habitacion=models.CharField(max_length=10, blank= False, null= False)
    
    Nombre_companero=models.CharField(max_length=50, blank= False, null= False)
    
    Finalidad_viaje=models.CharField(max_length=100, blank= False, null= False)
    
    Observaciones=models.CharField(max_length=100, blank= False, null= False)

     # Class Meta: Para definir el nombre del modelo en el sitio de administrador.

    class Meta:

        verbose_name = 'Dato_viaje'

        verbose_name_plural = 'Datos_vije'

    # Def: Para definir el nombre del modelo en el sitio de administrador.

    def __str__(self):

        return self.puesto_reservadpo

class Anticipos(models.Model):

    id= models.AutoField(primary_key=True)

    Datos_viaje_id=models.ForeignKey(Datos_viaje, on_delete= models.CASCADE)

    tipoMoneda=models.CharField(max_length=10, blank= False, null= False)

    Valor_dia=models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)

    Numero_dias=models.IntegerField()
    
    Total_gasto=models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)

     # Class Meta: Para definir el nombre del modelo en el sitio de administrador.

    class Meta:

        verbose_name = 'Anticipo'

        verbose_name_plural = 'Anticipos'

    # Def: Para definir el nombre del modelo en el sitio de administrador.

    def __str__(self):

        return self.puesto_reservadpo




