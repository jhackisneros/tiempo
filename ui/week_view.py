from data.parser import get_week_data
from utils.weather_logic import generate_weather_html

def render_week(semana):
    datos = get_week_data(semana)
    return generate_weather_html(datos)
