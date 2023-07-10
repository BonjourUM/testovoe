from django.core import serializers
from django.http import HttpResponse
from django.views.generic import ListView
from app.models import *


class ManufacturerListView(ListView):
    model = Manufacturer

    def get(self, *args, **kwargs):
        idr = kwargs.pop('id', None)
        manufacturer = Manufacturer.objects.filter(product_id__credit_request_id__credit__contract_id=idr).distinct()
        manufacturer = serializers.serialize('json', manufacturer)
        return HttpResponse(manufacturer)
