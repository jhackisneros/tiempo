import gradio as gr

# En lugar de usar `.set()`, usamos directamente Blocks con css
custom_css = """
body {
    background-color: #87CEEB !important;
    color: white !important;
}
.gr-button {
    color: #87CEEB !important;
}
"""

def apply_theme(blocks: gr.Blocks):
    blocks.css = custom_css
