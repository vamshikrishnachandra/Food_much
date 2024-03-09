from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,'Home.html')

def Why_We_Choose_Section(request):
    return render(request,'WhyWeChooseSection.html')

def Explore_menu(request):
    return render(request,'Exploremenu.html')

def Delivery_And_Payment_Section(request):
    return render(request,'DeliveryAndPayment.html')