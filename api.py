
from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.Transposition import TranspositionCipher

app = Flask(__name__, template_folder='templates')


# =========================
# Caesar Cipher
# =========================
caesar_cipher = CaesarCipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.get_json()

    plain_text = data['plain_text']
    key = int(data['key'])

    cipher_text = caesar_cipher.encode_content_value_content_value(
        plain_text,
        key
    )

    return jsonify({
        'cipher_text': cipher_text
    })


@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.get_json()

    cipher_text = data['cipher_text']
    key = int(data['key'])

    plain_text = caesar_cipher.decode_content_value_content_value(
        cipher_text,
        key
    )

    return jsonify({
        'plain_text': plain_text
    })


# =========================
# Vigenere Cipher
# =========================
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()

    plain_text = data['plain_text']
    key = data['key']

    cipher_text = vigenere_cipher.encode_content_value_content_value(
        plain_text,
        key
    )

    return jsonify({
        'cipher_text': cipher_text
    })


@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()

    cipher_text = data['cipher_text']
    key = data['key']

    plain_text = vigenere_cipher.decode_content_value_content_value(
        cipher_text,
        key
    )

    return jsonify({
        'plain_text': plain_text
    })


# =========================
# Rail Fence Cipher
# =========================
railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.get_json()

    plain_text = data['plain_text']
    key = int(data['key'])

    cipher_text = railfence_cipher.rail_fence_encode_content_value(
        plain_text,
        key
    )

    return jsonify({
        'cipher_text': cipher_text
    })


@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json()

    cipher_text = data['cipher_text']
    key = int(data['key'])

    plain_text = railfence_cipher.rail_fence_decode_content_value(
        cipher_text,
        key
    )

    return jsonify({
        'plain_text': plain_text
    })


# =========================
# PlayFair Cipher
# =========================
playfair_cipher = PlayFairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.get_json()

    key = data['key']

    playfair_matrix = playfair_cipher.create_playfair_matrix(key)

    return jsonify({
        "playfair_matrix": playfair_matrix
    })


@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()

    plain_text = data['plain_text']
    key = data['key']

    playfair_matrix = playfair_cipher.create_playfair_matrix(key)

    cipher_text = playfair_cipher.playfair_encode_content_value(
        plain_text,
        playfair_matrix
    )

    return jsonify({
        'cipher_text': cipher_text
    })


@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()

    cipher_text = data['cipher_text']
    key = data['key']

    playfair_matrix = playfair_cipher.create_playfair_matrix(key)

    plain_text = playfair_cipher.playfair_decode_content_value(
        cipher_text,
        playfair_matrix
    )

    return jsonify({
        'plain_text': plain_text
    })


# =========================
# Transposition Cipher
# =========================
transposition_cipher = TranspositionCipher()

@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()

    plain_text = data['plain_text']
    key = int(data['key'])

    cipher_text = transposition_cipher.encrypt(
        plain_text,
        key
    )

    return jsonify({
        'cipher_text': cipher_text
    })


@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()

    cipher_text = data['cipher_text']
    key = int(data['key'])

    plain_text = transposition_cipher.decrypt(
        cipher_text,
        key
    )

    return jsonify({
        'plain_text': plain_text
    })


# =========================
# Run Server
# =========================
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

