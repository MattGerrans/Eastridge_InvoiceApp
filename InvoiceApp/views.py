"""
API for simple implementation of an invoice challenge for Eastridge interview.

"""

from .models import Invoice, InvoiceItem
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from .serializers import InvoiceSerializer, InvoiceItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


def static_index(request):
    """
    Shows a boring static page for the root url.
    :param request: The request.
    :return: Static html page.
    """
    import os
    from glob import glob
    from . import settings
    current_directory = os.path.abspath(os.curdir)

    html = None
    html_file = ''
    if os.path.isdir(settings.STATICFILES_DIRS[0]):
        html_files = glob(os.path.join(settings.STATICFILES_DIRS[0], '*.html'))
        if html_files:
            html_file = html_files[0]
            if os.path.isfile(html_file):
                with open(html_file) as stream:
                    html = stream.read()

    if not html:
        red_cell = '<td><font color=red name=Consolas>'
        html = f"""<html>
        <head><title>Error Loading Page File</title></head>
        <body bgcolor=cyan text=Yellow>
        <h1>Error loading static page file; details:</h1>
        <table>
            <tr><td>Application current directory: {red_cell}{current_directory}
            <tr><td>Settings static directory:     {red_cell}{settings.STATICFILES_DIRS[0]}
            <tr><td>Settings static file:          {red_cell}{html_file}
        </body>
        </html>
        """

    html = html.replace('{url}', request.get_host())

    return HttpResponse(html)


@api_view(['GET', 'POST'])
def invoice_api(request):
    """
    Handles get and post for an Invoice.
    GET: Will list all invoices. POST will create a new invoice.
    :param request: The request.
    :return: The response.
    """
    if request.method == 'GET':
        invoices = Invoice.objects.all()
        invoice_serializer_list = InvoiceSerializer(invoices, many=True)
        return Response(invoice_serializer_list.data)
    elif request.method == 'POST':
        invoice_data = JSONParser().parse(request)
        invoice = Invoice(**invoice_data)
        invoice.save()
        return HttpResponse(invoice_data, status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def item_api(request, invoice_id):
    """
    Handles get and post for InvoiceItems.
    GET will get all invoice items for invoice with specified ID.
    POST:= will create an Invoice Item for the specified Invoice.
    :param request: The request.
    :param invoice_id: The id of the invoice.
    :return: The response.
    """
    try:
        invoice = Invoice.objects.get(pk=invoice_id)
        assert invoice.id == invoice_id
    except Invoice.DoesNotExist:
        return HttpResponse(status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        return get_invoice_items(request, invoice)
    elif request.method == 'POST':
        return post_invoice_item(request, invoice)


def get_invoice_items(request, invoice):
    """
    Get the invoice items for the invoice.
    :param request: The request.
    :param invoice: The invoice.
    :return: The response.
    """
    try:
        invoice_items = InvoiceItem.objects.filter(invoice_id__exact=invoice.id)
        serialized_invoice_items = [InvoiceItemSerializer(invoice_item) for invoice_item in invoice_items]
        return Response([s.data for s in serialized_invoice_items])
    except Invoice.DoesNotExist:
        return Response(status.HTTP_204_NO_CONTENT)
    except Invoice.MultipleObjectsReturned:
        return Response(status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)  # or 400


def post_invoice_item(request, invoice):
    """
    Post a new invoice item for this invoice.
    :param request: The request.
    :param invoice: The invoice.
    :return: The response.
    """
    invoice_item_data = JSONParser().parse(request)
    invoice_item_data['invoice'] = invoice
    invoice_item = InvoiceItem(**invoice_item_data)
    invoice_item.save()
    invoice_item_serializer = InvoiceItemSerializer(invoice_item)
    return Response(invoice_item_serializer.data, status.HTTP_201_CREATED)
