from typing import List

import numpy as np
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.layers import Dense, Dropout, Embedding, LSTM
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical


def prepare_data(X_train: List[str], y_train: List[str], X_test: List[str], y_test: List[str], max_len: int = 100):
    tokenizer = Tokenizer(num_words=5000)
    tokenizer.fit_on_texts(X_train)

    X_train_seq = tokenizer.texts_to_sequences(X_train)
    X_test_seq = tokenizer.texts_to_sequences(X_test)

    X_train_pad = pad_sequences(X_train_seq, maxlen=max_len)
    X_test_pad = pad_sequences(X_test_seq, maxlen=max_len)

    label_encoder = LabelEncoder()
    label_encoder.fit(["negative", "neutral", "positive"])
    y_train_enc = to_categorical(label_encoder.transform(y_train))
    y_test_enc = to_categorical(label_encoder.transform(y_test))

    return X_train_pad, y_train_enc, X_test_pad, y_test_enc, tokenizer, label_encoder


def build_model(input_length: int) -> Sequential:
    model = Sequential()
    model.add(Embedding(5000, 100, input_length=input_length))
    model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(3, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


if __name__ == "__main__":
    # Sample data
    X_train = [
        "company reported strong earnings growth",
        "shares surged positive earnings report",
        "revenue declined sharply poor results",
    ]
    y_train = ["positive", "positive", "negative"]

    X_test = [
        "company announces layoffs amid declining sales",
        "profit margins improved significantly",
    ]
    y_test = ["negative", "positive"]

    max_len = 100
    X_train_pad, y_train_enc, X_test_pad, y_test_enc, tokenizer, label_encoder = prepare_data(
        X_train, y_train, X_test, y_test, max_len
    )

    model = build_model(input_length=max_len)

    model.fit(
        X_train_pad,
        y_train_enc,
        epochs=5,
        batch_size=32,
        validation_data=(X_test_pad, y_test_enc)
    )

    loss, accuracy = model.evaluate(X_test_pad, y_test_enc, verbose=0)
    print(f"Test accuracy: {accuracy:.2f}")

    # Prediction
    sample_text = ["earnings beat expectations significantly"]
    sample_seq = tokenizer.texts_to_sequences(sample_text)
    sample_pad = pad_sequences(sample_seq, maxlen=max_len)
    pred = model.predict(sample_pad)
    pred_label = label_encoder.inverse_transform(np.argmax(pred, axis=1))
    print(f"Sample phrase sentiment: {pred_label[0]}")
