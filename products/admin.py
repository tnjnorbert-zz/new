from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	date_hierarchy="timestamp"
	search_fields=['title','description','price','active']
	list_display =['title','price','active','updated']
	list_editable=['price','active']
	list_filter=['price','active','updated']
	readonly_fields=['timestamp','updated']
	prepopulated_fields={"slug":("title",)}
	class Meta:
		model = Product
			

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
