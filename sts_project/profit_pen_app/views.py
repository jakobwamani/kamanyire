from django.shortcuts import render
from profit_pen_app.models import RawMaterial
from profit_pen_app.forms  import RawMaterialForm
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Welcome to the profitpen system.")

def create_supply(request):
	# dictionary for initial data with
	# field names as keys
	context = {}

	# add the dictionary during initialization
	form = RawMaterialForm(request.POST or None)
	if form.is_valid():
		form.save()
		
	context['form']= form
	return render(request, "supply.html", context)
