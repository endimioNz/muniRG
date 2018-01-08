from django.db import models
from django.core.urlresolvers import reverse 
from multiselectfield import MultiSelectField
# Create your models here.

class Emprendedor(models.Model):
	nombre = models.CharField("Nombre", max_length=30, null=False, blank=False)
	apellido = models.CharField("Apellido", max_length=30, null=False, blank=False)
	tipo_de_identificacion = (
		('DNI', 'DNI (Documento Nacional de Identidad)'),
		('CI', 'CI (Cedula de identidad)'),
		('LC', 'LC (Libreta de enrolamiento)'),
		)
	identificacion = models.CharField("Tipo de Identificacion", max_length=3, choices=tipo_de_identificacion, null=False, blank=False, default='DNI')
	numero = models.CharField(max_length=8, null=False, blank=False, unique=True)
	direccion = models.CharField("Direccion", max_length=30, null=False, blank=False)
	telefono = models.CharField("Telefono", max_length=20, null=False, blank=False)
	tipo_de_estadocivil = (
	    ('SOLTERO/A', 'SOLTERO/A'),
	    ('COMPROMETIDO/A', 'COMPROMETIDO/A'),
	    ('CASADO/A', 'CASADO/A'),
	    ('DIVORCIADO/A', 'DIVORCIADO/A'),
	    ('VIUDO/A', 'VIUDO/A'),
	    ('CONCUBINATO', 'CONCUBINATO'),
		)	
	estadocivil = models.CharField("Estado Civil", max_length=14, choices=tipo_de_estadocivil, null=False, blank=False)
	profesion = models.CharField("Profesion", max_length=30, null=False, blank=False)
	cuil = models.CharField("CUIL o CUIT", max_length=13, null=False, blank=False)
	fecha = models.DateField("Fecha de carga: ", auto_now=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	usuario = models.CharField("Responsable", max_length=30, null=False, blank=False)
	modeladodenegocios = models.BooleanField(default=False)
	ventas = models.BooleanField(default=False)
	marketing = models.BooleanField(default=False)
	disenodemarca = models.BooleanField(default=False)
	marcacolectiva = models.BooleanField(default=False) 
	rentabilidad = models.BooleanField(default=False)
	costos = models.BooleanField(default=False)
	entrenamientointensivo = models.BooleanField(default=False)
	culturaemprendedora = models.BooleanField(default=False)
	desarrollodeproducto = models.BooleanField(default=False)
	plandenegocios = models.BooleanField(default=False)
	innovacionycreatividad = models.BooleanField(default=False)
	liderazgo = models.BooleanField(default=False)
	trabajoenequipo = models.BooleanField(default=False)
	comunicacionefectiva = models.BooleanField(default=False)
	concursosyconvocatorias = models.BooleanField(default=False)
	tradicionalynotradicional = models.BooleanField(default=False)
	marketingdigital = models.BooleanField(default=False)
	redessociales = models.BooleanField(default=False)
	tiendaonline = models.BooleanField(default=False)
	cooperativismo = models.BooleanField(default=False)
	asociativismo = models.BooleanField(default=False)
	personajuridica = models.BooleanField(default=False)
	mujeremprendedora = models.BooleanField(default=False)
	trabajoydiscapacidad = models.BooleanField(default=False)

	def __str__(self):
		return ('%s, %s, %s: %s')%(self.nombre, self.apellido, self.identificacion, self.numero)	
	def save(self, force_insert=False, force_update=False):
		self.nombre = self.nombre.upper()
		self.apellido = self.apellido.upper()
		self.numero = self.numero.upper()
		self.direccion = self.direccion.upper()
		self.estadocivil = self.estadocivil.upper()
		self.profesion = self.profesion.upper()
		self.cuil = self.cuil.upper()
		self.usuario = self.usuario.upper()
		super(Emprendedor, self).save(force_insert, force_update)

	def get_absolute_url(self):
		return reverse("expediente:v_emprendedor", kwargs={"id": self.numero}) #keyword args



class Expediente(models.Model):
	emprendedor = models.ForeignKey(Emprendedor)
	tipo_de_asiento = (
		('ASESORAMIENTO', 'ASESORAMIENTO'),
		('OTORGAMIENTO: CREDITO', 'OTORGAMIENTO: CREDITO'),
		('OTORGAMIENTO: SUBSIDIO', 'OTORGAMIENTO: SUBSIDIO'),
		('SEGUIMIENTO: CREDITO', 'SEGUIMIENTO: CREDITO'),
		('SEGUIMIENTO: SUBSIDIO', 'SEGUIMIENTO: SUBSIDIO'),
		('FINANCIAMIENTO: PROPIO', 'FINANCIAMIENTO: PROPIO'),
		('FINANCIAMIENTO: TERCERO', 'FINANCIAMIENTO: TERCERO'),
		('FERIA: DESAFIO PRODUCIR', 'FERIA: DESAFIO PRODUCIR'),
		('FERIA: PASEO ARTESANO', 'FERIA: PASEO ARTESANO'),
		('FERIA: OTROS', 'FERIA: OTROS'),
		('CAPACITACION', 'CAPACITACION'),
		('NO APROBADO', 'NO APROBADO'),
		('CREDITO: CANCELADO', 'CREDITO: CANCELADO'),
		('SUBSIDIO: CANCELADO', 'SUBSIDIO: CANCELADO'),
		('OBSERVACIONES', 'OBSERVACIONES')
		)
	asiento = models.CharField("Asiento", max_length=25, choices=tipo_de_asiento, null=False, blank=False)	
	monto = models.IntegerField(default=0)
	tipo_de_rubro = (
		('ARTESANO','ARTESANO'),
		('DISEÑO','DISEÑO'),
		('GASTRONOMICO','GASTRONOMICO'),
		('HORTICOLA','HORTICOLA'),
		('SERVICIOS','SERVICIOS'),
		('SUSTENTABILIDAD','SUSTENTABILIDAD'),
		('TAXI/REMIS','TAXI/REMIS'),
		('TECNOLOGIA APROPIADA','TECNOLOGIA APROPIADA'),
		('TECNOLOGICO','TECNOLOGICO'),
		)
	rubro = models.CharField("Rubro", max_length=20, choices=tipo_de_rubro, null=False, blank=False)	
	texto = models.TextField("Informacion del expediente: ", null=False, blank=False)
	fecha = models.DateField("Fecha de carga: ", auto_now=False)	
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	usuario = models.CharField("Responsable", max_length=30, null=False, blank=False)
	activo = models.BooleanField(default=True)	

	def __str__(self):
		return ('Emprendedor: %s, %s, Cargado: %s ')%(self.emprendedor, self.asiento, self.fecha)

	def save(self, force_insert=False, force_update=False):
		self.texto = self.texto.upper()
		self.usuario = self.usuario.upper()
		super(Expediente, self).save(force_insert, force_update)
