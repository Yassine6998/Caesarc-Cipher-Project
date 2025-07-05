from flask import Flask, render_template, request
import string

app = Flask(__name__)

lower_alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase

def encrypt(sentence, shift):
    encrypted_sentence = ''
    for letter in sentence:
        if letter in lower_alphabet:
            old_index = lower_alphabet.index(letter)
            new_index = (old_index + shift) % 26
            encrypted_sentence += lower_alphabet[new_index]
        elif letter in upper_alphabet:
            old_index = upper_alphabet.index(letter)
            new_index = (old_index + shift) % 26
            encrypted_sentence += upper_alphabet[new_index]
        else:
            encrypted_sentence += letter
    return encrypted_sentence

@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted = ''
    if request.method == 'POST':
        sentence = request.form['sentence']
        shift = int(request.form['shift'])
        encrypted = encrypt(sentence, shift)
    return render_template('index.html', encrypted=encrypted)

if __name__ == '__main__':
    app.run(debug=True)
