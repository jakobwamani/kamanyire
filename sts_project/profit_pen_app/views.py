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

	# July 31 2021
	
	#i get to grab these values 
	# date = request.GET.get('date')
	# receipt_number = request.GET.get('receipt_number')
	# supplier = request.GET.get('supplier')
	# item = request.GET.get('item')
	# quantity = request.GET.get('quantity')
	# unit_price = request.GET.get('unit_price')
	# transport = request.GET.get('transport')
	# onloading = request.GET.get('onloading')
	# offloading = request.GET.get('offloading')
	# grinding = request.GET.get('grinding')

	#working on amounts......
	# amount = quantity*unit_price
	# fullamount = amount+transport+onloading+offloading+grinding
	# #create an object to send them to the table
	# b = RawMaterial(date=date, receipt_number=receipt_number, supplier=supplier, item=item, quantity=quantity,
	# 	unit_price=unit_price, amount=amount , transport=transport, onloading=onloading, offloading=offloading, grinding=grinding, fullamount=fullamount)
	# b.save()
	# print(type(quantity))

	return render(request, "supply.html",context)

def view_supply(request):
   	#get the date from the user 
	start_date = request.GET.get('start_date')
	end_date = request.GET.get('end_date')

	# run a query to get all the supplies on that date
	supplies = RawMaterial.objects.filter(date__range=[start_date, end_date])

	
     
	# return render(request, "view_supply.html", context)
	return render(request, "view_supply.html", {'supplies':supplies})

