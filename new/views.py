from django.shortcuts import redirect, render
import requests
import json
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        
        urls = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=2aab3bf369477bc517eee2ae66b0c974'
        data=requests.get(urls)
        data=data.json()
        if 'main' in data:
            
            city_weather = {
                "city":city,
                'Temparature':data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }
            return render(request,'new/home.html',{'data':city_weather})
        else:
            messages.error(request,'this city does not exist')
            return render(request,'new/home.html')
        
        
    return render(request,'new/home.html')