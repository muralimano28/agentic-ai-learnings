from dotenv import load_dotenv
from fastapi import FastAPI
from app.services.weather_service import WeatherService

# Load environment variables
load_dotenv()

app = FastAPI()
weather_service = WeatherService()


@app.get("/weather")
async def read_root(cities: str):
    # Just like map in js
    city_list: list[str] = [city.strip().lower()
                            for city in cities.split(',')]

    # _status, weather_data = await weather_service.get_weather_for_cities(city_list)
    weather_data = await weather_service.get_weather_for_cities_with_retry(city_list)

    return weather_data
