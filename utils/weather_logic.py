def generate_weather_html(datos):
    html = "<table style='width:100%; color:white;'>"
    html += "<tr><th>Hora</th><th>Clima</th></tr>"
    for hora, clima in datos:
        icono = "🌧️" if "lluvia" in clima.lower() else "☁️" if "nublado" in clima.lower() else "☀️"
        html += f"<tr><td>{hora}</td><td>{icono} {clima}</td></tr>"
    html += "</table>"
    return html
