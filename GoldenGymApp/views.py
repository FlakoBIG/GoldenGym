from django.shortcuts import render, redirect, get_object_or_404
from GoldenGymApp.models import Cliente,Encargado,Plan
from GoldenGymApp.forms import ClienteForm,EncargadoForm,PlanForm
from django.urls import reverse
from django.http import HttpResponseRedirect

def gestion_clientes(request):
    # Si el método es POST, es porque se envió el formulario
    if request.method == 'POST':
        if 'cliente_id' in request.POST:
            # Editar cliente existente
            cliente = get_object_or_404(Cliente, id=request.POST['cliente_id'])
            form = ClienteForm(request.POST, instance=cliente)
        else:
            # Crear nuevo cliente
            form = ClienteForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('gestion_clientes')  # Redirige después de guardar para evitar re-envío del formulario

    else:
        form = ClienteForm()  # Formulario vacío para crear un nuevo cliente

    # Obtener la lista de todos los clientes
    clientes = Cliente.objects.all()
    return render(request, 'GoldenGymApp/gestion_cliente.html', {'form': form, 'clientes': clientes})

def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.delete()
    return HttpResponseRedirect(reverse('gestion_clientes'))


def gestion_encargados(request):
    if request.method == 'POST':
        if 'encargado_id' in request.POST:
            # Editar encargado existente
            encargado = get_object_or_404(Encargado, id=request.POST['encargado_id'])
            form = EncargadoForm(request.POST, instance=encargado)
        else:
            # Crear nuevo encargado
            form = EncargadoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('gestion_encargados')  # Redirige para evitar reenvíos de formulario

    else:
        form = EncargadoForm()  # Formulario vacío para crear un nuevo encargado

    # Obtener la lista de todos los encargados
    encargados = Encargado.objects.all()
    return render(request, 'GoldenGymApp/gestion_encargado.html', {'form': form, 'encargados': encargados})

# Vista para eliminar encargado
def eliminar_encargado(request, encargado_id):
    encargado = get_object_or_404(Encargado, id=encargado_id)
    encargado.delete()
    return HttpResponseRedirect(reverse('gestion_encargados'))


def validar_ingreso(request):
    mensaje = None

    if request.method == "POST":
        rut_ingresado = request.POST.get("rut")

        # Buscar al cliente en la base de datos por su RUT
        try:
            cliente = Cliente.objects.get(rut=rut_ingresado)
            # Verificar si tiene una suscripción activa (esto dependerá de tu lógica de negocio)
            if cliente.suscripcion_activa:  # Asegúrate de que tienes este campo en tu modelo
                mensaje = "Ingreso permitido. Bienvenido al gimnasio."
            else:
                mensaje = "Acceso denegado. No tiene una suscripción activa."
        except Cliente.DoesNotExist:
            mensaje = "RUT no registrado. Verifique su información."

    return render(request, "GoldenGymApp/validar_ingreso.html", {"mensaje": mensaje})

def gestion_planes(request):
    if request.method == 'POST':
        if 'plan_id' in request.POST:
            # Editar plan existente
            plan = get_object_or_404(Plan, id=request.POST['plan_id'])
            form = PlanForm(request.POST, instance=plan)
        else:
            # Crear nuevo plan
            form = PlanForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar los cambios en la base de datos
            return redirect('gestion_planes')  

    else:
        form = PlanForm()  # Crear un formulario vacío para crear un nuevo plan

    # Obtener la lista de todos los planes
    planes = Plan.objects.all()
    return render(request, 'GoldenGymApp/gestion_planes.html', {'form': form, 'planes': planes})

def eliminar_plan(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)
    plan.delete()
    return HttpResponseRedirect(reverse('gestion_planes'))

def editar_plan(request, plan_id):
    # Obtener el plan que se está editando
    plan = get_object_or_404(Plan, id=plan_id)

    # Si el formulario es enviado
    if request.method == 'POST':
        # Vinculamos el formulario con los datos de la instancia del plan
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            # Guardamos los cambios
            form.save()
            return redirect('gestion_planes')  # Redirigir a la lista de planes o a otra página
    else:
        # Si es un GET, pasamos los datos del plan al formulario
        form = PlanForm(instance=plan)

    # Pasamos el formulario a la plantilla
    return render(request, 'GoldenGymApp/gestion_planes.html', {'form': form, 'plan': plan})

def registro_usuario(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir o hacer algo después de guardar
    return render(request, 'GoldenGymApp/registro.html', {'form': form})