from django import forms
from .models import RawMaterial , Product
from django.utils import timezone


# creating a form
class RawMaterialForm(forms.ModelForm):

  	
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
    #birth_date= forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS))
	receipt_number = forms.IntegerField()
	supplier = forms.CharField()
	item = forms.CharField()
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


class ProductForm(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	# date = forms.DateField()
	product = forms.CharField()
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
