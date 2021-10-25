from django import forms
from .models import RawMaterial , Product
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
PRODUCT_CHOICES = (("broilers_mash","broilers_mash")
,("chick_mash","chick_mash")
,("egg_boaster","egg_boaster")
,("growers_mash","growers_mash")
,("layers_mash","layers_mash")
,("meat_boaster","meat_boaster"))
class ProductForm(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	# date = forms.DateField()
	product = forms.ChoiceField(choices=PRODUCT_CHOICES)
	maize_bran = forms.IntegerField()
	cotton = forms.IntegerField()
	sun_flower = forms.IntegerField()
	salt = forms.IntegerField()
	layers_premix = forms.IntegerField()
	shells = forms.IntegerField()
	maize_boaster = forms.IntegerField()
	egg_boaster = forms.IntegerField()

	class Meta:
		model = Product

		fields = ["date","product","maize_bran","cotton","sun_flower","salt","layers_premix","shells","maize_boaster","egg_boaster"]
