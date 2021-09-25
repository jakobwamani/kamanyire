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

# Major issue September 15th 2021
Am running into a major issue right now, I have a raw materials table and a product table , when a product is being created , bits of the rawmaterials are used but how , 
they are picked directly from the supply table and then put into a list but the challenge is that , i wont know which value of the rawmaterial to reduct when the product is being created .

So what if i create another table that pulls all totals of the raw materials in one place not just
record like a ledgder.

so this is the plan , the result is to have a one value representing the quantity of specific rawmaterial owned by the business

but before that we have all the values put in a list then into that table .
Name of the table let it be raw_material_quantities 

```python
class RawMaterialQuantities(models.Model):
	date = models.DateField()
	maize_bran = models.IntegerField(default=0)
	cotton = models.IntegerField(default=0)
	sun_flower = models.IntegerField(default=0)
	fish = models.IntegerField(default=0)
	salt = models.IntegerField(default=0)
	general_purpose_premix = models.IntegerField(default=0)
	layers_premix = models.IntegerField(default=0)
	shells = models.IntegerField(default=0)
	meat_boaster = models.IntegerField(default=0)
	egg_boaster = models.IntegerField(default=0)

	def __str__(self):
		return '{}'.format(self.date)
```

So after creating this model , that will act as a good place for us to store our quantities of different raw materials .
Now the question is how do we get to store those quantites in there.
## These are the different ways in which we shall innteract with this model
#### 1.when a supply is made 
we shall get all the quantites of a specific raw materials put them in a list 
Sum up that list and store the sum inside the raw_material_quantites model 
To make it also clear we can't have a date on that model.
from then on we shall just be editing .
Must make sure that from then one we shall be editing not like creating a new input 

#### 2.when a supply is edited
Here we will edit that one row inside that RawmaterialQuantities table  
#### 3.when a supply is deleted
Here again we will still edit this stuff out .
#### 4.when a product is being made
Here we will again edit that one row , there is nothing like creating a new row.
#### 5.when a product is being edited 
Just updating that one row
#### 6.when a product is being deleted
Just updating that one row.

# September 18th 2021
#### Creation of a supply
So this is how we are going to do this .
Have the model "RawMaterialQuantites" populated
How
Check if the "RawMaterialQuantities" table has a row , if true
-We must make sure the "RawMaterialQuantities" table has initial values of zeros such that we can 
update it (i had to do this manually)
-We just add the last most quantity of a specific quantity to the quantity inside the "RawMaterialQuantites"
if false
-Look for the quantities of specific raw materials in the raw material model
-Put them in a list and sumup them up and then push that quantity inside "RawMaterialQuantites"

Now we are going to do this for every item so i think we are going to use a function.
This code will run we are trying to create a supply.

#### Edition of a supply
So we are check if the "RawMaterialQuantities" model is populated with one row
IF TRUE
We look for the quantities of that specific raw material in the "raw material" model
Put them in a list and sum them up and change that quantity value in the "RawMaterialQuantities" model

IF FALSE
the "RawMaterialQuantities" can't be empty

#### Deletion of a supply
So we check if the "RawMaterialQuantities" model is populated with one row 
IF TRUE
We look for that specific raw material in the raw material table , delete it 
then again we look for the quantites of that specific raw material in the "raw material table"
Put them in a list and then sum them up and change that quantity value in the "RawMaterialQuantites"

#### Creation of a product 
# September 20th 2021
i found out that , i lost the documentation of the whole project so , i should draw again  

So we check and see if the "RawMaterialQuantities" model is populated with one row.

IF TRUE
We reduce a specific quantity in the "RawMaterialQuantities" model and update it 

IF FALSE
the "RawMaterialQuantities" can't be empty

#### Edition of a product
So we make a change of a specific raw_material in the "product" model 
and againg make that change inside the "RawMaterialQuantities" model
We are doing all of this inorder to have one table of truth.

#### Deletion of a product 
So we get to know the different raw_materials in a specific product 
Then we subtract each of them from the RawMaterialQuantites table
and then we update the RawMaterialQuantities


# github account token
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

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

September 2nd 2021
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

September 15th 2021
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

September 22th 2021
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
