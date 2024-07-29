from django.shortcuts import render
from .models import Chai_Variety, Store
from django.shortcuts import get_object_or_404
from .forms import Chai_Variety_Form

def all_first_app(request):
    chais = Chai_Variety.objects.all()
    return render(request, "firstapp/all_firstapp.html", {"chais": chais})

def chai_detail(request,chai_id):
    chai = get_object_or_404(Chai_Variety,pk = chai_id)
    return render(request,"firstapp/chai_detail.html",{"chai" : chai})

def chai_store_view(request):
    stores = None
    if request.method == "POST":
        form = Chai_Variety_Form(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data["chai_variety"]
            stores = Store.objects.filter(chai_varieties = chai_variety)
    else:
        form = Chai_Variety_Form()
    return render(request,"firstapp/chai_stores.html",{"stores" : stores, "form" : form})
