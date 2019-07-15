from django.shortcuts import render
from django.http import Http404
# Create your views here.
from .models import Register


def register_page_view(request):
    obj=Register.objects.get(id=1)
    context={"object":obj}
    return render(request,"index.html",context)