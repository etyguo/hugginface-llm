from transformers import pipeline

transcriber = pipeline(
    task="automatic-speech-recognition", model="openai/whisper-base.en"
)
result = transcriber(
    "/home/et/Downloads/mlk.flac",
    return_timestamps=False,
)

print(result)