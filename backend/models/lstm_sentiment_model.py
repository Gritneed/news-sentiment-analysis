import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
import numpy as np

# Example datasets (replace with your actual preprocessed data)
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

# Encode labels explicitly
label_encoder = LabelEncoder()
label_encoder.fit(["negative", "neutral", "positive"])
y_train_enc = to_categorical(label_encoder.transform(y_train))
y_test_enc = to_categorical(label_encoder.transform(y_test))

# Tokenize text
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(X_train)

# Convert text to sequences explicitly
X_train_seq = tokenizer.texts_to_sequences(X_train)
X_test_seq = tokenizer.texts_to_sequences(X_test)

# Pad sequences clearly
max_len = 100
X_train_padded = pad_sequences(X_train_seq, maxlen=max_len)
X_test_padded = pad_sequences(X_test_seq, maxlen=max_len)

# Build LSTM model explicitly
model = Sequential()
model.add(Embedding(5000, 100, input_length=max_len))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(3, activation='softmax'))  # 3 sentiment classes

# Compile clearly defined model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Explicitly train model
model.fit(
    X_train_padded,
    y_train_enc,
    epochs=5,         # clearly define number of epochs (adjustable)
    batch_size=32,    # adjust as necessary
    validation_data=(X_test_padded, y_test_enc)
)

# Evaluate clearly
loss, accuracy = model.evaluate(X_test_padded, y_test_enc, verbose=0)
print(f"Test accuracy: {accuracy:.2f}")

# Example prediction clearly demonstrated
sample_text = ["earnings beat expectations significantly"]
sample_seq = tokenizer.texts_to_sequences(sample_text)
sample_pad = pad_sequences(sample_seq, maxlen=max_len)
pred = model.predict(sample_pad)
pred_label = label_encoder.inverse_transform(np.argmax(pred, axis=1))
print(f"Sample phrase sentiment: {pred_label[0]}")
