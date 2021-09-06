# Profit pen inventory system

# July 29th 21:51
# Setup Django project
# Setup Database
# Create the raw_materials model
```python
class RawMaterial(models.Model):
	date = models.DateField()
	receipt_number = CharField()
	supplier = models.CharField(max_length = 100)
	item = models.CharFieldField()
	quantity = models.IntegerField()
	unit_price = models.IntegerField()
	amount = models.IntegerField()
	def __str__(self):
		return self.date,self.supplier,self.item,self.unit_price,self.amount
```
# Include app in project
```python
INSTALLED_APPS = [
    'profit_pen_app.apps.ProfitPenAppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
# Make migrations
```python
python manage.py makemigrations
```
# migrate
```python
python manage.py migrate
```
# Give raw_materials model an admin interface
I went to the profit_pen_app/admin.py
```python
from .models import RawMaterial

admin.site.register(RawMaterial)
```
# Create a form
The forms.py file is to be located in the applications' directory

# Create a view in views.py

# Create a templates

# Retriview view
But to retriev the view in the way that i wanted i had to used some template tags

# CRUD products
Now its from mixtures that we get products
## create products
create the products model
September 1st 2021
Now as the the products are being created , we get to find out that we must subtract the quantity of 
the different ingredients that has been used but we do that by tackling one by one.
Steps involved in a backward way
1.We have a remaining quantity of a raw material
But before that , we had to 
2.Subtract the (inital quantity of the rawmaterial-the required quantity to make the product)
but before that we had to get the required quantity ? How 
3.```python
maize_bran = form.cleaned_data.get("maize_bran")
```
4.We also have to get the initial quantity of the raw material
Solutions
we are looking for quantity of a specific item , however what disturbs me is that the user might have another supply intake and this present logic will only subtract from that latest intake hence ignoring other previous intakes .

Hypothesis one
Am thinking of having another table that only collects the quantities of the specific rawmaterials. Incase we get to have another supply , the supply table is populated with new  and so is the new table which i will call the supply quantities, because there is just one row to edit , then i won't have to worry about other quantities.

September 2nd 2021
Steps (backward fashion)
We shall have a model called RawMaterial_Quantities
what should it include ?
maize_bran,cotton ,sun_flower ,salt ,layers_premix ,shells ,maize_boaster ,egg_boaster 

And How will they be populated?
We shall get all quantities of a particular raw material 

Get all the supplies which were of a particular raw_material
```python
 raw_shit = RawMaterial.objects.filter(item='Maize/bran')
```

Change the result of the query into a list
```python
raw_shit_list = list(raw_shit)
```

Create an empty list to store the quantites .For every item in the raw_shit_list,get the quantity attribute and add it to the empty list.After that update the supply_quantities table.

September 3rd 2021
Am thinking of writing a function to do all that because , i can't do it on my own.

September 6th 2021
i have created a function to do the subtraction and then also am using some messages to indicate to the user the level of inventory remaining of a certain raw material.
# github account token
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

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

September 2nd 2021
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
References
DJANGO CRUD
https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/

How to draw business process diagrams
http://www.umsl.edu/~sauterv/analysis/dfd/dfd_intro.html

Setup Django Project
https://docs.djangoproject.com/en/3.2/intro/tutorial01/

str-returned-non-string-type-tuple
https://stackoverflow.com/questions/39883950/str-returned-non-string-type-tuple

How to create custom template tags
https://docs.djangoproject.com/en/3.2/howto/custom-template-tags/

How to retrieve data from a django form 
http://www.learningaboutelectronics.com/Articles/How-to-retrieve-data-from-a-Django-form-Python.php
# Contributors 

Lutaro Ronnie 
