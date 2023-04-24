from api_service import get_weather
from coordinates import get_coordinates


def weather() -> str:
    """Возвращает сообщение о температуре и описании погоды. """
    wthr = get_weather(get_coordinates())
    return f'{wthr.location}, {wthr.description}\n' \
           f'Temperature is {wthr.temperature}°C, feels like {wthr.temperature_feeling}°C'


def wind() -> str:
    """Возвращает сообщение о направлении и скорости ветра."""
    wthr = get_weather(get_coordinates())
    return f'{wthr.wind_direction} wind {wthr.wind_speed} m/s'


def sun_time() -> str:
    """ Возвращает сообщение о времени восхода и захода солнца."""
    wthr = get_weather(get_coordinates())
    return f'Sunrise: {wthr.sunrise.strftime("%H:%M")}\n' \
           f'Sunset: {wthr.sunset.strftime("%H:%M")}\n'
