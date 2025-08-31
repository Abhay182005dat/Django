from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    url = "https://api.open-meteo.com/v1/forecast"
    city_name = request.GET.get('city') # 'Delhi' if user typed Delhi
    weather_data = {}
    error_message = None
    if city_name:
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}"
        response = requests.get(geo_url).json()
        print(response)
        if 'results' in response:
            latitude = response['results'][0]['latitude']
            longitude = response['results'][0]['longitude']
            latitude = float(latitude)
            longitude = float(longitude)
            params = {
                "latitude": latitude,
                "longitude": longitude,
                "hourly": "temperature_2m,weathercode,windspeed_10m,relative_humidity_2m,weather_code",
                "daily": "temperature_2m_max,temperature_2m_min",
                "timezone": "Asia/Kolkata"
            }
            response = requests.get(url , params=params)
            print(response)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'temperature' : data['hourly']['temperature_2m'][0],
                    'wind_speed' : data['hourly']['windspeed_10m'][0],
                    'humidity' : data['hourly']['relative_humidity_2m'][0],
                    'city': city_name
                }
        else:
            error_message = "City not found"

    context = {
        'weather' : weather_data,
        'city_name' : city_name,
        'error': error_message
    }
    print("Weather Data:", weather_data)
    print("Error:", error_message)

    return render(request , 'weather_app/index.html',context)