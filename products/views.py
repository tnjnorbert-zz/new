from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
	username_is="norbert tumukunde"
	context={"username_is":username_is}
	template='home.html'
	return render(request,template,context)

def all(request):
	products = Product.objects.all()
	context = {'products': products}
	template="all_products.html"
	return render(request,template,context) 

def single(request, slug):
	try:
		product = Product.objects.get(slug=slug)
		context = {'product': product}
		template = 'single_product.html'
		return render(request, template, context)
	except :
		raise Http404
		