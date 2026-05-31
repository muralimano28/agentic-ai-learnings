class Weather():
    city_name: str
    temperature: float
    error: str | None

    def __init__(self, city_name: str, temperature: float, error: str | None) -> None:
        self.city_name = city_name
        self.temperature = temperature
        self.error = error

    def to_dict(self) -> dict:
        return {
            "city_name": self.city_name,
            "temperature": self.temperature
        }
