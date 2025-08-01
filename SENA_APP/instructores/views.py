from django.shortcuts import HttpResponse
from django.template import loader
from .models import Instructor

# Create your views here.

app_name = 'instructores'

def instructores(request):
    lista_instructores = Instructor.objects.all().order_by('nombre', 'apellido')
    template = loader.get_template('lista_instructores.html')
    context = {
        'lista_instructores': lista_instructores,
        'total_instructores': lista_instructores.count(),
    }
    return HttpResponse(template.render(context, request))