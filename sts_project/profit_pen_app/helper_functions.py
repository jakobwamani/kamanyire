: def subtracting(raw_material):
   ...:     #maize_bran_ingridient = form.cleaned_data['maize_bran']
   ...:     maize_bran_supply = RawMaterial.objects.filter(item=raw_material)
   ...:     #
   ...:     maize_bran_supply_list = list(maize_bran_supply)
   ...:     # Create an empty list to store the quantites 
   ...:     maize_bran_supply_quantities = []
   ...:     # For every item in the maize_bran_supply_list , get the quantity attribute and add it to the empty list.
   ...:     for quantity_attribute in maize_bran_supply_list:
   ...:         #get the value of the quantity
   ...:         value = quantity_attribute.quantity
   ...:         #populate the empty list
   ...:         maize_bran_supply_quantities.append(value)
   ...:     #get the sum of quantites inside the maize_bran_supply_quantities
   ...:     return sum(maize_bran_supply_quantities)
   ...: 
