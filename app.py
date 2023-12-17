from transformers import pipeline
import gradio as gr

model=pipeline('summarization')

def predict(prompt):
    summary=model(promt)[0]['summarized_text']
    return summary

with gr.Blocks() as demo:
    textbox=gr.Textbox(placeholder='Enter text block to summarize', lines=4)
    gr.Interface(fn=predict, inputs=textbox, outputs="text")

demo.launch()
