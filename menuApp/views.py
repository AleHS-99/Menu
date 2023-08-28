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
    data = 'http://elguayabero.pythonanywhere.com/'
    img = qrcode.make(data)

    buf = BytesIO()
    img.save(buf)
    image_stream = buf.getvalue()

    response = HttpResponse(image_stream,content_type="image/png")
    response['Content-Disposition']='attachment;filename=qr.png'
    return response

def abaut(request):

    return render(request, 'abaut.html')

