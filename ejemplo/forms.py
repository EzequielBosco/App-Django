from django import forms
from ejemplo.models import Persona

class PersonaForm(forms.ModelForm):

    fecha_de_nacimiento=forms.DateField(label="Fecha de nacimiento", input_formats=["%d/%m/%Y"],
    #widget es un tip para que el usuario sepa como ingresar la fecha
    widget=forms.TextInput(attrs={"placeholder":"07/10/1999"}))

    class Meta:
        model = Persona
        fields = ["nombre", "apellido", "fecha_de_nacimiento"]