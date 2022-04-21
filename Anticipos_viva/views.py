from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from pickle import FALSE
from Anticipos_viva.models import Info_solicitante,Registro_ida,Registro_regreso,Datos_viaje,Anticipos

# Create your views here.

def inicio_de_sesion(request):

    if request.method=='POST':

        fecha_dili=request.POST['fecha_dili']
        evento_aog=request.POST['evento_aog']
        t_c=request.POST['t_c']
        crew=request.POST['crew']
        compania=request.POST['Compania']
        name=request.POST['name']
        Tipo_Id=request.POST['Tipo_Id']
        numero_cc=request.POST['numero_cc']
        nacimiento=request.POST['nacimiento']
        correo=request.POST['correo']
        cumero_cel=request.POST['cumero_cel']
        area_loboral=request.POST['area_loboral']
        ceco=request.POST['ceco']
        descripcion=request.POST['descripcion']
        observaciones=request.POST['observaciones']
        tipoViaje=request.POST['tipoViaje']
        alojamiento=request.POST['alojamiento']
        alimentacion=request.POST['alimentacion']
        solicitud_trans=request.POST['solicitud_trans']
        renta_vh=request.POST['renta_vh']
        xx2=request.POST['xx2']
        name_compi=request.POST['name_compi']
        origenIda=request.POST['origenIda']
        destinoIda=request.POST['destinoIda']
        fechaIda=request.POST['fechaIda']
        hora_vueloIda=request.POST['hora_vueloIda']
        origenRegreso=request.POST['origenRegreso']
        destinoRegreso=request.POST['destinoRegreso']
        fechaRegreso=request.POST['fechaRegreso']
        hora_vueloRegreso=request.POST['hora_vueloRegreso']
        lolsito=request.POST['lolsito']

        Info_solicitante(Fecha_diligenciamiento=fecha_dili, Nombre_completo=name,
        Fecha_nacimiento=nacimiento, Tipo_cc=Tipo_Id, Numero_cc=numero_cc, Area_trabajo=area_loboral,
        Compania=Compania, Email_personal=correo, Numero_cel=cumero_cel, Tipo_colaborador=t_c,
        Evento_aog=evento_aog, Entrenamiento_crew=crew).save()

        Registro_ida(Origen=origenIda, Destino=destinoIda, Fecha_vuelo=fechaIda, Hora_vuelo=hora_vueloIda).save()

        Registro_regreso(Origen=origenRegreso, Destino=destinoRegreso, Fecha_vuelo=fechaRegreso, Hora_vuelo=hora_vueloRegreso).save()

        Datos_viaje(Alojamiento=alojamiento, Alimentacion=alimentacion, Tipo_moneda=tipoViaje, Transporte=solicitud_trans, 
        Renta_vehiculo=renta_vh, Comparte_habitacion=xx2, Nombre_companero=name_compi, Finalidad_viaje=descripcion, Observaciones=observaciones).save()
        
        Anticipos(tipoMoneda=lolsito, Valor_dia=copsito).save()

        return render(request,'paginas/inicio_de_sesion.html')

    else:

        return render(request,'paginas/inicio_de_sesion.html')

def item_cop(request):
    return render(request,'paginas/item_cop.html')

def item_pen(request):
    return render(request,'paginas/item_pen.html')

def item_usd(request):
    return render(request,'paginas/item_usd.html')