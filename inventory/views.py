# Views implement the control layer of MVC.  That's not
# confusing at all.

from django.shortcuts import render
from django.http import Http404

# Don't need this any more but it's used for returning raw
# strings instead of routing to templates.
# from django.http import HttpResponse

from inventory.models import Item


def index(request):
	items = Item.objects.exclude(amount = 0)
	# Render creates the HTTP response and wires the view to
	# a template.  First parameter is the request object, second
	# is the template file to render.  Last parameter is a list
	# where the key is the variable name used by the template and
	# the value is the data which is passed.
	return render(request, 'inventory/index.html', {
		'items': items,
	})

def item_detail(request, id):
	# This try/except block is used to catch queries to items which
	# don't exist.
	try:
		item = Item.objects.get(id = id)
	except Item.DoesNotExist:
		raise Http404('This item does not exist.')

	return render(request, 'inventory/item_detail.html', {
		'item': item
	})
