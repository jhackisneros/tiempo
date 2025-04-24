from ui.home_menu import home_interface
import gradio as gr

def launch_app():
    gr.close_all()
    app = home_interface()
    app.launch(share=True)  # 🔥 Esto genera el link público
