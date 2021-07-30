from django.db import models

# declare a new model with a name "GeeksModel"
class RawMaterial(models.Model):

	# fields of the model
	# date,receiptnumber,supplier,item,unit,quantity,amount
	date = models.DateField()
	receipt_number = models.CharField(max_length = 100)
	supplier = models.CharField(max_length = 100)
	item = models.CharField(max_length = 50)
	quantity = models.IntegerField()
	unit_price = models.IntegerField()
	#Am making this a null True because when the user is entering the supply data , am not able to make it appear
	#immediately , that's above my paygrade
	amount = models.IntegerField(null=True)
	transport = models.IntegerField()
	onloading = models.IntegerField()
	offloading = models.IntegerField()
	grinding = models.IntegerField()
	#Am making this a null True because when the user is entering the supply data , am not able to make it appear
	#immediately , that's above my paygrade
	fullamount = models.IntegerField(null=True)


	# renames the instances of the model
	# with their title name
	def __str__(self):
		   
		return '{} {} {} {} {}'.format(self.date,self.supplier,self.item,self.unit_price,self.amount)

