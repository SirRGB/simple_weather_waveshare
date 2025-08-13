import openmeteo_requests
import requests_cache
from retry_requests import retry

from parse_config import get_latitude, get_longitude, get_timezone

def get_weather_data() -> list:
    # Set up the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": get_latitude(),
        "longitude": get_longitude(),
        "current": ["temperature_2m", "rain"],
        "hourly": ["temperature_2m", "rain"],
        "timezone": get_timezone(),
        "forecast_days": 1,
        "forecast_hours": 5,
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]

    # Process current data. The order of variables needs to be the same as requested.
    current = response.Current()
    hourly_temp = [f"{current.Variables(0).Value():02.1f}"]
    hourly_rain = [f"{current.Variables(1).Value():02.1f}"]

    for time in range(5):
         # [value] [time]
        hourly_temp.append(f"{response.Hourly().Variables(0).Values(time):02.1f}")
        hourly_rain.append(f"{response.Hourly().Variables(1).Values(time):02.1f}")

    return [hourly_temp, hourly_rain]
