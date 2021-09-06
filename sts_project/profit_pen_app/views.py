from django.shortcuts import render
from profit_pen_app.models import RawMaterial,Product
from profit_pen_app.forms  import RawMaterialForm ,ProductForm
from django.http import HttpResponse
from django.shortcuts import redirect
from helper_functions import * 
from django.contrib import messages


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
	return render(request, "supply.html",context)

def viewing_supply(request):
   	#get the date from the user 
	start_date = request.GET.get('start_date')
	end_date = request.GET.get('end_date')

	# run a query to get all the supplies on that date
	supplies = RawMaterial.objects.filter(date__range=[start_date, end_date])

	print(type(supplies))
     
	# return render(request, "view_supply.html", context)
	return render(request, "view_supply.html", {'supplies':supplies})

def updating_supply(request):
	context_dict = {}
	if 'id' in request.GET:
		pk = request.GET['id']
		print (pk)
		clean_pk = pk.strip("/")
		print (clean_pk)
		supply_record = RawMaterial.objects.get(id=clean_pk)
		form = RawMaterialForm(request.POST or None, instance=supply_record)
    
		if form.is_valid():			
			form.save()
			redirect('view_supply.html')
		context_dict["form"] = form
	return render(request,"update_supply.html",context=context_dict)

def delete_supply(request):
    # book= get_object_or_404(Book, pk=pk)  
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        supply_record_to_delete = RawMaterial.objects.get(id=cleaned_pk)  
        if request.method=='POST':
            supply_record_to_delete.delete()
            return redirect('view_supply.html')

        context_dict["object"] = supply_record_to_delete
    return render(request, "delete_supply.html",context=context_dict)

def create_product(request):
	context = {}
	form = ProductForm(request.POST or None)
	if form.is_valid():
		#so its from here that we shall pull of that stuff
		#Grab the data from the form
		#Subtract it from the data in the raw materials
		#then save the form.	
		maize_bran_ingridient = form.cleaned_data['maize_bran']
		# then pick from the supplies
		# maize_bran_supply = RawMaterial.objects.filter(item='Maize/bran')
		# # Change the result of the query into a list
		# maize_bran_supply_list = list(maize_bran_supply)
		# # Create an empty list to store the quantites 
		# maize_bran_supply_quantities = []
		# # For every item in the maize_bran_supply_list , get the quantity attribute and add it to the empty list.
		# for quantity_attribute in maize_bran_supply_list:
		# 	#get the value of the quantity
		# 	value = quantity_attribute.quantity
		# 	#populate the empty list
		# 	maize_bran_supply_quantities.append("value")
		# #get the sum of quantites inside the maize_bran_supply_quantities
		# sum(maize_bran_supply_quantities)
		# #try to get the remaining quantity of the rawmaterial
		#this is the function to subtract 
		subtracting('Maize/bran')

		remaining_maize_bran = maize_bran_ingridient - subtracting('Maize/bran')
		#if the balance is less than zero 
		if remaining_maize_bran < 0:
			messages.add_message(request, messages.INFO, 'Maize_bran is over')
		
		#subtracting('Maize/bran')


		    	
		form.save()
	context['form'] = form

	return render(request,"product.html",context)

def viewing_product(request):
   	#get the date from the user 
	start_date = request.GET.get('start_date')
	end_date = request.GET.get('end_date')

	# run a query to get all the supplies on that date
	products = Product.objects.filter(date__range=[start_date, end_date])

	print(type(products))
     
	return render(request, "view_product.html", {'products':products}) 

def updating_product(request):
	context_dict = {}

	if 'id' in request.GET:
		pk = request.GET['id']

		print (pk)
		clean_pk = pk.strip("/")
		print (clean_pk)
		product_record = Product.objects.get(id=clean_pk)
		form = ProductForm(request.POST or None, instance=product_record)
    
		if form.is_valid():
			
			form.save()

			redirect('view_product.html')

		context_dict["form"] = form

	return render(request,"update_product.html",context=context_dict)

def delete_product(request):
    # book= get_object_or_404(Book, pk=pk)  
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        product_record_to_delete = Product.objects.get(id=cleaned_pk)  
        if request.method=='POST':
            product_record_to_delete.delete()
            return redirect('view_product.html')

        context_dict["object"] = product_record_to_delete
    return render(request, "delete_product.html",context=context_dict)