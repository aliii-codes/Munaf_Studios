# demo.py - SUPER SIMPLE PUBLIC DEMO
import gradio as gr
import requests

def make_ad(idea):
    try:
        r = requests.post(
            "http://localhost:8000/generate",
            json={"prompt": idea, "mode": "packshot", "aspect_ratio": "1:1"},
            timeout=60
        )
        return r.json().get("result_url", "Error")
    except:
        return "Studio not running. Open http://localhost:8501 first!"

with gr.Blocks() as demo:
    gr.Markdown("# Munaf.Studios\n**Type anything → Get pro ad**")
    idea = gr.Textbox(label="Your idea", placeholder="Red sneakers, gold watch, coffee cup...")
    btn = gr.Button("Generate Ad")
    img = gr.Image()

    btn.click(make_ad, idea, img)

demo.launch(share=True)  #