from rest_framework import serializers
from .models import Invoice, InvoiceItem


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'created_date']


class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ['id', 'units', 'description', 'amount']

"""
class Junk(serializers.Serializer):
    def create(self, validated_data):
        return Invoice.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.invoice = validated_data.get('invoice', instance.invoice)
        instance.units = validated_data.get('units', instance.units)
        instance.description = validated_data.get('description', instance.description)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.save()
        return instance
"""

