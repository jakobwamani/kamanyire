from .models import RawMaterial , Product , RawMaterialQuantities , ProductQuantities
import datetime

def subtracting(a,mai,cot,sun,fis,sal,gpp,lyp,she,meb,egb):
   instance = RawMaterialQuantities.objects.last()
   #subtract the current information , maize bran
   current_maize = instance.maize_bran - mai
   #
   instance.maize_bran = current_maize
   instance.save()
   #cotton
   current_cotton = instance.cotton - cot
   instance.cotton = current_cotton
   instance.save()
   #sun_flower
   current_sun_flower = instance.sun_flower - sun
   instance.sun_flower = current_sun_flower
   instance.save()
   #fish
   current_fish = instance.fish - fis
   instance.fish = current_fish
   instance.save()
   #salt
   current_salt = instance.salt - sal
   instance.salt = current_salt
   instance.save()
   #general_purpose_premix
   current_general_purpose_premix = instance.general_purpose_premix - gpp
   instance.general_purpose_premix = current_general_purpose_premix
   instance.save()
   #layers_premix
   current_layers_premix = instance.layers_premix - lyp
   instance.layers_premix = current_layers_premix
   instance.save()
   #shells
   current_shells = instance.shells - she
   instance.shells = current_shells
   instance.save()
   #meat_boaster
   current_meat_boaster = instance.meat_boaster - meb
   instance.meat_boaster = current_meat_boaster
   instance.save()
   #egg_boaster
   current_egg_boaster = instance.egg_boaster - egb
   instance.egg_boaster = current_egg_boaster
   instance.save()

def compute_quantities():
   check_row = RawMaterialQuantities.objects.count()

   if check_row >= 1:
      #here am going to introduct a function because item get the item that has been supplied
      #but first , i need to get it from the form
      #so here due the technical difficulty we shall not care to find out which specific item
      #at first was supplied   
      # we also have to check if the Raw material model is populated or not
      check_supplies = RawMaterial.objects.count()

      if check_supplies >= 1: 
         #we want to get the lastest value of a specific item
         #We just look through the RawMaterial model and look for last input of a specific item
         # get_lastest_item_supplied = RawMaterial.objects.latest('-item')
         get_lastest_item_supplied = RawMaterial.objects.last()
         quantity_of_lastest_item  = get_lastest_item_supplied.quantity
         lastest_item_supplied     = get_lastest_item_supplied.item
         #use these two variables quantity_of_lastest_item and lastest_item_supplied to update the row
         # the RawMaterialQuantities model
         if lastest_item_supplied == 'maize_bran':
            #get the current values inside the RawMaterialQuantities
            quantity_update = RawMaterialQuantities.objects.last()
            current_quantity = quantity_update.maize_bran
            #now add both quantities from the Raw material table and RawMaterialQuantities table
            total_quantity = current_quantity + quantity_of_lastest_item
            #then now i can update the value inside the RawMaterialQuantites model       
            # #i proceed to update the RMQ table
            quantity_addition = RawMaterialQuantities.objects.last()
            quantity_addition.maize_bran = total_quantity
            quantity_addition.save() 

         elif lastest_item_supplied == 'cotton':
            quantity_cotton_update = RawMaterialQuantities.objects.last()
            current_cotton_quantity = quantity_cotton_update.cotton
            total_cotton_quantity = current_cotton_quantity + quantity_of_lastest_item
            quantity_cotton_addition = RawMaterialQuantities.objects.last()
            quantity_cotton_addition.cotton = total_cotton_quantity
            quantity_cotton_addition.save()

         elif lastest_item_supplied == 'sun_flower':
            quantity_update = RawMaterialQuantities.objects.last()
            current_quantity = quantity_update.sun_flower
            total_quantity = current_quantity + quantity_of_lastest_item
            quantity_addition = RawMaterialQuantities.objects.last()
            quantity_addition.sun_flower = total_quantity
            quantity_addition.save()

         elif lastest_item_supplied == 'fish':
            quantity_update = RawMaterialQuantities.objects.last()
            current_quantity = quantity_update.fish
            total_quantity = current_quantity + quantity_of_lastest_item
            quantity_addition = RawMaterialQuantities.objects.last()
            quantity_addition.fish = total_quantity
            quantity_addition.save()

         elif lastest_item_supplied == 'salt':
            quantity_update = RawMaterialQuantities.objects.last()
            current_quantity = quantity_update.salt
            total_quantity = current_quantity + quantity_of_lastest_item
            quantity_addition = RawMaterialQuantities.objects.last()
            quantity_addition.salt = total_quantity
            quantity_addition.save()

         elif lastest_item_supplied == 'layers_premix':
            quantity_update = RawMaterialQuantities.objects.last()
            current_quantity = quantity_update.layers_premix
            total_quantity = current_quantity + quantity_of_lastest_item
            quantity_addition = RawMaterialQuantities.objects.last()
            quantity_addition.layers_premix = total_quantity
            quantity_addition.save()

         elif lastest_item_supplied == 'general_purpose_premix':
            quantity_update = RawMaterialQuantities.objects.last()
            current_quantity = quantity_update.general_purpose_premix
            total_quantity = current_quantity + quantity_of_lastest_item
            quantity_addition = RawMaterialQuantities.objects.last()
            quantity_addition.general_purpose_premix = total_quantity
            quantity_addition.save()

         elif lastest_item_supplied == 'shells':
            quantity_update = RawMaterialQuantities.objects.last()
            current_quantity = quantity_update.shells
            total_quantity = current_quantity + quantity_of_lastest_item
            quantity_addition = RawMaterialQuantities.objects.last()
            quantity_addition.shells = total_quantity
            quantity_addition.save()

         elif lastest_item_supplied == 'meat_boaster':
            quantity_update = RawMaterialQuantities.objects.last()
            current_quantity = quantity_update.meat_boaster
            total_quantity = current_quantity + quantity_of_lastest_item
            quantity_addition = RawMaterialQuantities.objects.last()
            quantity_addition.meat_boaster = total_quantity
            quantity_addition.save()

         elif lastest_item_supplied == 'egg_boaster':
            quantity_update = RawMaterialQuantities.objects.last()
            current_quantity = quantity_update.egg_boaster
            total_quantity = current_quantity + quantity_of_lastest_item
            quantity_addition = RawMaterialQuantities.objects.last()
            quantity_addition.egg_boaster = total_quantity
            quantity_addition.save()

   elif check_row == 0:
      #create default quantities
     
      default_quantiites = RawMaterialQuantities.objects.create(date = datetime.datetime.now(),maize_bran = 0 ,cotton = 0,
                                                               sun_flower = 0, fish = 0,salt = 0 ,
                                                               general_purpose_premix = 0,layers_premix = 0,
                                                                shells = 0, meat_boaster = 0,egg_boaster=0)
      #next thing that we need to do is to populate the RawmaterialQuantities table
      #with the initial values
      #get the item inside the raw materials model and then update the row in RMQ model
      #that specific quantity
      #after populating them with initial value , then i will also have to populate that 
      #latest value inside the RMQ table
      lastest_supply = RawMaterial.objects.last()
      #here we are turning this occurance into a dictionary
      #we might want to print the quantity, just for sastisfaction
      #get the quantity from the dictionary 
      quantity_of_supply = lastest_supply.quantity
      #but still i must change the quantity_of_lastest_item into an int for it to
      #work properly
      # so we also get the specific item in the object because we shall use it to select the 
      #row to update 
      item_of_supply = lastest_supply.item
      #use these two variables quantity_of_lastest_item and lastest_item_supplied to update the row
      # the RawMaterialQuantities model
      if item_of_supply == 'maize_bran':
         #get the current values inside the RawMaterialQuantities
         quantity_update              = RawMaterialQuantities.objects.last()
         current_quantity             = quantity_update.maize_bran
         #now add both quantities from the Raw material table and RawMaterialQuantities table
         total_quantity               = current_quantity + quantity_of_supply
         #then now i can update the value inside the RawMaterialQuantites model          
         quantity_addition            = RawMaterialQuantities.objects.last()
         quantity_addition.maize_bran = total_quantity
         quantity_addition.save()

      elif item_of_supply == 'cotton':
         cotton_update           = RawMaterialQuantities.objects.last()
         cotton_quantity         = cotton_update.cotton
         total_cotton_quantity   = cotton_quantity + quantity_of_supply           
         cotton_addition         = RawMaterialQuantities.objects.last()
         cotton_addition.cotton  = total_cotton_quantity
         cotton_addition.save()

      elif item_of_supply == 'sun_flower':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.sun_flower
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.sun_flower  = total_quantity
         addition.save()

      elif item_of_supply == 'fish':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.fish
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.fish  = total_quantity
         addition.save()

      elif item_of_supply == 'salt':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.salt
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.salt  = total_quantity
         addition.save()

      elif item_of_supply == 'layers_premix':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.layers_premix
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.layers_premix  = total_quantity
         addition.save()

      elif item_of_supply == 'general_purpose_premix':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.general_purpose_premix
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.general_purpose_premix  = total_quantity
         addition.save()

      elif item_of_supply == 'shells':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.shells
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.shells = total_quantity
         addition.save()

      elif item_of_supply == 'meat_boaster':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.meat_boaster
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.meat_boaster = total_quantity
         addition.save()

      elif item_of_supply == 'egg_boaster':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.egg_boaster
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.egg_boaster = total_quantity
         addition.save()

def reduce_due_to_deletion(supply_item,supply_quantity):
   # maize_bran,cotton,sun_flower,fish,salt,general_purpose_premix,layers_premix ,shells 
   # ,meat_boaster ,egg_boaster 
   if supply_item == "maize_bran":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.maize_bran
      quantity_update = current_quantity - supply_quantity
      instance.maize_bran = quantity_update
      instance.save()

   elif supply_item == "cotton":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.cotton
      quantity_update = current_quantity - supply_quantity
      instance.cotton = quantity_update
      instance.save()

   elif supply_item == "sun_flower":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.sun_flower
      quantity_update = current_quantity - supply_quantity
      instance.sun_flower = quantity_update
      instance.save()

   elif supply_item == "fish":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.fish
      quantity_update = current_quantity - supply_quantity
      instance.fish = quantity_update
      instance.save()

   elif supply_item == "salt":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.salt
      quantity_update = current_quantity - supply_quantity
      instance.salt = quantity_update
      instance.save()

   elif supply_item == "general_purpose_premix":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.general_purpose_premix
      quantity_update = current_quantity - supply_quantity
      instance.general_purpose_premix = quantity_update
      instance.save()

   elif supply_item == "layers_premix":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.layers_premix
      quantity_update = current_quantity - supply_quantity
      instance.layers_premix = quantity_update
      instance.save()

   elif supply_item == "shells":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.shells
      quantity_update = current_quantity - supply_quantity
      instance.shells = quantity_update
      instance.save()

   elif supply_item == "meat_boaster":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.meat_boaster
      quantity_update = current_quantity - supply_quantity
      instance.meat_boaster = quantity_update
      instance.save()

   elif supply_item == "egg_boaster":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.egg_boaster
      quantity_update = current_quantity - supply_quantity
      instance.egg_boaster = quantity_update
      instance.save()

   return print("Numbers successfully reduced")

def compute_product_quantities():
   print("Today shit was tuff , just had to repeat the whole thing")
   # new quantity of broilers_marsh is gotten by summing up all the quantities of the last instance in product model
   # Current quantity of broilers_marsh? i will probe the pq model for last instance
   # have the current quantity of broilers_marsh
   # also the new quantity of broilers_marsh
   # add the quantity of broilers_marsh
   # Do any products exist 
   
   #do the same for Raw material quantities
   if ProductQuantities.objects.count() == 0:
      create_them = ProductQuantities.objects.create(date = datetime.datetime.now(), broilers_marsh = 0 , chick_marsh = 0 , old_pig = 0 , growers_marsh =0 ,
                     layers_marsh = 0 , young_pig = 0)

   else:
      if Product.objects.count() == 0:
         #create the product 
         make = Product.objects.create(date= datetime.datetime.now(),product="broilers_marsh",maize_bran = 0,
                  cotton = 0 , sun_flower = 0 , salt = 0 , layers_premix = 0 ,shells = 0, meat_boaster = 0 , egg_boaster = 0 , fish = 0, general_purpose_premix = 0  )
         print("A product has been created")
      else:
         last_product = Product.objects.last()
         #we are going to get all the attributes of the last instance 
         mb = last_product.maize_bran
         co = last_product.cotton
         sf = last_product.sun_flower
         fi = last_product.fish
         sa = last_product.salt
         gpp = last_product.general_purpose_premix
         lp = last_product.layers_premix
         sh = last_product.shells
         mb = last_product.meat_boaster
         eb = last_product.egg_boaster
         # add them together
         last_quantity = mb + co + sf + fi + sa + gpp + lp + sh + mb + eb 

         current_quantity = ProductQuantities.objects.last()
         if last_product.product == "broilers_marsh":
            current_bm = current_quantity.broilers_marsh
            #add the stuff together
            summation = current_bm + last_quantity
            #we go update the broilers_marsh
            current_quantity.broilers_marsh = summation
            current_quantity.save()

def adding(product,maize_bran,cotton,sun_flower,fish,salt,general_purpose_premix,layers_premix,shells,meat_boaster,egg_boaster):   
   #here we are getting the product from the form
   #we could first add up all the rawmats and have one figure
   total_quantity = maize_bran + cotton + sun_flower + fish + salt + general_purpose_premix + layers_premix + shells + meat_boaster + egg_boaster
   last_quantity = ProductQuantities.objects.last()
   if product == "broilers_marsh":
      item = last_quantity.broilers_marsh 
      new_quantity = total_quantity + item
      last_quantity.broilers_marsh = new_quantity
      last_quantity.save()

   elif product == "chick_marsh":
      item = last_quantity.chick_marsh
      new_quantity = total_quantity + item
      last_quantity.chick_marsh = new_quantity
      last_quantity.save()

   elif product == "old_pig":
      item = last_quantity.old_pig
      new_quantity = total_quantity + item
      last_quantity.old_pig = new_quantity
      last_quantity.save()

   elif product == "growers_marsh":
      item = last_quantity.growers_marsh
      new_quantity = total_quantity + item
      last_quantity.growers_marsh = new_quantity
      last_quantity.save()

   elif product == "layers_marsh":
      item = last_quantity.layers_marsh
      new_quantity = total_quantity + item
      last_quantity.layers_marsh = new_quantity
      last_quantity.save()

   elif product == "young_pig":
      item = last_quantity.young_pig
      new_quantity = total_quantity + item 
      last_quantity.young_pig = new_quantity
      last_quantity.save()


         


      

















