from django.shortcuts import render
from django.views import View
from ejemplo.models import Persona

class ListarPersonas(View):
    template_name = "ejemplo/lista_de_personas.html"

    def get(self, request):
        personas = Persona.objects.all()
        return render(request, self.template_name, {"personas":personas})
