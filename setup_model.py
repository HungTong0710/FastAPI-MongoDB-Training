from transformers import pipeline

print("Loading DistilGPT2 model, Please wait...")

try:
    story_generator = pipeline('text-generation', model='distilgpt2', device=-1)
    print("Model loaded and ready!")

except Exception as e:
    print(f"Failed to load model: {e}")
    story_generator = None