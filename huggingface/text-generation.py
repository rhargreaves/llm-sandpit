from transformers import pipeline

classifier = pipeline("text-generation", model="distilgpt2")
while True:
    text = input("Enter initial text: ")
    generated_text = classifier(text, num_return_sequences=2, max_length=30)
    for t in generated_text:
        print(t.get("generated_text"))
