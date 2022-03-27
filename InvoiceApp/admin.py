from django.contrib import admin
from .models import Invoice, InvoiceItem

# [Django AttributeError: 'Alias' object has no attribute 'urls'](https://stackoverflow.com/questions/40833324/django-attributeerror-alias-object-has-no-attribute-urls)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
