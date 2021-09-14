from django.db import models

# declare a new model with a name "GeeksModel"
class RawMaterial(models.Model):

	# fields of the model
	# date,receiptnumber,supplier,item,unit,quantity,amount
	date = models.DateField()
	receipt_number = models.CharField(max_length = 100)
	supplier = models.CharField(max_length = 100)
	#defining the choices

	item = models.CharField(max_length = 50)
	quantity = models.IntegerField()
	unit_price = models.IntegerField()
	#Am making this a null True because when the user is entering the supply data , am not able to make it appear
	#immediately , that's above my paygrade
	amount = models.IntegerField(default=0)
	transport = models.IntegerField()
	onloading = models.IntegerField()
	offloading = models.IntegerField()
	grinding = models.IntegerField()
	#Am making this a null True because when the user is entering the supply data , am not able to make it appear
	#immediately , that's above my paygrade
	cost_of_supply = models.IntegerField(default=0)
	pricing = models.IntegerField(default=0)


	# renames the instances of the model
	# with their title name
	def __str__(self):
		   
		return '{} {} {} {} {}'.format(self.date,self.supplier,self.item,self.unit_price,self.amount)

class Product(models.Model):
	date = models.DateField()
	product = models.CharField(max_length = 100)
	maize_bran = models.IntegerField(default=0)
	cotton = models.IntegerField(default=0)
	sun_flower = models.IntegerField(default=0)
	salt = models.IntegerField(default=0)
	layers_premix = models.IntegerField(default=0)
	shells = models.IntegerField(default=0)
	maize_boaster = models.IntegerField(default=0)
	egg_boaster = models.IntegerField(default=0)

	def __str__(self):
		return '{}'.format(self.product)


# maize_bran,cotton ,sun_flower ,salt ,layers_premix ,shells ,maize_boaster ,egg_boaster 

class RawMaterialQuantities(models.Model):
	date = models.DateField()
	maize_bran = models.IntegerField(default=0)
	cotton = models.IntegerField(default=0)
	sun_flower = models.IntegerField(default=0)
	salt = models.IntegerField(default=0)
	layers_premix = models.IntegerField(default=0)
	shells = models.IntegerField(default=0)
	maize_boaster = models.IntegerField(default=0)
	egg_boaster = models.IntegerField(default=0)

	def __str__(self):
		return '{}'.format(self.date)


