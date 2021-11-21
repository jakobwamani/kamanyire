from django import forms
from .models import RawMaterial , Product ,ProductPrices , RawMaterialPrices
from django.utils import timezone

RAW_MATERIAL_CHOICES = (("maize_bran" , "maize_bran"),("cotton", "cotton")
,("sun_flower" , "sun_flower")
,("fish" , "fish")
,("salt" ,"salt")
,("layers_premix" , "layers_premix")
,("general_purpose_premix" , "general_purpose_premix")
,("layers_premix" , "layers_premix")
,("shells" , "shells")
,("meat_boaster" , "meat_boaster")
,("egg_boaster" ,"egg_boaster"))
# creating a form
class RawMaterialForm(forms.ModelForm):

  	
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
    #birth_date= forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS))
	receipt_number = forms.IntegerField()
	supplier = forms.CharField()
	item = forms.ChoiceField(choices=RAW_MATERIAL_CHOICES)
	# item = forms.CharField()
	quantity = forms.IntegerField(disabled=True)
	increase_quantity = forms.IntegerField(initial=0)
	reduce_quantity = forms.IntegerField(initial=0)
	unit_price = forms.IntegerField()
	# i  cannot edit this stuff from right here so all amounts will shown in the retrieve view
	# amount = forms.IntegerField()
	transport = forms.IntegerField()
	onloading = forms.IntegerField()
	offloading = forms.IntegerField()
	grinding = forms.IntegerField()
	# i  cannot edit this stuff from right here so all amounts will shown in the retrieve view
	# fullamount = forms.IntegerField()
	# pricing = forms.IntegerField(help_text='First check to cost of supply to update this')
   
	# create meta class
	class Meta:
		# specify model to be used
		model = RawMaterial

		# exclude = ["amount","fullamount",]
		fields = [
			
			"date",
			"receipt_number",
			"supplier",
			"item","quantity","increase_quantity","reduce_quantity","unit_price", "transport","onloading","offloading","grinding",
		]

#supply form
class SupplyForm(forms.ModelForm):

  	
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
    #birth_date= forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS))
	receipt_number = forms.IntegerField()
	supplier = forms.CharField()
	item = forms.ChoiceField(choices=RAW_MATERIAL_CHOICES)
	# item = forms.CharField()
	quantity = forms.IntegerField()
	unit_price = forms.IntegerField()
	# i  cannot edit this stuff from right here so all amounts will shown in the retrieve view
	# amount = forms.IntegerField()
	transport = forms.IntegerField()
	onloading = forms.IntegerField()
	offloading = forms.IntegerField()
	grinding = forms.IntegerField()
	# i  cannot edit this stuff from right here so all amounts will shown in the retrieve view
	# fullamount = forms.IntegerField()
	# pricing = forms.IntegerField(help_text='First check to cost of supply to update this')
   
	# create meta class
	class Meta:
		# specify model to be used
		model = RawMaterial

		# exclude = ["amount","fullamount",]
		fields = [
			
			"date",
			"receipt_number",
			"supplier",
			"item","quantity","unit_price", "transport","onloading","offloading","grinding",
		]


# broilers_mash
# brown_salt
# calcium
# chick_mash
# coconut
# cotton_cake
# egg_boaster
# growers_mash
# layers_mash
# lime
# meat_boaster
PRODUCT_CHOICES = (("broilers_marsh","broilers_marsh")
,("chick_marsh","chick_marsh")
,("growers_marsh","growers_marsh")
,("old_pig","old_pig")
,("layers_marsh","layers_marsh")
,("young_pig","young_pig"))
class ProductForm(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	# date = forms.DateField()
	product = forms.ChoiceField(choices=PRODUCT_CHOICES)
	fish = forms.IntegerField(initial = 0)
	maize_bran = forms.IntegerField(initial = 0)
	cotton = forms.IntegerField(initial = 0)
	sun_flower = forms.IntegerField(initial = 0)
	salt = forms.IntegerField(initial = 0)
	layers_premix = forms.IntegerField(initial = 0)
	general_purpose_premix = forms.IntegerField(initial = 0)
	shells = forms.IntegerField(initial = 0)
	meat_boaster = forms.IntegerField(initial = 0)
	egg_boaster = forms.IntegerField( initial = 0)

	class Meta:
		model = Product

		fields = ["date","product","maize_bran","cotton","sun_flower","salt","layers_premix","general_purpose_premix","shells","meat_boaster","egg_boaster","fish"]


class ProductPriceForm(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	broilers_marsh = forms.IntegerField(initial = 0)
	chick_marsh = forms.IntegerField(initial = 0)
	old_pig = forms.IntegerField(initial = 0)
	growers_marsh = forms.IntegerField(initial = 0)
	layers_marsh = forms.IntegerField(initial = 0)
	young_pig = forms.IntegerField(initial = 0)

	class Meta:
		model = ProductPrices

		fields = ["date","broilers_marsh","chick_marsh","old_pig","growers_marsh","layers_marsh","young_pig"]



class RawMaterialPricesForm(forms.ModelForm):
	# quantity_id = models.AutoField(primary_key=True)
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	# date = models.DateField()
	maize_bran = forms.IntegerField(initial=0)
	cotton = forms.IntegerField(initial=0)
	sun_flower = forms.IntegerField(initial=0)
	fish = forms.IntegerField(initial=0)
	salt = forms.IntegerField(initial=0)
	general_purpose_premix = forms.IntegerField(initial=0)
	layers_premix = forms.IntegerField(initial=0)
	shells = forms.IntegerField(initial=0)
	meat_boaster = forms.IntegerField(initial=0)
	egg_boaster = forms.IntegerField(initial=0)

	class Meta:
		model = RawMaterialPrices

		fields = ["date","maize_bran","cotton","sun_flower","salt","layers_premix","general_purpose_premix","shells","meat_boaster","egg_boaster","fish"]


