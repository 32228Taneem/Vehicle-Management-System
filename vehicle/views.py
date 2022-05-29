from django.shortcuts import render, redirect
from . models import Vehicle
from django.contrib import messages

# Create your views here.
def delete_vehicle(request,vehicle_id):
    vehicle = Vehicle.objects.get(pk=vehicle_id)
    vehicle.delete()
    return redirect('vehicle-list')

def vehicle_details(request,vehicle_id):
    vehicle = Vehicle.objects.get(pk=vehicle_id)
    return render(request,'vehicle/vehicle_details.html',{
        "vehicle" : vehicle
    })


def update_vehicle(request,vehicle_id):
    vehicle = Vehicle.objects.get(pk=vehicle_id)
    if request.method == 'POST':
        vehicle.name = request.POST['vehicle-name']
        vehicle.brand = request.POST['brand-name']
        vehicle.location = request.POST['location']
        vehicle.speed = request.POST['speed']
        vehicle.avg_speed = request.POST['avg-speed']
        vehicle.temperature = request.POST['temperature']
        vehicle.fuel_level = request.POST['fuel-level']
        vehicle.engine = request.POST['engine']
        vehicle.camera1 = request.POST['camera1']
        vehicle.camera2 = request.POST['camera2']
        vehicle.save()
        messages.success(request,("Product updated successfully"))
        return redirect('vehicle-list')
    return render(request,'vehicle/update_vehicle.html',{
        "vehicle" : vehicle
    })

def search_vehicle(request):
    if request.method == "POST":
        searched = request.POST['searched']
        vehicles = Vehicle.objects.filter(name__contains=searched)
        return render(request,'vehicle/vehicle_list.html',{
            "vehicles" : vehicles
            })
    else:
        return render(request,'events/search_venue.html',{})

def add_vehicle(request):
    if request.method == "POST":
        name = request.POST['vehicle-name']
        brand = request.POST['brand-name']
        location = request.POST['location']
        speed = request.POST['speed']
        avg_speed = request.POST['avg-speed']
        temperature = request.POST['temperature']
        fuel_level = request.POST['fuel-level']
        engine = request.POST['engine']
        camera1 = request.POST['camera1']
        camera2 = request.POST['camera2']

        vehicle = Vehicle(name=name,brand=brand,location=location,speed=speed,avg_speed=avg_speed,temperature=temperature,fuel_level=fuel_level,engine=engine,camera1=camera1,camera2=camera2)
        vehicle.save()
        messages.success(request,("Registered Successfully...Log In Now..."))
        return redirect('add-vehicle')
    else:
        return render(request,'vehicle/add_vehicle.html',{})


def vehicle_list(request):
    vehicles = Vehicle.objects.all().order_by('name')
    return render(request,'vehicle/vehicle_list.html',{
        "vehicles" : vehicles
    })


def home(request):
    return render(request,'vehicle/home.html',{})
