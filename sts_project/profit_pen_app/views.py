from django.shortcuts import render
from profit_pen_app.models import * 
from profit_pen_app.forms  import * 
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
		rear_date = last_date.strftime("%x")
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

	#do the same with Product 
	lastproduct = ProductQuantities.objects.last()

	count_pq = ProductQuantities.objects.count()
	if(count_pq != 0):
		last_date = lastproduct.date
		rear_date = last_date.strftime("%x")
		current_date = datetime.datetime.now()
		earlist_date = current_date.strftime("%x")
		if rear_date == earlist_date:
			print("Dates are equal")
		else:
			dup_broilers_marsh = lastproduct.broilers_marsh
			dup_chick_marsh = lastproduct.chick_marsh
			dup_old_pig = lastproduct.old_pig
			dup_growers_marsh = lastproduct.growers_marsh
			dup_layers_marsh = lastproduct.layers_marsh
			dup_young_pig = lastproduct.young_pig

			duplicate_quantiites = ProductQuantities.objects.create(date = datetime.datetime.now(),broilers_marsh = dup_broilers_marsh , chick_marsh = dup_chick_marsh , 
									old_pig = dup_old_pig , growers_marsh = dup_growers_marsh,layers_marsh = dup_layers_marsh , young_pig = dup_young_pig)
	else:
		print("Just continue with life")

	last_product_price = ProductPrices.objects.last()

	count_pp = ProductPrices.objects.count()
	if(count_pp != 0 ):
		last_date = last_product_price.date
		rear_date = last_date.strftime("%x")
		current_date = datetime.datetime.now()
		earlist_date = datetime.datetime.now()
		earlist_date = current_date.strftime("%x")
		if rear_date == earlist_date:
			print("Dates are equal")
		else:
			dup_broilers_marsh = last_product_price.broilers_marsh
			dup_chick_marsh = last_product_price.chick_marsh
			dup_old_pig = last_product_price.old_pig
			dup_growers_marsh = last_product_price.growers_marsh
			dup_layers_marsh = last_product_price.layers_marsh
			dup_young_pig = last_product_price.young_pig

			duplicate_prices = ProductQuantities.objects.create(date = datetime.datetime.now(),broilers_marsh = dup_broilers_marsh , chick_marsh = dup_chick_marsh , 
									old_pig = dup_old_pig , growers_marsh = dup_growers_marsh,layers_marsh = dup_layers_marsh , young_pig = dup_young_pig)
	else:
		print("Why can't just be free , from the ways of this world")

	last_rm_quantity = RawMaterialPrices.objects.last()
	#check if it has any instances , if not then just skip to the end
	count_rm = RawMaterialPrices.objects.count()
	if(count_rm != 0):
		#change dates into some specific dates (%x-Local version of date-12/31/18)
		last_date = last_rm_quantity.date
		rear_date = last_date.strftime("%x")
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
			duplicate_quantiites = RawMaterialPrices.objects.create(date = datetime.datetime.now(),maize_bran = dup_maize_bran ,cotton = dup_cotton,
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

		#populate the product quantities model

		adding(product,maize_bran,cotton,sun_flower,fish,salt,general_purpose_premix,layers_premix,shells,meat_boaster,egg_boaster)

		form.save()
		
	context['form'] = form
	redirect('index')

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

def create_product_price(request):
	# dictionary for initial data with
	# field names as keys
	context = {}

	# add the dictionary during initialization
	form = ProductPriceForm(request.POST or None)

	if form.is_valid():
		form.save()
		#Its here that after the supply is made then we shall start populating the RawMaterialQuantities
		#table
		# we shall check if the "RawMaterialQuantities" table has atleast one row
		# compute_quantities()
	context['form'] = form

	return render(request, "create_product_price.html",context)

def viewing_product_prices(request):
   	#get the date from the user 
	start_date = request.GET.get('start_date')
	end_date = request.GET.get('end_date')

	# broilers_marsh,chick_marsh,old_pig,growers_marsh,layers_marsh ,young_pig 

	# run a query to get all the supplies on that date
	p_prices = ProductPrices.objects.filter(date__range=[start_date, end_date])

	# print(type(supplies))
     
	# return render(request, "view_supply.html", context)
	return render(request, "view_product_prices.html", {'p_prices':p_prices})

def updating_product_prices(request):
	context_dict = {}

	if 'id' in request.GET:
		pk = request.GET['id']

		print (pk)
		clean_pk = pk.strip("/")
		print (clean_pk)
		product_prices = ProductPrices.objects.get(id=clean_pk)
		form = ProductPriceForm(request.POST or None, instance=product_prices)
    
		if form.is_valid():
			
			form.save()

			redirect('view_product_prices.html')

		context_dict["form"] = form

	return render(request,"update_product_prices.html",context=context_dict)

def deleting_product_prices(request):

    # book= get_object_or_404(Book, pk=pk)  
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        product_price_to_delete = ProductPrices.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        product_price_to_delete.delete()
        redirect('view_product_prices.html')
        # if request.method =='POST':
        # 	#we get to know the item 

        #     supply_record_to_delete.delete()
        #     return redirect('view_supply.html')

        # context_dict["object"] = supply_record_to_delete
    return render(request, "delete_product_prices.html",context=context_dict)

def create_raw_material_prices(request):
	# dictionary for initial data with
	# field names as keys
	context = {}

	# add the dictionary during initialization
	form = RawMaterialPricesForm(request.POST or None)

	if form.is_valid():
		form.save()
		#Its here that after the supply is made then we shall start populating the RawMaterialQuantities
		#table
		# we shall check if the "RawMaterialQuantities" table has atleast one row
		# compute_quantities()
	context['form'] = form

	return render(request, "create_raw_material_prices.html",context)

def view_raw_material_prices(request):
	#get the date from the user 
	start_date = request.GET.get('start_date')
	end_date = request.GET.get('end_date')

	# broilers_marsh,chick_marsh,old_pig,growers_marsh,layers_marsh ,young_pig 

	# run a query to get all the supplies on that date
	r_m_prices = RawMaterialPrices.objects.filter(date__range=[start_date, end_date])

	# print(type(supplies))
     
	# return render(request, "view_supply.html", context)
	return render(request, "view_raw_material_prices.html", {'r_m_prices':r_m_prices})

def update_raw_material_prices(request):
	context_dict = {}

	if 'id' in request.GET:
		pk = request.GET['id']

		print (pk)
		clean_pk = pk.strip("/")
		print (clean_pk)
		product_prices = RawMaterialPrices.objects.get(id=clean_pk)
		form = RawMaterialPricesForm(request.POST or None, instance=product_prices)
    
		if form.is_valid():			
			form.save()
			redirect('view_raw_material_prices.html')
		context_dict["form"] = form

	return render(request,"update_raw_material_prices.html",context=context_dict)

def deleting_raw_material_prices(request):
	 # book= get_object_or_404(Book, pk=pk)  
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        product_price_to_delete = RawMaterialPrices.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        product_price_to_delete.delete()
        # redirect('view_product_prices.html')
        # if request.method =='POST':
        # 	#we get to know the item 

        #     supply_record_to_delete.delete()
        #     return redirect('view_supply.html')

        # context_dict["object"] = supply_record_to_delete
    return render(request, "delete_raw_material_prices.html",context=context_dict)

def viewing_product_catalog(request):
	#get the date from the user 
	start_date = request.GET.get('start_date')
	end_date = request.GET.get('end_date')

	# broilers_marsh,chick_marsh,old_pig,growers_marsh,layers_marsh ,young_pig 

	# run a query to get all the supplies on that date
	p_q = ProductQuantities.objects.filter(date__range=[start_date, end_date])

	l_p_q = ProductQuantities.objects.last()

	l_p_p = ProductPrices.objects.last()

	context = {}
	# add the dictionary during initialization
	form = ProductSalesForm(request.POST or None)
	if form.is_valid():
		#So here it means that if am deduct the quantity that has been bought,
		#i must do it for every raw material , that's what it means 
		# Get to know the particular product from the form
		product = form.cleaned_data['product']
		quantity = form.cleaned_data['quantity']	
		print("Hello we are now here")
		product_sales_quantity_deduction(product,quantity)
		
		form.save()
		
	#Adding items to the dictionary
	context['form'] = form
	context['p_q'] = p_q
	context['l_p_q'] = l_p_q
	context['l_p_p'] = l_p_p

	return render(request, "view_product_catalog.html", context)

def viewing_raw_material_catalog(request):
	#get the date from the user 
	# broilers_marsh,chick_marsh,old_pig,growers_marsh,layers_marsh ,young_pig 

	# run a query to get all the supplies on that date

	r_m_q = RawMaterialQuantities.objects.last()

	r_m_p = RawMaterialPrices.objects.last()

	context = {}
	# add the dictionary during initialization
	form = RawMaterialSalesForm(request.POST or None)
	if form.is_valid():
		#So here it means that if am deduct the quantity that has been bought,
		#i must do it for every raw material , that's what it means 
		# raw_material = form.cleaned_data['raw_material']
		# quantity = form.cleaned_data['quantity']
		# raw_material_sales_quantity_deduction(raw_material,quantity)
		form.save()
		
	context['form'] = form
	# So am suggesting that after the sale has been saved , then we deduct the quantities 
	last_sale = RawMaterialSales.objects.last()
	#then throw the variables to the deduction function
	raw_material_sales_quantity_deduction(last_sale.raw_material,last_sale.quantity)


	return render(request, "view_raw_material_catalog.html", {'r_m_q':r_m_q,'r_m_p':r_m_p ,'form':form ,})






	



