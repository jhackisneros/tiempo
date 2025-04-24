import gradio as gr
from ui.week_view import render_week
from ui.styles import custom_theme

def home_interface():
    with gr.Blocks(title="☀️ App del Tiempo", theme=custom_theme) as demo:
        gr.Markdown("## ☁️☀️ Bienvenido a la App del Tiempo", elem_id="title")

        with gr.Row():
            semana_selector = gr.Dropdown(
                label="Seleccioná una semana",
                choices=["Semana 1", "Semana 2", "Semana 3"],
                value="Semana 1"
            )

        clima_output = gr.HTML(label="Pronóstico por hora")

        semana_selector.change(fn=render_week, inputs=semana_selector, outputs=clima_output)

    return demo
