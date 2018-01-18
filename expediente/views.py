from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse
from .models import *
from .forms import *
from django.core import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.forms import  UserCreationForm
import json

# inicio reportlab
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm, inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.colors import pink, green, brown, white, black, magenta, red
import time
from reportlab.lib.enums import *
from reportlab.lib.pagesizes import letter, A4,landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, TableStyle, Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from io import BytesIO

from django.views.generic import ListView
from reportlab.lib.utils import ImageReader

PAGE_HEIGHT=A4[1]
PAGE_WIDTH=A4[0]
styles = getSampleStyleSheet()

pdfmetrics.registerFont(TTFont('Existence-Light', 'static/fonts/Existence-Light.ttf'))
pdfmetrics.registerFont(TTFont('Ubuntu-B', 'static/fonts/ubuntu-font-family-0.83/Ubuntu-B.ttf'))
pdfmetrics.registerFont(TTFont('Ubuntu-L', 'static/fonts/ubuntu-font-family-0.83/Ubuntu-L.ttf'))
pdfmetrics.registerFont(TTFont('Ubuntu-M', 'static/fonts/ubuntu-font-family-0.83/Ubuntu-M.ttf'))
pdfmetrics.registerFont(TTFont('Ubuntu-C', 'static/fonts/ubuntu-font-family-0.83/Ubuntu-C.ttf'))
pdfmetrics.registerFont(TTFont('Ubuntu-R', 'static/fonts/ubuntu-font-family-0.83/Ubuntu-R.ttf'))

styles.add(ParagraphStyle(name='tit2', alignment=TA_CENTER, fontName = "Ubuntu-M", fontSize = 14))
styles.add(ParagraphStyle(name='tit1', alignment=TA_CENTER, fontName = "Existence-Light", fontSize = 16))
styles.add(ParagraphStyle(name='tit3', alignment=TA_LEFT, fontName = "Ubuntu-L", fontSize = 12))
styles.add(ParagraphStyle(name='tablas', alignment=TA_LEFT, fontName = "Ubuntu-C", fontSize = 11))
styles.add(ParagraphStyle(name='textos', alignment=TA_LEFT, fontName = "Ubuntu-R", fontSize = 10))

tit1 = styles["tit1"]
tit2 = styles["tit2"]
tit3 = styles["tit3"]
tablas = styles["tablas"]
textos = styles["textos"]

LIST_STYLE = TableStyle(
	[('GRID', (0,0), (17, -1), 1, colors.black),
	('BACKGROUND', (0,0), (-1, 0), colors.lightgrey),
	('FONT', (0,0), (-1, -1), 'Ubuntu-C', 10)]
)
# fin reportlab

# Create your views here.
def pdf(request, id=None):
	if not request.user.is_authenticated():
		raise Http404
	instance = get_object_or_404(Emprendedor, numero=id)
	if(instance):
		expediente_listado = Expediente.objects.all().filter(emprendedor=instance).order_by("fecha")
		
		#inicio reportlab
		response = HttpResponse(content_type='application/pdf')
		pdf_name = "expediente_%d.pdf" %instance.id
		response['Content-Disposition'] = 'filename=%s; pagesize=A4' %pdf_name
		buff = BytesIO()
		title = "Informe_%d" %instance.id
		
		Story = [Spacer(1, 0)]
		style = styles["textos"]

		def myFirstPage(canvas, doc):
			canvas.saveState()
			canvas.setFont('Ubuntu-R', 8)
			canvas.drawString(inch, A4[1] - 50, "Dirección de Desarrollo Local -  Secretaría de Producción y Ambiente.")
			canvas.line(inch, A4[1] - 60, A4[0] - 65, A4[1] - 60)
			# numeracion de pagina
			canvas.setFont('Ubuntu-R', 8)
			canvas.drawString(inch, 0.75 * inch, "Pagina %d / Río Grande, Tierra del Fuego" %(doc.page))
			canvas.restoreState()

		def cuerpo(canvas):
			titulo = Paragraph("REPORTE DEL EXPEDIENTE", tit1) 
			Story.append(titulo)
			Story.append(Spacer(1, 30))

			persona = Paragraph("""<b>Nombre y Apellido: </b>"""+instance.apellido+""", """+instance.nombre+"""<br/><b>"""+instance.identificacion+""": </b>"""+instance.numero+"""<br/><b>Direccion: </b>"""+instance.direccion
				+"""<br/><b>Estado Civil: </b>"""+instance.estadocivil+"""<br/><b>Profesión: </b>"""+instance.profesion, styles["Normal"]) 
			Story.append(persona)
			Story.append(Spacer(1, 12))

			for e in expediente_listado:
				if e.activo and e.asiento != "OBSERVACIONES":
					if e.asiento == "OTORGAMIENTO: CREDITO" or e.asiento == "OTORGAMIENTO: SUBSIDIO":
						subt = Paragraph("""<b>FECHA: </b>"""+str(e.fecha)+""", <b> SE INICIÓ UN ASIENTO DE: </b>"""+e.asiento+"""<b> CON UN MONTO TOTAL DE: </b>$"""+str(e.monto)
							+"""<b> Y SE REALIZÓ EL SIGUIENTE INFORME: </b>""", styles["Normal"]) 
						Story.append(subt)
						Story.append(Spacer(1, 12))

						tex = Paragraph(e.texto, style) 
						Story.append(tex)
						Story.append(Spacer(1, 12))
					else:
						subt = Paragraph("""<b>FECHA: </b>"""+str(e.fecha)+""", <b> SE INICIÓ UN ASIENTO DE: </b>"""+e.asiento+"""<b> Y SE REALIZÓ EL SIGUIENTE INFORME: </b>""", styles["Normal"]) 
						Story.append(subt)
						Story.append(Spacer(1, 12))

						tex = Paragraph(e.texto, style) 
						Story.append(tex)
						Story.append(Spacer(1, 12))

			return Story

		Story = cuerpo(canvas)
		doc = SimpleDocTemplate(buff, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=75)
		#Construimos el documento a partir de los argumentos definidos
		doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myFirstPage)
		response.write(buff.getvalue())
		buff.close()
		return response


	# 	context = {
	# 		"emprendedor": instance,
	# 		"expediente": expediente_listado,
	# 	}
	# 	return render(request, "pdf.html", context)
	
	# else:
	# 	raise Http404
def listados_pdf(request, id=None):
	if not request.user.is_authenticated():
		raise Http404
	instance = []
	if id == 'modeladodenegocios':
		instance = Emprendedor.objects.all().filter(modeladodenegocios=False)
	elif id == 'ventas':
		instance = Emprendedor.objects.all().filter(ventas=False)

	elif id == 'marketing':
		instance = Emprendedor.objects.all().filter(marketing=False)

	elif id == 'disenodemarca':
		instance = Emprendedor.objects.all().filter(disenodemarca=False)

	elif id == 'marcacolectiva':
		instance = Emprendedor.objects.all().filter(marcacolectiva=False)

	elif id == 'rentabilidad':
		instance = Emprendedor.objects.all().filter(rentabilidad=False)

	elif id == 'costos':
		instance = Emprendedor.objects.all().filter(costos=False)

	elif id == 'entrenamientointensivo':
		instance = Emprendedor.objects.all().filter(entrenamientointensivo=False)

	elif id == 'culturaemprendedora':
		instance = Emprendedor.objects.all().filter(culturaemprendedora=False)

	elif id == 'desarrollodeproducto':
		instance = Emprendedor.objects.all().filter(desarrollodeproducto=False)

	elif id == 'plandenegocios':
		instance = Emprendedor.objects.all().filter(plandenegocios=False)

	elif id == 'innovacionycreatividad':
		instance = Emprendedor.objects.all().filter(innovacionycreatividad=False)

	elif id == 'liderazgo':
		instance = Emprendedor.objects.all().filter(liderazgo=False)

	elif id == 'trabajoenequipo':
		instance = Emprendedor.objects.all().filter(trabajoenequipo=False)

	elif id == 'comunicacionefectiva':
		instance = Emprendedor.objects.all().filter(comunicacionefectiva=False)

	elif id == 'concursosyconvocatorias':
		instance = Emprendedor.objects.all().filter(concursosyconvocatorias=False)

	elif id == 'tradicionalynotradicional':
		instance = Emprendedor.objects.all().filter(tradicionalynotradicional=False)

	elif id == 'marketingdigital':
		instance = Emprendedor.objects.all().filter(marketingdigital=False)

	elif id == 'redessociales':
		instance = Emprendedor.objects.all().filter(redessociales=False)

	elif id == 'tiendaonline':
		instance = Emprendedor.objects.all().filter(tiendaonline=False)

	elif id == 'cooperativismo':
		instance = Emprendedor.objects.all().filter(cooperativismo=False)

	elif id == 'asociativismo':
		instance = Emprendedor.objects.all().filter(asociativismo=False)

	elif id == 'personajuridica':
		instance = Emprendedor.objects.all().filter(personajuridica=False)

	elif id == 'mujeremprendedora':
		instance = Emprendedor.objects.all().filter(mujeremprendedora=False)

	elif id == 'trabajoydiscapacidad':
		instance = Emprendedor.objects.all().filter(trabajoydiscapacidad=False)

	if instance :
		response = HttpResponse(content_type='application/pdf')
		pdf_name = "Capacitaciones.pdf" 
		response['Content-Disposition'] = 'filename=%s; pagesize=landscape(A4)' %pdf_name
		buff = BytesIO()
		title = "Capacitaciones" 
		
		Story = [Spacer(1, 0)]
		style = styles["textos"]

		def myFirstPage(canvas, doc):
			canvas.saveState()
			# numeracion de pagina
			canvas.setFont('Ubuntu-R', 8)
			canvas.drawString(inch, 0.75 * inch, "Pagina %d" %(doc.page))
			canvas.restoreState()
		
		def cuerpo(canvas): 
			libro = Paragraph("Capacitaciones", tit1) 
			Story.append(libro)
			Story.append(Spacer(1, 30))

			headings = ["Apellido y Nombre", "Identificacion ", "Profesion", "Telefono", "Confirmacion"]
			allregistros = []
			for r in instance:
				registro=[]
				registro.append(r.apellido + ", " + r.nombre)
				registro.append(r.numero)
				registro.append(r.profesion)
				registro.append(r.telefono)
				registro.append("     ")

				allregistros.append(registro)

			t = Table([headings] + allregistros)
			t.setStyle(LIST_STYLE)
			Story.append(t)
			Story.append(Spacer(1, 12))
			return Story


		Story = cuerpo(canvas)
		doc = SimpleDocTemplate(buff, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=75)
		#Construimos el documento a partir de los argumentos definidos
		doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myFirstPage)
		response.write(buff.getvalue())
		buff.close()
		return response
	else:
		raise Http404


def home(request):
	if request.user.is_authenticated():
		if not request.user.is_staff:
			context = {
				"admin" : 0,
			}
			return render(request, "home.html", context)
		else:
			context = {
				"admin" : 1,
			}
			return render(request, "home.html", context)
	else:		
		raise Http404

def l_emprendedor(request):
	
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404

	emprendedor = Emprendedor.objects.all()
	context = {
		'emprendedor': emprendedor,
		'title': "Emprendedores"
	}
	return render(request, "emprendedorlist.html", context)

def crear_emprendedor(request):
	if not request.user.is_authenticated():
		raise Http404
	form = EmprendedorForm(request.POST or None)
	if form.is_valid():
		
		instance = form
		instance.save()

		instance = form.save(commit=False)
		
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title" : "Nuevo Emprendedor",
		"form" : form,
	}
	return render(request, "emprendedorbase.html", context)

def v_emprendedor(request, id=None):
	if request.user.is_authenticated():
		if not request.user.is_staff:
			instance = get_object_or_404(Emprendedor, numero=id)
			context = {
				"persona" : instance,
				"title": "Detalle de Emprendedor",
				"admin": 0,
			}
			return render(request, "emprendedordetalle.html", context)

		else:
			instance = get_object_or_404(Emprendedor, numero=id)
			context = {
				"persona" : instance,
				"title": "Detalle de Emprendedor",
				"admin": 1,
			}
			return render(request, "emprendedordetalle.html", context)

	else:
		raise Http404
	
def u_emprendedor(request, id=None):
	if not request.user.is_authenticated():
		raise Http404
	instance = get_object_or_404(Emprendedor, numero=id)
	form = EmprendedorForm(request.POST or None, instance=instance)
	if form.is_valid():
		
		instance = form
		instance.save()
		instance = form.save(commit=False)
		
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title": "Modificar Emprendedor",
		"instance": instance,
		"form": form,
		"modificar": 0,
	}
	return render(request, "emprendedorbase.html", context)

def desactivar_emprendedor(request):
	return HttpResponse()


def expediente(request, id=None):
	if request.user.is_authenticated():
		if not request.user.is_staff:
			instance = get_object_or_404(Emprendedor, numero=id)
			if(instance):
				instance2 = Expediente.objects.all().filter(emprendedor=instance).order_by("-fecha")
				context = {
					"persona": instance,
					"expediente": instance2,
					"admin": 0,
				}
				return render(request, "expediente.html", context)

		else:
			instance = get_object_or_404(Emprendedor, numero=id)
			if(instance):
				instance2 = Expediente.objects.all().filter(emprendedor=instance).order_by("-fecha")
				context = {
					"persona": instance,
					"expediente": instance2,
					"admin": 1,
				}
				return render(request, "expediente.html", context)
	else:
		raise Http404
	instance = get_object_or_404(Emprendedor, numero=id)
	if(instance):
		instance2 = Expediente.objects.all().filter(emprendedor=instance).order_by("-fecha")
		context = {
			"persona": instance,
			"expediente": instance2,
		}

		return render(request, "expediente.html", context)
	else:
		raise Http404

def expediente_a(request, id=None):
	if not request.user.is_authenticated():
		raise Http404
	instance = get_object_or_404(Emprendedor, numero=id)
	if(instance):
		instance2 = Expediente.objects.all().filter(emprendedor=instance)
		form = ExpedienteForm(request.POST or None)
		if form.is_valid():
			
			instance = form
			instance.save()
			instance = form.save(commit=False)
			print(instance.emprendedor.numero)
			# cambiar id por dni
			return redirect("expediente:asientos", id=instance.emprendedor.numero)
		else:
			print (form.errors)
		context = {
			"persona": instance,
			"expediente": instance2,
			"form": form,
		}

		return render(request, "asiento.html", context)
	else:
		raise Http404

def expediente_m(request, id=None, pd=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Emprendedor, numero=id)

	if(instance):
		instance2 = get_object_or_404(Expediente, id=pd)
		form = ExpedienteForm(request.POST or None, instance=instance2)
		if form.is_valid():
			
			instance = form
			instance.save()
			instance = form.save(commit=False)
			return redirect("expediente:asientos", id=id)
		
		else:
			print (form.errors)
		context = {
			"modificar": 0,
			"persona": instance,
			"check": instance2,
			"form": form,
		}

		return render(request, "asiento.html", context)
	else:
		raise Http404

def expediente_d(request, id=None, pd=None):

	instance = get_object_or_404(Expediente, id=pd)
	instance.activo = False
	instance.save()
	return redirect("expediente:asientos", id=id)

def expediente_ac(request, id=None, pd=None):
	print('here')
	instance = get_object_or_404(Expediente, id=pd)
	instance.activo = True
	instance.save()
	return redirect("expediente:asientos", id=id)

def listados(request):
	if not request.user.is_authenticated():
		raise Http404
	return render(request, "listados.html")

def listados_i(request, id=None):
	if not request.user.is_authenticated():
		raise Http404
	if id == 'modeladodenegocios':
		instance = Emprendedor.objects.all().filter(modeladodenegocios=False) 
		total=len(instance)
		context = {
			"title": 'Modelado de negocios',
			"instance": instance,
			"url":	id, "total": total,
		}
		return render(request, "listados_i.html", context )
	elif id == 'ventas':
		instance = Emprendedor.objects.all().filter(ventas=False) 
		total=len(instance)
		context = {
			"title": 'Ventas',
			"instance": instance,
			"url":	id, "total": total,	
		}
		return render(request, "listados_i.html", context )

	elif id == 'marketing':
		instance = Emprendedor.objects.all().filter(marketing=False) 
		total=len(instance)
		context = {
			"title": 'Marketing',
			"instance": instance,
			"url":	id, "total": total,	
		}
		return render(request, "listados_i.html", context )

	elif id == 'disenodemarca':
		instance = Emprendedor.objects.all().filter(disenodemarca=False) 
		total=len(instance)
		context = {
			"title": 'Diseño de Marca',
			"instance": instance,	
			"url":	id, "total": total,
		}
		return render(request, "listados_i.html", context )

	elif id == 'marcacolectiva':
		instance = Emprendedor.objects.all().filter(marcacolectiva=False) 
		total=len(instance)
		context = {
			"title": 'Marca Colectiva',
			"instance": instance,
			"url":	id, "total": total,	
		}
		return render(request, "listados_i.html", context )

	elif id == 'rentabilidad':
		instance = Emprendedor.objects.all().filter(rentabilidad=False) 
		total=len(instance)
		context = {
			"title": 'Rentabilidad',
			"instance": instance,
			"url":	id, "total": total,	
		}
		return render(request, "listados_i.html", context )

	elif id == 'costos':
		instance = Emprendedor.objects.all().filter(costos=False) 
		total=len(instance)
		context = {
			"title": 'Costos',
			"instance": instance,
			"url":	id, "total": total,	
		}
		return render(request, "listados_i.html", context )

	elif id == 'entrenamientointensivo':
		instance = Emprendedor.objects.all().filter(entrenamientointensivo=False) 
		total=len(instance)
		context = {
			"title": 'Entrenamiento Intensivo',
			"instance": instance,	
			"url":	id, "total": total,
		}
		return render(request, "listados_i.html", context )

	elif id == 'culturaemprendedora':
		instance = Emprendedor.objects.all().filter(culturaemprendedora=False) 
		total=len(instance)
		context = {
			"title": 'Cultura Emprendedora',
			"instance": instance,
			"url":	id, "total": total,	
		}
		return render(request, "listados_i.html", context )

	elif id == 'desarrollodeproducto':
		instance = Emprendedor.objects.all().filter(desarrollodeproducto=False) 
		total=len(instance)
		context = {
			"title": 'Desarrollo de Producto',
			"instance": instance,
			"url":	id, "total": total,	
		}
		return render(request, "listados_i.html", context )

	elif id == 'plandenegocios':
		instance = Emprendedor.objects.all().filter(plandenegocios=False) 
		total=len(instance)
		context = {
			"title": 'Plan de Negocios',
			"instance": instance,	
			"url":	id, "total": total,
		}
		return render(request, "listados_i.html", context )

	elif id == 'innovacionycreatividad':
		instance = Emprendedor.objects.all().filter(innovacionycreatividad=False) 
		total=len(instance)
		context = {
			"title": 'Innovacion y Creatividad',
			"instance": instance,
			"url":	id, "total": total,	
		}
		return render(request, "listados_i.html", context )
	elif id == 'liderazgo':
		instance = Emprendedor.objects.all().filter(liderazgo=False) 
		total=len(instance)
		context = {
			"title": 'Liderazgo',
			"instance": instance,	
			"url":	id, "total": total,
		}
		return render(request, "listados_i.html", context )

	elif id == 'trabajoenequipo':
		instance = Emprendedor.objects.all().filter(trabajoenequipo=False) 
		total=len(instance)
		context = {
			"title": 'Trabajo en equipo',
			"instance": instance,	
			"url":	id, "total": total,
		}
		return render(request, "listados_i.html", context )

	elif id == 'comunicacionefectiva':
		instance = Emprendedor.objects.all().filter(comunicacionefectiva=False) 
		total=len(instance)
		context = {
			"title": 'Comunicacion Efectiva',
			"instance": instance,	
			"url":	id, "total": total,
		}
		return render(request, "listados_i.html", context )

	elif id == 'concursosyconvocatorias':
		instance = Emprendedor.objects.all().filter(concursosyconvocatorias=False) 
		total=len(instance)
		context = {
			"title": 'Concursos y Convocatorias',
			"instance": instance,
			"url":	id, "total": total,	
		}
		return render(request, "listados_i.html", context )

	elif id == 'tradicionalynotradicional':
		instance = Emprendedor.objects.all().filter(tradicionalynotradicional=False) 
		total=len(instance)
		context = {
			"title": 'Financiamiento Tradicional y no Tradicional',
			"instance": instance,	
			"url":	id, "total": total,
		}
		return render(request, "listados_i.html", context )

	elif id == 'marketingdigital':
		instance = Emprendedor.objects.all().filter(marketingdigital=False) 
		total=len(instance)
		context = {
			"title": 'Marketing Digital',
			"instance": instance,	
			"url":	id, "total": total,
		}
		return render(request, "listados_i.html", context )	

	elif id == 'redessociales':
		instance = Emprendedor.objects.all().filter(redessociales=False) 
		total=len(instance)
		context = {
			"title": 'Ventas por Redes Sociales',
			"instance": instance,	
			"url":	id, "total": total,
		}
		return render(request, "listados_i.html", context )

	elif id == 'tiendaonline':
		instance = Emprendedor.objects.all().filter(tiendaonline=False) 
		total=len(instance)
		context = {
			"title": 'Tienda Online',
			"instance": instance,
			"url":	id, "total": total,	
		}
		return render(request, "listados_i.html", context )

	elif id == 'cooperativismo':
		instance = Emprendedor.objects.all().filter(cooperativismo=False) 
		total=len(instance)
		context = {
			"title": 'Cooperativismo',
			"instance": instance,
			"url":	id, "total": total,	
		}
		return render(request, "listados_i.html", context )

	elif id == 'asociativismo':
		instance = Emprendedor.objects.all().filter(asociativismo=False) 
		total=len(instance)
		context = {
			"title": 'Asociativismo',
			"instance": instance,	
			"url":	id, "total": total,
		}
		return render(request, "listados_i.html", context )

	elif id == 'personajuridica':
		instance = Emprendedor.objects.all().filter(personajuridica=False) 
		total=len(instance)
		context = {
			"title": 'Persona Juridica',
			"instance": instance,	
			"url":	id, "total": total,
		}
		return render(request, "listados_i.html", context )

	elif id == 'mujeremprendedora':
		instance = Emprendedor.objects.all().filter(mujeremprendedora=False) 
		total = len(instance)
		context = {
			"title": 'Mujer Emprendedora',
			"instance": instance,	
			"url":	id, 
			"total": total,
		}
		return render(request, "listados_i.html", context )

	elif id == 'trabajoydiscapacidad':
		instance = Emprendedor.objects.all().filter(trabajoydiscapacidad=False) 
		total=len(instance)
		context = {
			"title": 'Trabajo y Discapacidad',
			"instance": instance,	
			"url":	id, "total": total,
		}
		return render(request, "listados_i.html", context )

	elif id == 'desafio':
		emprendedor = Emprendedor.objects.all()
		#print(emprendedor)			
		expediente = Expediente.objects.all().filter(asiento="FERIA: DESAFIO PRODUCIR")
		finallist = []
		for x in emprendedor:
			for z in expediente:
				if x == z.emprendedor:
					print('Encontrado')
				else:
					finallist.append(x)
		context = {
			"title": 'Desafio Producir',
			"instance": finallist,	
		}
		return render(request, "listados_i.html", context )

	elif id == 'artesano':
		emprendedor = Emprendedor.objects.all()
		#print(emprendedor)			
		expediente = Expediente.objects.all().filter(asiento="FERIA: PASEO ARTESANO")
		finallist = []
		print(expediente)
		for x in emprendedor:
			for z in expediente:
				if x == z.emprendedor:
					print('Encontrado')
				else:
					finallist.append(x)


		context = {
			"title": 'Paseo Artesano',
			"instance": finallist,	
		}
		return render(request, "listados_i.html", context )
 
	else:
		raise Http404	
	
	return render(request, "listados.html")



def credito(request):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	expediente = Expediente.objects.all().filter(asiento="OTORGAMIENTO: CREDITO").order_by('fecha')
		
	control = ""
	fechalist = []
	artesanolist = []
	diseñolist = []
	gastronomicolist = []
	horticolalist = []
	servicioslist = []
	sustentabilidadlist = []
	autoslist = []
	tecnologialist = []
	tecnologicolist = []

	for z in expediente:
		if z.activo:	
			if control != z.fecha.year:
				total=0
				control = z.fecha.year
				fechalist.append(control)
				artesanolist.append(total)
				diseñolist.append(total)
				gastronomicolist.append(total)
				horticolalist.append(total)
				servicioslist.append(total)
				sustentabilidadlist.append(total)
				autoslist.append(total)
				tecnologialist.append(total)
				tecnologicolist.append(total)

			last = (len(fechalist)-1)
			if z.rubro == "ARTESANO": 
				artesanolist[last] = artesanolist[last] + z.monto 
			if z.rubro == "DISEÑO": 
				diseñolist[last] = diseñolist[last] + z.monto 
			if z.rubro == "GASTRONOMICO": 
				gastronomicolist[last] = gastronomicolist[last] + z.monto 
			if z.rubro == "HORTICOLA": 
				horticolalist[last] = horticolalist[last] + z.monto 
			if z.rubro == "SERVICIOS": 
				servicioslist[last] = servicioslist[last] + z.monto 
			if z.rubro == "SUSTENTABILIDAD": 
				sustentabilidadlist[last] = sustentabilidadlist[last] + z.monto
			if z.rubro == "TAXI/REMIS": 
				autoslist[last] = autoslist[last] + z.monto
			if z.rubro == "TECNOLOGIA APROPIADA": 
				tecnologialist[last] = tecnologialist[last] + z.monto
			if z.rubro == "TECNOLOGICO": 
				tecnologicolist[last] = tecnologicolist[last] + z.monto
	context = {
		'title': "Grafico de creditos por año",
		'years': fechalist,
		'artesanolist': artesanolist,
		'diseñolist': diseñolist,
		'gastronomicolist': gastronomicolist,
		'horticolalist': horticolalist,
		'servicioslist': servicioslist,
		'sustentabilidadlist': sustentabilidadlist,
		'autoslist': autoslist,
		'tecnologialist': tecnologialist,
		'tecnologicolist': tecnologicolist,

	}
	return render(request, "graphscred.html", context)


def subsidio(request):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	expediente = Expediente.objects.all().filter(asiento="OTORGAMIENTO: SUBSIDIO").order_by('fecha')
		
	control = ""
	fechalist = []
	artesanolist = []
	diseñolist = []
	gastronomicolist = []
	horticolalist = []
	servicioslist = []
	sustentabilidadlist = []
	autoslist = []
	tecnologialist = []
	tecnologicolist = []
	for z in expediente:
		if z.activo:
			if control != z.fecha.year:
				total=0
				control = z.fecha.year
				fechalist.append(control)
				artesanolist.append(total)
				diseñolist.append(total)
				gastronomicolist.append(total)
				horticolalist.append(total)
				servicioslist.append(total)
				sustentabilidadlist.append(total)
				autoslist.append(total)
				tecnologialist.append(total)
				tecnologicolist.append(total)

			last = (len(fechalist)-1)
			if z.rubro == "ARTESANO": 
				artesanolist[last] = artesanolist[last] + z.monto 
			if z.rubro == "DISEÑO": 
				diseñolist[last] = diseñolist[last] + z.monto 
			if z.rubro == "GASTRONOMICO": 
				gastronomicolist[last] = gastronomicolist[last] + z.monto 
			if z.rubro == "HORTICOLA": 
				horticolalist[last] = horticolalist[last] + z.monto 
			if z.rubro == "SERVICIOS": 
				servicioslist[last] = servicioslist[last] + z.monto 
			if z.rubro == "SUSTENTABILIDAD": 
				sustentabilidadlist[last] = sustentabilidadlist[last] + z.monto
			if z.rubro == "TAXI/REMIS": 
				autoslist[last] = autoslist[last] + z.monto
			if z.rubro == "TECNOLOGIA APROPIADA": 
				tecnologialist[last] = tecnologialist[last] + z.monto
			if z.rubro == "TECNOLOGICO": 
				tecnologicolist[last] = tecnologicolist[last] + z.monto
	context = {
		'title': "Grafico de Subsidios por año",
		'years': fechalist,
		'artesanolist': artesanolist,
		'diseñolist': diseñolist,
		'gastronomicolist': gastronomicolist,
		'horticolalist': horticolalist,
		'servicioslist': servicioslist,
		'sustentabilidadlist': sustentabilidadlist,
		'autoslist': autoslist,
		'tecnologialist': tecnologialist,
		'tecnologicolist': tecnologicolist,
	}
	return render(request, "graphssubs.html", context)
	
def empgraph(request):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	
	instance = Emprendedor.objects.all().order_by('fecha', 'profesion')
	yearlist = []
	proflist = []
	total = 1
	control = ""

	control2 = ""
	for z in instance:
		if z.fecha.year != control:
			control = z.fecha.year
			yearlist.append(control)
			proflist.append([])
			last = (len(yearlist)-1)
			control2 = ""

		if control == z.fecha.year:
			proflist[last].append(z.profesion)
			
	
	context = {
		"title": "Grafico de Emprendedores",
		"years": yearlist,
		"profesion": json.dumps(proflist),
	}	
	return render(request, "graphsempr.html", context)

def get_empr2(request, id=None, *args, **kwargs):
	emprendedor = Emprendedor.objects.all().order_by('fecha')
	totalfinal = int(id)
	
	fix = int(len(emprendedor))

	final = fix - totalfinal


	graflist = ["No Participaron", "Participaron"]
	totallist = [totalfinal,final]


	data = {
		"graflist" : graflist,
		"totallist": totallist,
	}
	return JsonResponse(data)


def get_cred(request, *args, **kwargs):
	expediente = Expediente.objects.all().filter(asiento="OTORGAMIENTO: CREDITO").order_by('fecha')
	control = ""
	fechalist = []
	totallist = []

	for z in expediente:
		if z.activo:
			if control != z.fecha.year:
				total=0
				control = z.fecha.year
				fechalist.append(control)
				totallist.append(total)

			last = (len(totallist)-1)
			totallist[last] = totallist[last] + z.monto

	data = {
		"Years" : fechalist,
		"Montos": totallist,
	}
	print(fechalist)
	print(totallist)
	return JsonResponse(data)

def get_subs(request, *args, **kwargs):
	expediente = Expediente.objects.all().filter(asiento="OTORGAMIENTO: SUBSIDIO").order_by('fecha')
		
	control = ""
	fechalist = []
	totallist = []

	for z in expediente:
		if z.activo:
			if control != z.fecha.year:
				total=0
				control = z.fecha.year
				fechalist.append(control)
				totallist.append(total)
			last = (len(totallist)-1)
			totallist[last] = totallist[last] + z.monto

	print( fechalist )
	print( totallist )

	data = {
		"Years" : fechalist,
		"Montos": totallist,
	}
	return JsonResponse(data)

def get_empr(request, *args, **kwargs):
	emprendedor = Emprendedor.objects.all().order_by('fecha')
	control = ""
	fechalist = []
	totallist = []

	for z in emprendedor:
		if control != z.fecha.year:
			total=0
			control = z.fecha.year
			fechalist.append(control)
			totallist.append(total)

		last = (len(totallist)-1)
		totallist[last] = totallist[last] + 1

	data = {
		"Years" : fechalist,
		"Montos": totallist,
	}
	return JsonResponse(data)
