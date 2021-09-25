from .models import RawMaterial , Product , RawMaterialQuantities
import datetime

def subtracting(raw_material):
   #maize_bran_ingridient = form.cleaned_data['maize_bran']
   maize_bran_supply = RawMaterial.objects.filter(item=raw_material)
   #
   maize_bran_supply_list = list(maize_bran_supply)
   # Create an empty list to store the quantites 
   maize_bran_supply_quantities = []
   # For every item in the maize_bran_supply_list , get the quantity attribute and add it to the empty list.
   for quantity_attribute in maize_bran_supply_list:
      #get the value of the quantity
      value = quantity_attribute.quantity
      #populate the empty list
      maize_bran_supply_quantities.append(value)
      #get the sum of quantites inside the maize_bran_supply_quantities
   return sum(maize_bran_supply_quantities)

def compute_quantities():

   check_row = RawMaterialQuantities.objects.count()

   if check_row == 1:
      #here am going to introduct a function because item get the item that has been supplied
      #but first , i need to get it from the form
      #so here due the technical difficulty we shall not care to find out which specific item
      #at first was supplied
      
      #item_supplied = form.cleaned_data['item']
      
      # we also have to check if the Raw material model is populated or not
      check_supplies = RawMaterial.objects.count()

      if check_supplies == 1: 
         #we want to get the lastest value of a specific item
         #We just look through the RawMaterial model and look for last input of a specific item
         get_lastest_item_supplied = RawMaterial.objects.latest('-item')

         #here we are turning this occurance into a dictionary
         item_dict = get_lastest_item_supplied.__dict__

         #we might want to print the quantity, just for sastisfaction
         print(item_dict)
         #get the quantity from the dictionary 
         quantity_of_lastest_item = item_dict.get("quantity")
         # so we also get the specific item in the object because we shall use it to select the 
         #row to update 
         lastest_item_supplied = item_dict.get("item")
         #use these two variables quantity_of_lastest_item and lastest_item_supplied to update the row
         # the RawMaterialQuantities model
         if lastest_item_supplied == 'maize_bran':
            # quantity_update=RawMaterialQuantities.objects.filter(id = 1).update(maize_bran = quantity_of_lastest_item)
            # quantity_update = RawMaterialQuantities.objects.get(maize_bran)
            #get the current values inside the RawMaterialQuantities
            quantity_update = RawMaterialQuantities.objects.values('maize_bran')
            #since the values function returns a queryset , i have to change it into a list
            listform = list(quantity_update)
            specific_dict = listform[0]
            current_quantity = specific_dict.get("maize_bran")
            #now add both quantities from the Raw material table and RawMaterialQuantities table
            total_quantity = current_quantity + quantity_of_lastest_item
            #then now i can update the value inside the RawMaterialQuantites model
            quantity_addition = RawMaterialQuantities.objects.filter(id = 1).update(maize_bran = total_quantity)

   else:
      #create default quantities
     
      default_quantiites = RawMaterialQuantities.objects.create(date = datetime.datetime.now(),maize_bran = 0 ,cotton = 0,
                                                               sun_flower = 0, fish = 0,salt = 0 ,
                                                               general_purpose_premix = 0,layers_premix = 0,
                                                               shells = 0, meat_boaster = 0,egg_boaster=0)




