from django.http import HttpResponse
from django.template import loader
from .models import Programa

# Create your views here.

def programas(request):
    lista_programas = Programa.objects.all()
    template = loader.get_template('lista_programas.html')
    context = {
    'lista_programas': lista_programas,
    'total_programas': lista_programas.count(),
    'estado_actual': Programa.objects.filter(estado='ACT').count(),
    }
    return HttpResponse(template.render(context, request))
    