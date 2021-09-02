from django.shortcuts import render
from property.models import Property

def homePage(request):
    property_list = Property.objects.all()
    context = {
        'property_list': property_list,
        'title': 'Home'
    }
    return render(request, 'rokayproperties/home.html', context)

def contactPage(request):
    context = {
        'title': 'Contact'
    }
    return render(request, 'rokayproperties/contact.html', context)
