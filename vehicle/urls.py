from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('vehicle_list',views.vehicle_list,name="vehicle-list"),
    path('add_vehicle',views.add_vehicle,name="add-vehicle"),
    path('search_vehicle',views.search_vehicle,name="search-vehicle"),
    path('update_vehicle/<vehicle_id>',views.update_vehicle,name="update-vehicle"),
    path('vehicle_details/<vehicle_id>',views.vehicle_details,name="vehicle-details"),
    path('delete_vehicle/<vehicle_id>',views.delete_vehicle,name="delete-vehicle"),
]