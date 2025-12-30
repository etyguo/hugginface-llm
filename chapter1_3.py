from transformers import pipeline

classifier = pipeline("sentiment-analysis")
result = classifier("I've been waiting for a HuggingFace course my whole life.")

print(result)

result_2 = classifier([
    "I've been waiting for a HuggingFace course my whole life.",
    "I hate this so much!"
])
print(result_2)
