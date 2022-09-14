from multiprocessing import context
from django.shortcuts import render
from katalog.models import CatalogItem 

# TODO: Create your views here.
def show_catalog(request):
    data_barang = CatalogItem.objects.all()
    context = {
        "list_barang": data_barang,
        "nama": "Ahmad Hanif",
        "npm": "2106750603"
    }
    return render(request, "katalog.html", context)
