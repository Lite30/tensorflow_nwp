import numpy as np
import tensorflow as tf
import pickle
import os
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Embedding, LSTM, Dense

MODEL_PATH = 'models/model.h5'
TOKENIZER_PATH = 'models/tokenizer.pkl'

def load_data():
    with open('friends1.txt', 'r', encoding='utf-8') as file:
        return file.read()

def preprocess(text):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([text])
    sequences = [tokenizer.texts_to_sequences([line])[0] for line in text.split('\n') if line]
    input_sequences = [seq[:i+1] for seq in sequences for i in range(1, len(seq))]
    max_len = max(len(seq) for seq in input_sequences)
    X = pad_sequences(input_sequences, maxlen=max_len, padding='pre')[:, :-1]
    y = tf.keras.utils.to_categorical(pad_sequences(input_sequences, maxlen=max_len, padding='pre')[:, -1], 
                                   num_classes=len(tokenizer.word_index)+1)
    return tokenizer, max_len, X, y

def build_model(vocab_size, seq_len):
    model = Sequential([
        Embedding(vocab_size, 100, input_length=seq_len-1),
        LSTM(150),
        Dense(vocab_size, activation='softmax')
    ])
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def load_or_train_model():
    if os.path.exists(MODEL_PATH) and os.path.exists(TOKENIZER_PATH):
        model = load_model(MODEL_PATH)
        with open(TOKENIZER_PATH, 'rb') as f:
            tokenizer, max_len = pickle.load(f)
    else:
        os.makedirs('models', exist_ok=True)
        tokenizer, max_len, X, y = preprocess(load_data())
        model = build_model(len(tokenizer.word_index)+1, max_len)
        model.fit(X, y, epochs=50, verbose=1)
        model.save(MODEL_PATH)
        with open(TOKENIZER_PATH, 'wb') as f:
            pickle.dump((tokenizer, max_len), f)
    return model, tokenizer, max_len

def predict_next_words(model, tokenizer, max_len, seed_text, next_words):
    for _ in range(next_words):
        tokens = pad_sequences([tokenizer.texts_to_sequences([seed_text])[0]], maxlen=max_len-1, padding='pre')
        predicted = model.predict(tokens, verbose=0).argmax()
        seed_text += " " + tokenizer.index_word.get(predicted, "")
    return seed_text