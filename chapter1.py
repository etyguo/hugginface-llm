from transformers import pipeline

transcriber = pipeline(
    task="automatic-speech-recognition", model="openai/whisper-base.en"
)
result = transcriber(
    "/home/et/Downloads/test-youtube.mp3",
    return_timestamps=True,
)

print(result)