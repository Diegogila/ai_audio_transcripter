from transformers import pipeline

def transcription_audio(audio_input):
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny.en",
        chunk_length_s=30,
    )

    result = pipe(audio_input, batch_size=8)["text"]

    return result



