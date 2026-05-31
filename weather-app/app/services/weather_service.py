import os
import asyncio
import httpx
from app.models.weather import Weather

weather_api_base_url = os.environ.get("WEATHER_API_BASE_URL")
weather_api_app_id = os.environ.get("WEATHER_APP_ID")


class WeatherService():
    def __init__(self):
        self.api_url = f'{weather_api_base_url}?appid={weather_api_app_id}&units=metric&q='

    async def get_weather_for_cities(self, cities: list[str]) -> tuple[bool, list[dict]]:
        # Creating one instance of client for optimization.
        async with httpx.AsyncClient() as client:
            tasks = [self.fetch_weather(city, client) for city in cities]
            # * is to unpack the list into individual arguments created above as asyncio.gather doesn't accept list directly.
            results = await asyncio.gather(*tasks)

            failed: list[bool] = [
                status for status, _data in results if status != True]

        return False if len(failed) > 0 else True,  [weather for _status, weather in results]

    async def get_weather_for_cities_with_retry(self, cities: list[str]) -> list[dict]:
        async with httpx.AsyncClient() as client:
            tasks = [self.fetch_weather_with_retry(
                city, client) for city in cities]

            results = await asyncio.gather(*tasks)

            return results

    async def fetch_weather(self, city_name: str, client: httpx.AsyncClient) -> tuple[bool, Weather]:
        url: str = f'{self.api_url}{city_name}'
        status: bool = False
        error: str | None = None

        try:
            if (city_name == "chennai"):
                raise Exception("testing error case")

            response = await client.get(url)
            data = response.json()

            status = True
        except Exception as e:
            status = False
            error = str(e)

        weather_info = Weather(
            city_name, float(data['main']['temp'] if status == True else 0), error)

        return status, weather_info

    async def fetch_weather_with_retry(self, city_name: str, client: httpx.AsyncClient) -> Weather | Exception:
        url: str = f'{self.api_url}{city_name}'

        for attempt in range(3):
            try:
                response = await client.get(url)
                data = response.json()

                if not data['cod'] or int(data['cod']) != 200:
                    return Weather(city_name, float(0), data['message'] or f'Not able to fetch weather data for {city_name}')

                return Weather(city_name, float(data['main']['temp']), None)
            except Exception as e:
                if attempt == 2:
                    return Weather(city_name, float(0), str(e))

                await asyncio.sleep(2 ** attempt)
