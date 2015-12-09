from django.db import models

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=120, null=False, blank=False)
	description = models.TextField(null=False, blank=False)
	price = models.DecimalField(decimal_places=2,max_digits=100,default=0.00)
	slug = models.SlugField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.title
	class Meta:
		unique_together=('title','slug')
			

class ProductImage(models.Model):
	product=models.ForeignKey(Product)
	image = models.ImageField(upload_to='products/images/')
	featured = models.BooleanField(default=False)
	thumbnail=models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	updated=models.DateTimeField(auto_now_add=False,auto_now=True)

	def __unicode__(self):
		return self.product.title

		