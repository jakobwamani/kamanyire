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
		# July 30th 2021
		# the line below is how you get data from a form
		# i need to calculate the amount and also the full amount it cost kamanyire to get a supply
		# for amount , i could say , its quantity multiplied by unit_price
		# for full amount , its am amount + transport + onloading + offloading + grinding 
		# i have to get each one of them first then treat them
		# quantity = form.cleaned_data.get("quantity")
		# unit_price = form.cleaned_data.get("unit_price")
		# transport = form.cleaned_data.get("transport")
		# onloading = form.cleaned_data.get("onloading")
		# offloading = form.cleaned_data.get("offloading")
		# grinding = form.cleaned_data.get("grinding")
		# set the amount and full amount
		# raw_material_amount = quantity * unit_price
		# transactional_fullamount = raw_material_amount + transport + onloading + offloading + grinding 
		# setattr(form, amount, raw_material_amount)
		# i have decided to leave out amount and full amount from the database because , i have failed to derive
		# and enter them in the form at once



		# print(supplier)
		form.save()
		
	context['form']= form
	return render(request, "supply.html", context)

def view_supply(request):
    # dictionary for initial data with
    # field names as keys
    context = {}
 
    # add the dictionary during initialization
   
    supply_list = RawMaterial.objects.all()

    context_dict = {'supply_list' : supply_list}
     
    return render(request, "view_supply.html", context_dict)
