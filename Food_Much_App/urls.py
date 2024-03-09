from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.Home,name='Home'),
    path('WhyChooseUs',views.Why_We_Choose_Section,name='WhyWeChooseSection'),
    path('ExploreMenuSection/',views.Explore_menu,name='ExploreMenuSection'),
    path('DeliveryAndPaymentSection',views.Delivery_And_Payment_Section,name='DeliveryAndPaymentSection'),
    
   
]