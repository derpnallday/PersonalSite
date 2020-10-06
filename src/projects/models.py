from django.db import models

# Create your models here.
class Project(models.Model):
	name		= models.CharField(max_length=20) #max length required
	year 		= models.IntegerField()
	link		= models.CharField(max_length=30)
	description = models.TextField(blank=True, null=True)

# Too make changes to models
# run manage.py makemigrateions
# run manage.py migrate

# Too add/remove attributes
# either set default value for new attribute or set null=True/default=True

# How to add to database with python
# 	from products.models import Product
# 	Product.objects.create(FIELDS=value)