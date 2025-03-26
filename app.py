import gradio as gr
from simple_speech2text import transcription_audio

audio_input = gr.Audio(sources="upload",type="filepath")
output_text = gr.Textbox()

iface = gr.Interface(fn=transcription_audio,
                     inputs=audio_input,
                     outputs=output_text,
                     title="Audio Transcription App",
                     description="Upload the audio file")

iface.launch(server_name="0.0.0.0", server_port=7860)