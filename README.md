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

# github account token
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

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
