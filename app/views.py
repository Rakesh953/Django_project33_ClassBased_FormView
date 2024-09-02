from django.shortcuts import render
from django.views.generic import FormView
from app.forms import *
from django.http import HttpResponse
# Create your views here.


class CB_List_View(FormView):
    template_name='CB_List_View.html'
    form_class=StudentForm

    def form_valid(self, form):
        form.save()
        return HttpResponse('Form is sumitted successfully')