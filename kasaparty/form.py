from django import forms
from django.forms import ModelForm
from kasaparty.models.cotizacion import Cotizacion


class CotizacionForm(ModelForm):
    class Meta:
        model = Cotizacion
        fields = "__all__"
        widgets = {
            "fecha_evento": forms.DateInput(attrs={"type": "date"}),
        }
