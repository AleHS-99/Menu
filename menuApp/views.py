from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from six import BytesIO
import qrcode
from.models import *
# Create your views here.
class HomePage(ListView):
    model = oferta
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = oferta.objects.all()
        a = []
        for i in modalidad.objects.all():
            a.append((i.codigo,i.modal,i.modal.replace(' ','')))
        context['modal'] = a
        return context

def qrcode2(request):
    data = 'http://alehs.pythonanywhere.com/'
    img = qrcode.make(data)

    buf = BytesIO()
    img.save(buf)
    image_stream = buf.getvalue()

    response = HttpResponse(image_stream,content_type="image/png")
    response['Content-Disposition']='attachment;filename=qr.png'
    return response

def abaut(request):

    return render(request, 'abaut.html')

class LoginFormView(LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class ofertas(ListView):
    model = modalidad
    template_name = 'ofertas_list.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = ['oferta','opciones']
        context['url'] = reverse_lazy('addOa')
        context['title'] = 'Lsitado de Ofertas'
        return context

class AddOferta(CreateView):
    template_name = 'addbase.html'
    form_class = ModalForm
    model = modalidad
    success_url = reverse_lazy('addO')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Añadir Oferta'
        return context
def update(request,pk):
    obj = modalidad.objects.get(codigo=pk)
    form = ModalForm(instance=obj)
    context={'form':form, 'title':'Editar Oferta'}
    if request.method=='POST':
        form = ModalForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('addO')
    return render(request,'addbase.html',context)

class DeleteCola(DeleteView):
    model = modalidad
    template_name = 'deleteCola.html'
    success_url = reverse_lazy('addO')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Eliminar Oferta'
        context['list_url'] = reverse_lazy('addO')
        return context

class Servicios(ListView):
    model = oferta
    template_name = 'servicios_list.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = ['Nombre','Descripción','Tipo de Oferta','Precio','Opciones']
        context['url'] = reverse_lazy('addSa')
        context['title'] = 'Listado de Servicios por Oferta'
        context['object_list'] = oferta.objects.all()
        return context

class AddServicio(CreateView):
    template_name = 'addS.html'
    form_class = OfertaForm
    model = modalidad
    success_url = reverse_lazy('addS')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        try:
            form = OfertaForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('addS')
        except Exception:
            pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Añadir Servicio'
        return context
def updateS(request,pk):
    obj = oferta.objects.get(codigo=pk)
    form = OfertaForm(instance=obj)
    context={'form':form, 'title':'Editar Servicio'}
    if request.method=='POST':
        form = OfertaForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('addS')
    return render(request,'addS.html',context)

class DeleteS(DeleteView):
    model = oferta
    template_name = 'deleteServicio.html'
    success_url = reverse_lazy('addS')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Eliminar Servicio'
        context['list_url'] = reverse_lazy('addS')
        return context


class CreateUserForm(FormView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('Home')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs)

    def form_valid(self, form):
        form.save()
        return redirect('Home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context