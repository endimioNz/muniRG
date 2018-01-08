from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.utils import timezone
class EmprendedorForm(forms.ModelForm):
	
	fecha = forms.DateField(widget=forms.SelectDateWidget(years=range(2003, 2100)), initial=timezone.now()
)
	class Meta:
		model = Emprendedor
		fields = [
			"nombre",
			"apellido",
			"identificacion",
			"numero",
			"direccion",
			"telefono",
			"estadocivil",
			"profesion",
			"cuil",
			"modeladodenegocios",
			"ventas", 
			"marketing",
			"disenodemarca",
			"marcacolectiva",
			"rentabilidad",
			"costos",
			"entrenamientointensivo",
			"culturaemprendedora",
			"desarrollodeproducto",
			"plandenegocios",
			"innovacionycreatividad",
			"liderazgo",
			"trabajoenequipo",
			"comunicacionefectiva",
			"concursosyconvocatorias",
			"tradicionalynotradicional",
			"marketingdigital",
			"redessociales",
			"tiendaonline",
			"cooperativismo", 
			"asociativismo",
			"personajuridica",
			"mujeremprendedora",
			"trabajoydiscapacidad",
			'usuario',
			"fecha",
			
		]

class ExpedienteForm(forms.ModelForm):
	fecha = forms.DateField(widget=forms.SelectDateWidget(years=range(2003, 2100)), initial=timezone.now()
)
	class Meta:
		model = Expediente
		fields = [
			'emprendedor',
			'rubro',
			'monto',
			'asiento',
			'texto',
			'fecha',
			'usuario',
		]
