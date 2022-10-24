from django.shortcuts import get_object_or_404, render
from django.views import View
from ejemplo.models import Persona
from ejemplo.forms import PersonaForm

class ListarPersonas(View):
    template_name = "ejemplo/lista_de_personas.html"

    def get(self, request):
        personas = Persona.objects.all()
        return render(request, self.template_name, {"personas":personas})

class CargarPersonas(View):
    template_name = "ejemplo/carga_de_personas.html"
    form_class = PersonaForm
    initial = {"nombre":"","apellido":"","fecha_de_nacimiento":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form":form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form":form})

class ActualizarPersona(View):
    template_name = "ejemplo/actualizar_persona.html"
    success_template = "ejemplo/exito.html"
    form_class = PersonaForm
    initial = {"nombre":"","apellido":"","fecha_de_nacimiento":""}

    def get(self, request, pk):
        persona = get_object_or_404(Persona, pk=pk)
        form = self.form_class(instance=persona)
        return render(request, self.template_name, {"form":form, "pk":pk})

    def post(self, request, pk):
        persona = get_object_or_404(Persona, pk=pk)
        form = self.form_class(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)
        return render(request, self.success_template)