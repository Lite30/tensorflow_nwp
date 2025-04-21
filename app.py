from flask import Flask, render_template, request
from main import load_or_train_model, predict_next_words
import webbrowser
from threading import Timer

app = Flask(__name__)
model, tokenizer, max_seq_len = load_or_train_model()

def open_browser():
    webbrowser.open_new("http://localhost:5000")

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
        seed = request.form['seed_text']
        num_words = int(request.form['num_words'])
        result = predict_next_words(model, tokenizer, max_seq_len, seed, num_words)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True)