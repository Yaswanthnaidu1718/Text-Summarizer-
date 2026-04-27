from flask import Flask, request, render_template
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

app = Flask(__name__)

device = "cuda" if torch.cuda.is_available() else "cpu"

# 🔥 BEST MODEL FOR SUMMARIZATION
model_name = "facebook/bart-large-cnn"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']   

    text = "Summarize the following text:\n" + text   

    inputs = tokenizer(text, return_tensors="pt", truncation=True).to(device)

    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=20,
        min_length=5,
        num_beams=8,
        length_penalty=3.5,
        no_repeat_ngram_size=3,
        early_stopping=True
    )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return render_template("index.html", summary=summary, text=text)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)