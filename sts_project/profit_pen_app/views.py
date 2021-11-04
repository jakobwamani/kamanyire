from django.shortcuts import render
from profit_pen_app.models import RawMaterial,Product,RawMaterialQuantities
from profit_pen_app.forms  import RawMaterialForm ,ProductForm, SupplyForm
from django.http import HttpResponse
from django.shortcuts import redirect
from profit_pen_app.helper_functions import * 
# import helper_functions.py
from django.contrib import messages


def index(request):
	#To create a new instance of the RMQ model 
	#grab the lastest instance inside the RMQ model
	lastitem = RawMaterialQuantities.objects.last()
	#check if it has any instances , if not then just skip to the end
	count_quantities = RawMaterialQuantities.objects.count()
	if(count_quantities != 0):
		#change dates into some specific dates (%x-Local version of date-12/31/18)
		last_date = lastitem.date
		rear_date =last_date.strftime("%x")
		current_date = datetime.datetime.now()
		earlist_date = current_date.strftime("%x")
		if rear_date == earlist_date:
		    print("Dates are equal")
		else:
			#duplicate the last instance
			dup_maize_bran = lastitem.maize_bran 
			dup_cotton = lastitem.cotton
			dup_sun_flower = lastitem.sun_flower
			dup_fish = lastitem.fish
			dup_salt = lastitem.salt
			dup_general_purpose_premix = lastitem.general_purpose_premix
			dup_layers_premix = lastitem.layers_premix
			dup_shells = lastitem.shells
			dup_meat_boaster = lastitem.meat_boaster
			dup_egg_boaster=lastitem.egg_boaster
			duplicate_quantiites = RawMaterialQuantities.objects.create(date = datetime.datetime.now(),maize_bran = dup_maize_bran ,cotton = dup_cotton,
	                                                               sun_flower = dup_sun_flower, fish = dup_fish,salt = dup_salt ,
	                                                               general_purpose_premix = dup_general_purpose_premix,layers_premix = dup_layers_premix,
	                                                               shells = dup_shells, meat_boaster = dup_meat_boaster,egg_boaster=dup_egg_boaster)
	else:
		print("Just continue with life")
	return HttpResponse("Hello, world. Welcome to the profitpen system.")

def create_supply(request):
	# dictionary for initial data with
	# field names as keys
	context = {}

	# add the dictionary during initialization
	form = SupplyForm(request.POST or None)

	if form.is_valid():
		form.save()
		#Its here that after the supply is made then we shall start populating the RawMaterialQuantities
		#table
		# we shall check if the "RawMaterialQuantities" table has atleast one row
		compute_quantities()
	context['form'] = form

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
			increase_quantity_value = form.cleaned_data['increase_quantity']

			reduce_quantity_value = form.cleaned_data['reduce_quantity']

			if increase_quantity_value > 0:
				#get the current quantity of raw material in the RMQ model
				#Get date from the form
				date_of_supply = form.cleaned_data['date']
				#identify the item that we want to update
				item_supplied = form.cleaned_data['item']
				if item_supplied == 'egg_boaster':
					amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
					#get amount supplied	
					item_value = amount_of_supply.egg_boaster
					#add the two together
					incremented_value = item_value + increase_quantity_value
					#update the value 
					amount_of_supply.egg_boaster = incremented_value
					amount_of_supply.save()					
					# then also add the incremented value on the last instance
					current_supply = RawMaterialQuantities.objects.last()
					#latest_instance
					#first check if the updated instance the lastest instance are
					#of the same date or not
					last_date = amount_of_supply.date
					rear_date = last_date.strftime("%x")
					current_date = current_supply.date
					earlist_date = current_date.strftime("%x")
					#code below is for incase the dates are not the same.
					if rear_date != earlist_date:
						current_egg_boaster_value = current_supply.egg_boaster
						increased_value = current_egg_boaster_value + increase_quantity_value
						current_supply.egg_boaster = increased_value
						current_supply.save()
					else:
						print("move on with life")

				elif item_supplied == 'maize_bran':
					#update the RMQ maize_bran quantity
					amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
					item_value = amount_of_supply.maize_bran
					incremented_value = item_value + increase_quantity_value
					amount_of_supply.maize_bran = incremented_value
					amount_of_supply.save()
					
					#update the last instance
					current_supply = RawMaterialQuantities.objects.last()
					#latest_instance
					#first check if the updated instance the lastest instance are
					#of the same date or not
					last_date = amount_of_supply.date
					rear_date = last_date.strftime("%x")
					current_date = current_supply.date
					earlist_date = current_date.strftime("%x")

					if rear_date != earlist_date:
						current_maize_bran_value = current_supply.maize_bran
						increased_value =  current_maize_bran_value + increase_quantity_value
						current_supply.maize_bran = increased_value
						current_supply.save()
					else:
						print("move on with life")						

				elif item_supplied == 'cotton':
					amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
					item_value = amount_of_supply.cotton
					incremented_value = item_value + increase_quantity_value
					amount_of_supply.cotton = incremented_value
					amount_of_supply.save()

					current_supply = RawMaterialQuantities.objects.last()
					#latest_instance
					#first check if the updated instance the lastest instance are
					#of the same date or not
					last_date = amount_of_supply.date
					rear_date = last_date.strftime("%x")
					current_date = current_supply.date
					earlist_date = current_date.strftime("%x")

					if rear_date != earlist_date:
						current_cotton_value = current_supply.cotton
						increased_value =  current_cotton_value + increase_quantity_value
						current_supply.cotton = increased_value
						current_supply.save()
					else:
						print("move on with life")

				elif item_supplied == 'sun_flower':
					amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
					item_value = amount_of_supply.sun_flower
					incremented_value = item_value + increase_quantity_value
					amount_of_supply.sun_flower = incremented_value
					amount_of_supply.save()

					current_supply = RawMaterialQuantities.objects.last()
					#latest_instance
					#first check if the updated instance the lastest instance are
					#of the same date or not
					last_date = amount_of_supply.date
					rear_date = last_date.strftime("%x")
					current_date = current_supply.date
					earlist_date = current_date.strftime("%x")

					if rear_date != earlist_date:
						current_sun_flower_value = current_supply.sun_flower
						increased_value =  current_sun_flower_value + increase_quantity_value
						current_supply.sun_flower = increased_value
						current_supply.save()
					else:
						print("move on with life")

				elif item_supplied == 'fish':
					amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
					item_value = amount_of_supply.fish
					incremented_value = item_value + increase_quantity_value
					amount_of_supply.fish = incremented_value
					amount_of_supply.save()

					current_supply = RawMaterialQuantities.objects.last()
					#latest_instance
					#first check if the updated instance the lastest instance are
					#of the same date or not
					last_date = amount_of_supply.date
					rear_date = last_date.strftime("%x")
					current_date = current_supply.date
					earlist_date = current_date.strftime("%x")

					if rear_date != earlist_date:
						current_fish_value = current_supply.fish
						increased_value =  current_fish_value + increase_quantity_value
						current_supply.fish = increased_value
						current_supply.save()
					else:
						print("move on with life")

				elif item_supplied == 'salt':
					amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
					item_value = amount_of_supply.salt
					incremented_value = item_value + increase_quantity_value
					amount_of_supply.salt = incremented_value
					amount_of_supply.save()

					current_supply = RawMaterialQuantities.objects.last()
					#latest_instance
					#first check if the updated instance the lastest instance are
					#of the same date or not
					last_date = amount_of_supply.date
					rear_date = last_date.strftime("%x")
					current_date = current_supply.date
					earlist_date = current_date.strftime("%x")

					if rear_date != earlist_date:
						current_salt_value = current_supply.salt
						increased_value =  current_salt_value + increase_quantity_value
						current_supply.salt = increased_value
						current_supply.save()
					else:
						print("move on with life")

				elif item_supplied == 'layers_premix':
					amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
					item_value = amount_of_supply.layers_premix
					incremented_value = item_value + increase_quantity_value
					amount_of_supply.layers_premix = incremented_value
					amount_of_supply.save()

					current_supply = RawMaterialQuantities.objects.last()
					#latest_instance
					#first check if the updated instance the lastest instance are
					#of the same date or not
					last_date = amount_of_supply.date
					rear_date = last_date.strftime("%x")
					current_date = current_supply.date
					earlist_date = current_date.strftime("%x")

					if rear_date != earlist_date:
						current_layers_premix_value = current_supply.layers_premix
						increased_value =  current_layers_premix_value + increase_quantity_value
						current_supply.layers_premix = increased_value
						current_supply.save()
					else:
						print("move on with life")

				elif item_supplied == 'general_purpose_premix':
					amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
					item_value = amount_of_supply.general_purpose_premix
					incremented_value = item_value + increase_quantity_value
					amount_of_supply.general_purpose_premix = incremented_value
					amount_of_supply.save()

					current_supply = RawMaterialQuantities.objects.last()
					#latest_instance
					#first check if the updated instance the lastest instance are
					#of the same date or not
					last_date = amount_of_supply.date
					rear_date = last_date.strftime("%x")
					current_date = current_supply.date
					earlist_date = current_date.strftime("%x")

					if rear_date != earlist_date:
						current_general_purpose_premix_value = current_supply.general_purpose_premix
						increased_value =  current_general_purpose_premix_value + increase_quantity_value
						current_supply.general_purpose_premix = increased_value
						current_supply.save()
					else:
						print("move on with life")

				elif item_supplied == 'shells':
					amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
					item_value = amount_of_supply.shells
					incremented_value = item_value + increase_quantity_value
					amount_of_supply.shells = incremented_value
					amount_of_supply.save()

					current_supply = RawMaterialQuantities.objects.last()
					#latest_instance
					#first check if the updated instance the lastest instance are
					#of the same date or not
					last_date = amount_of_supply.date
					rear_date = last_date.strftime("%x")
					current_date = current_supply.date
					earlist_date = current_date.strftime("%x")

					if rear_date != earlist_date:
						current_general_purpose_premix_value = current_supply.shells
						increased_value =  current_shells_value + increase_quantity_value
						current_supply.shells = increased_value
						current_supply.save()
					else:
						print("move on with life")
						
				elif item_supplied == 'meat_boaster':
					amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
					item_value = amount_of_supply.meat_boaster
					incremented_value = item_value + increase_quantity_value
					amount_of_supply.meat_boaster = incremented_value
					amount_of_supply.save()

					current_supply = RawMaterialQuantities.objects.last()
					#latest_instance
					#first check if the updated instance the lastest instance are
					#of the same date or not
					last_date = amount_of_supply.date
					rear_date = last_date.strftime("%x")
					current_date = current_supply.date
					earlist_date = current_date.strftime("%x")

					if rear_date != earlist_date:
						current_general_purpose_premix_value = current_supply.meat_boaster
						increased_value =  current_shells_value + increase_quantity_value
						current_supply.meat_boaster = increased_value
						current_supply.save()
					else:
						print("move on with life")

			else:
				date_of_supply = form.cleaned_data['date']
				#identify the item that we want to update
				item_supplied = form.cleaned_data['item']
				if item_supplied == 'egg_boaster':
					amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
					#get amount supplied	
					item_value = amount_of_supply.egg_boaster
					#add the two together
					incremented_value = item_value - reduce_quantity_value
					#update the value 
					amount_of_supply.egg_boaster = incremented_value
					amount_of_supply.save()					
					# then also add the incremented value on the last instance
					current_supply = RawMaterialQuantities.objects.last()
					#latest_instance
					#first check if the updated instance the lastest instance are
					#of the same date or not
					last_date = amount_of_supply.date
					rear_date = last_date.strftime("%x")
					current_date = current_supply.date
					earlist_date = current_date.strftime("%x")
					#code below is for incase the dates are not the same.
					if rear_date != earlist_date:
						current_egg_boaster_value = current_supply.egg_boaster
						increased_value = current_egg_boaster_value - reduce_quantity_value
						current_supply.egg_boaster = increased_value
						current_supply.save()
					else:
						print("move on with life")

				elif item_supplied == 'maize_bran':
					#update the RMQ maize_bran quantity
					amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
					item_value = amount_of_supply.maize_bran
					incremented_value = item_value - reduce_quantity_value
					amount_of_supply.maize_bran = incremented_value
					amount_of_supply.save()
					
					#update the last instance
					current_supply = RawMaterialQuantities.objects.last()
					#latest_instance
					#first check if the updated instance the lastest instance are
					#of the same date or not
					last_date = amount_of_supply.date
					rear_date = last_date.strftime("%x")
					current_date = current_supply.date
					earlist_date = current_date.strftime("%x")

					if rear_date != earlist_date:
						current_maize_bran_value = current_supply.maize_bran
						increased_value =  current_maize_bran_value + reduce_quantity_value
						current_supply.maize_bran = increased_value
						current_supply.save()
					else:
						print("move on with life")		

				elif item_supplied == 'cotton':
					amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
					item_value = amount_of_supply.cotton
					incremented_value = item_value - reduce_quantity_value
					amount_of_supply.cotton = incremented_value
					amount_of_supply.save()

					current_supply = RawMaterialQuantities.objects.last()
					#latest_instance
					#first check if the updated instance the lastest instance are
					#of the same date or not
					last_date = amount_of_supply.date
					rear_date = last_date.strftime("%x")
					current_date = current_supply.date
					earlist_date = current_date.strftime("%x")

					if rear_date != earlist_date:
						current_cotton_value = current_supply.cotton
						increased_value =  current_cotton_value - reduce_quantity_value
						current_supply.cotton = increased_value
						current_supply.save()
					else:
						print("move on with life")

				elif item_supplied == 'sun_flower':
					amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
					item_value = amount_of_supply.sun_flower
					incremented_value = item_value - reduce_quantity_value
					amount_of_supply.sun_flower = incremented_value
					amount_of_supply.save()

					current_supply = RawMaterialQuantities.objects.last()
					#latest_instance
					#first check if the updated instance the lastest instance are
					#of the same date or not
					last_date = amount_of_supply.date
					rear_date = last_date.strftime("%x")
					current_date = current_supply.date
					earlist_date = current_date.strftime("%x")

					if rear_date != earlist_date:
						current_sun_flower_value = current_supply.sun_flower
						increased_value =  current_sun_flower_value - reduce_quantity_value
						current_supply.sun_flower = increased_value
						current_supply.save()
					else:
						print("move on with life")

				elif item_supplied == 'fish':
					amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
					item_value = amount_of_supply.fish
					incremented_value = item_value - reduce_quantity_value
					amount_of_supply.fish = incremented_value
					amount_of_supply.save()

					current_supply = RawMaterialQuantities.objects.last()
					#latest_instance
					#first check if the updated instance the lastest instance are
					#of the same date or not
					last_date = amount_of_supply.date
					rear_date = last_date.strftime("%x")
					current_date = current_supply.date
					earlist_date = current_date.strftime("%x")

					if rear_date != earlist_date:
						current_fish_value = current_supply.fish
						increased_value =  current_fish_value - reduce_quantity_value
						current_supply.fish = increased_value
						current_supply.save()
					else:
						print("move on with life")

				elif item_supplied == 'salt':
					amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
					item_value = amount_of_supply.salt
					incremented_value = item_value - reduce_quantity_value
					amount_of_supply.salt = incremented_value
					amount_of_supply.save()

					current_supply = RawMaterialQuantities.objects.last()
					#latest_instance
					#first check if the updated instance the lastest instance are
					#of the same date or not
					last_date = amount_of_supply.date
					rear_date = last_date.strftime("%x")
					current_date = current_supply.date
					earlist_date = current_date.strftime("%x")

					if rear_date != earlist_date:
						current_salt_value = current_supply.salt
						increased_value =  current_salt_value - reduce_quantity_value
						current_supply.salt = increased_value
						current_supply.save()
					else:
						print("move on with life")

				elif item_supplied == 'layers_premix':
					amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
					item_value = amount_of_supply.layers_premix
					incremented_value = item_value - reduce_quantity_value
					amount_of_supply.layers_premix = incremented_value
					amount_of_supply.save()

					current_supply = RawMaterialQuantities.objects.last()
					#latest_instance
					#first check if the updated instance the lastest instance are
					#of the same date or not
					last_date = amount_of_supply.date
					rear_date = last_date.strftime("%x")
					current_date = current_supply.date
					earlist_date = current_date.strftime("%x")

					if rear_date != earlist_date:
						current_layers_premix_value = current_supply.layers_premix
						increased_value =  current_layers_premix_value - reduce_quantity_value
						current_supply.layers_premix = increased_value
						current_supply.save()
					else:
						print("move on with life")

				elif item_supplied == 'general_purpose_premix':
					amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
					item_value = amount_of_supply.general_purpose_premix
					incremented_value = item_value - reduce_quantity_value
					amount_of_supply.general_purpose_premix = incremented_value
					amount_of_supply.save()

					current_supply = RawMaterialQuantities.objects.last()
					#latest_instance
					#first check if the updated instance the lastest instance are
					#of the same date or not
					last_date = amount_of_supply.date
					rear_date = last_date.strftime("%x")
					current_date = current_supply.date
					earlist_date = current_date.strftime("%x")

					if rear_date != earlist_date:
						current_general_purpose_premix_value = current_supply.general_purpose_premix
						increased_value =  current_general_purpose_premix_value - increase_quantity_value
						current_supply.general_purpose_premix = increased_value
						current_supply.save()
					else:
						print("move on with life")

				elif item_supplied == 'shells':
					amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
					item_value = amount_of_supply.shells
					incremented_value = item_value - reduce_quantity_value
					amount_of_supply.shells = incremented_value
					amount_of_supply.save()

					current_supply = RawMaterialQuantities.objects.last()
					#latest_instance
					#first check if the updated instance the lastest instance are
					#of the same date or not
					last_date = amount_of_supply.date
					rear_date = last_date.strftime("%x")
					current_date = current_supply.date
					earlist_date = current_date.strftime("%x")

					if rear_date != earlist_date:
						current_general_purpose_premix_value = current_supply.shells
						increased_value =  current_shells_value - reduce_quantity_value
						current_supply.shells = increased_value
						current_supply.save()
					else:
						print("move on with life")

				elif item_supplied == 'meat_boaster':
					amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
					item_value = amount_of_supply.meat_boaster
					incremented_value = item_value - reduce_quantity_value
					amount_of_supply.meat_boaster = incremented_value
					amount_of_supply.save()

					current_supply = RawMaterialQuantities.objects.last()
					#latest_instance
					#first check if the updated instance the lastest instance are
					#of the same date or not
					last_date = amount_of_supply.date
					rear_date = last_date.strftime("%x")
					current_date = current_supply.date
					earlist_date = current_date.strftime("%x")

					if rear_date != earlist_date:
						current_general_purpose_premix_value = current_supply.meat_boaster
						increased_value =  current_shells_value - reduce_quantity_value
						current_supply.meat_boaster = increased_value
						current_supply.save()
					else:
						print("move on with life")
			
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
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        supply_item = supply_record_to_delete.item
        supply_quantity = supply_record_to_delete.quantity
        #put them inside a function right away
        reduce_due_to_deletion(supply_item,supply_quantity) 
        
        supply_record_to_delete.delete()
        redirect('view_supply.html')
        # if request.method =='POST':
        # 	#we get to know the item 

        #     supply_record_to_delete.delete()
        #     return redirect('view_supply.html')

        # context_dict["object"] = supply_record_to_delete
    return render(request, "delete_supply.html",context=context_dict)

def create_product(request):
	context = {}
	form = ProductForm(request.POST or None)
	if form.is_valid():

		product = form.cleaned_data['product']	
		maize_bran = form.cleaned_data['maize_bran']
		cotton = form.cleaned_data['cotton']
		sun_flower = form.cleaned_data['sun_flower']
		fish = form.cleaned_data['fish']
		salt = form.cleaned_data['salt']
		general_purpose_premix = form.cleaned_data['general_purpose_premix']
		layers_premix = form.cleaned_data['layers_premix']
		shells = form.cleaned_data['shells']
		meat_boaster = form.cleaned_data['meat_boaster']
		egg_boaster = form.cleaned_data['egg_boaster']


	   	# maize_bran,cotton,sun_flower,fish,salt,general_purpose_premix,layers_premix ,shells 
   		# ,meat_boaster ,egg_boaster
		 
		subtracting(product,maize_bran,cotton,sun_flower,fish,salt,general_purpose_premix,layers_premix,shells,meat_boaster,egg_boaster)

		# remaining_maize_bran = maize_bran_ingridient - subtracting('maize_bran')
		# #if the balance is less than zero 
		# if remaining_maize_bran < 0:
		# 	messages.add_message(request, messages.INFO, 'Maize_bran is over')
		# else:
		# 	messages.add_message(request, messages.INFO, "Remaining_maize_bran " + str(remaining_maize_bran) + "kilograms")
		
		# #so we are now		    	
		form.save()
	context['form'] = form

	return render(request,"product.html",context)

def viewing_product(request):
   	#get the date from the user 
	start_date = request.GET.get('start_date')
	end_date = request.GET.get('end_date')
	# six_months.strftime('%Y%m%d')
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

def deleting_product(request):
    # book= get_object_or_404(Book, pk=pk)  
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        product_record_to_delete = Product.objects.get(id=cleaned_pk)  
        # if request.method=='POST':
        product_record_to_delete.delete()
        return redirect('view_products')
        # return redirect('../view_product.html')

        # context_dict["object"] = product_record_to_delete
    return render(request, "delete_product.html",context=context_dict)