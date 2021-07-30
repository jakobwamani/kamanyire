from django import forms
from .models import RawMaterial
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
	amount = forms.IntegerField()
    # year = forms.ChoiceField(choices=year_choices)


	# create meta class
	class Meta:
		# specify model to be used
		model = RawMaterial

		# specify fields to be used
		# YEARS= [x for x in range(2020,2025)]
  		# date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())


		fields = [
			
			"date",
			"receipt_number",
			"supplier",
			"item",
			"quantity",
			"unit_price", 
			"amount",
		]
