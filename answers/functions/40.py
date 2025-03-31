import httpx
from datetime import datetime, timedelta
import json 
 
def get_weather_forecast():
    location_id = 1566083 # Default location ID for Ho Chi Minh City, Vietnam
    
    # Second API call to get weather data
    weather_url = f"https://weather-broker-cdn.api.bbci.co.uk/en/forecast/aggregated/{location_id}"

    with httpx.Client(timeout=30.0) as client:
        response = client.get(weather_url)

    weather_data = response.json()
    
    # Extract forecast data
    forecasts = {}
    for forecast in weather_data['forecasts']:
        date = forecast['summary']['report']['localDate']
        description = forecast['summary']['report']['enhancedWeatherDescription']
        forecasts[date] = description

    print(f"Forecast for Ho Chi Minh City, Vietnam:")
    print(json.dumps(forecasts, indent=2))    
    return forecasts

# weather_data = get_weather_forecast()
# print(json.dumps(weather_data, indent=2))