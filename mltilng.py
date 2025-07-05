from gtts import gTTS
import gradio as gr
import tempfile

lang = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
}

def language(audio):
    return lang.get(audio, "en")

def gtts_speak(text, audio_language):
    language_code = language(audio_language)
    tts = gTTS(text, lang=language_code)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        return fp.name

gr.Interface(
    fn=gtts_speak,
    inputs=[
        gr.Textbox(label="Write your Text"),
        gr.Dropdown(["English", "Hindi", "French", "German"], label="Select Language")
    ],
    outputs=gr.Audio(type="filepath")
).launch()
