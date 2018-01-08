from django.conf.urls import url
from django.contrib import admin
from expediente import views

urlpatterns = [


    #sistem
    url(r'^home/$', views.home),


    #emprendedor
    url(r'^emprendedor/$', views.l_emprendedor, name="l_emprendedor"),
    url(r'^emprendedor/crear/$', views.crear_emprendedor),
    url(r'^emprendedor/(?P<id>[\w\-]+)/$', views.v_emprendedor, name="v_emprendedor"),
    url(r'^emprendedor/(?P<id>[\w\-]+)/u$', views.u_emprendedor),

    #expediente
    url(r'^(?P<id>[\w\-]+)/expediente/$', views.expediente, name="asientos"),
    url(r'^(?P<id>[\w\-]+)/expediente/activar/(?P<pd>\d+)$', views.expediente_ac), #activar
    url(r'^(?P<id>[\w\-]+)/expediente/desactivar/(?P<pd>\d+)$', views.expediente_d), #desactivar
    url(r'^(?P<id>[\w\-]+)/expediente/asiento$', views.expediente_a), #generar nuevo asiento
    url(r'^(?P<id>[\w\-]+)/expediente/asiento/(?P<pd>\d+)$', views.expediente_m), # Modificar asiento

    #listados
    url(r'^listados/$', views.listados),
    url(r'^listados/(?P<id>[\w\-]+)$', views.listados_i),


    #graphs
    url(r'^graphs/cred$', views.credito),
    url(r'^graphs/subs$', views.subsidio),
    url(r'^graphs/empr$', views.empgraph),


    #jsongraphs
    url(r'^api/graphs/cred/$', views.get_cred),
    url(r'^api/graphs/empr/$', views.get_empr),
    url(r'^api/graphs/empr2/(?P<id>\d+)$', views.get_empr2),
    url(r'^api/graphs/subs/$', views.get_subs),

    #pdf
    url(r'^(?P<id>[\w\-]+)/expediente/pdf/$', views.pdf),
    url(r'^listados/(?P<id>[\w\-]+)/pdf$', views.listados_pdf),

]