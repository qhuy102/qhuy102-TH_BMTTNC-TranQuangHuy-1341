# Rewritten source structure
from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayFairCipher
from cipher.railfence import RailFenceCipher
from cipher.Transposition import TranspositionCipher

app = Flask(__name__, template_folder='templates')


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/caesar/encode_content_value", methods=['POST'])
def caesar_encode_content_value():
    content_value = request.form['inputPlainText']
    secret_key = int(request.form['inputKeyPlain'])
    caesar = CaesarCipher()
    encode_content_valueed_content_value = caesar.encode_content_value_content_value(content_value, secret_key)
    return f"content_value: {content_value}<br>/secret_key: {secret_key}<br>/encode_content_valueed content_value: {encode_content_valueed_content_value}"

@app.route("/caesar/decode_content_value", methods=['POST'])
def caesar_decode_content_value():
    content_value = request.form['inputCipherText']
    secret_key = int(request.form['inputKeyCipher'])
    caesar = CaesarCipher()
    decode_content_valueed_content_value = caesar.decode_content_value_content_value(content_value, secret_key)
    return f"content_value: {content_value}<br>/secret_key: {secret_key}<br>/decode_content_valueed content_value: {decode_content_valueed_content_value}"



@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encode_content_value", methods=['POST'])
def vigenere_encode_content_value():
    content_value = request.form['inputPlainText']
    secret_key = request.form['inputKeyPlain']
    vigenere = VigenereCipher()
    encode_content_valueed_content_value = vigenere.encode_content_value_content_value(content_value, secret_key)
    return f"content_value: {content_value}<br>/secret_key: {secret_key}<br>/encode_content_valueed content_value: {encode_content_valueed_content_value}"

@app.route("/vigenere/decode_content_value", methods=['POST'])
def vigenere_decode_content_value():
    content_value = request.form['inputCipherText']
    secret_key = request.form['inputKeyCipher']
    vigenere = VigenereCipher()
    decode_content_valueed_content_value = vigenere.decode_content_value_content_value(content_value, secret_key)
    return f"content_value: {content_value}<br>/secret_key: {secret_key}<br>/decode_content_valueed content_value: {decode_content_valueed_content_value}"



@app.route("/playfair")
def playfair():
    return render_template('playfair.html')
@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
        data = request.json  
        secret_key = data.get('secret_key', '') 
        playfair_cipher = PlayFairCipher()
        playfair_matrix = playfair_cipher.create_playfair_matrix(secret_key) 
        return jsonify({"playfair_matrix": playfair_matrix})

@app.route("/playfair/encode_content_value", methods=['POST'])
def playfair_encode_content_value():
    content_value = request.form['inputPlainText']
    secret_key = request.form['inputKeyPlain']
    playfair_cipher = PlayFairCipher()
    playfair_matrix = playfair_cipher.create_playfair_matrix(secret_key)
    encode_content_valueed_content_value = playfair_cipher.playfair_encode_content_value(content_value, playfair_matrix)
    return f"content_value: {content_value}<br>/secret_key: {secret_key}<br>/encode_content_valueed content_value: {encode_content_valueed_content_value}"

@app.route("/playfair/decode_content_value", methods=['POST'])
def playfair_decode_content_value():
    content_value = request.form['inputCipherText']
    secret_key = request.form['inputKeyCipher']
    playfair_cipher = PlayFairCipher()
    playfair_matrix = playfair_cipher.create_playfair_matrix(secret_key)
    decode_content_valueed_content_value = playfair_cipher.playfair_decode_content_value(content_value, playfair_matrix)
    return f"content_value: {content_value}<br>/secret_key: {secret_key}<br>/decode_content_valueed content_value: {decode_content_valueed_content_value}"



@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encode_content_value", methods=['POST'])
def railfence_encode_content_value():
    content_value = request.form['inputPlainText']
    secret_key = int(request.form['inputKeyPlain'])
    railfence = RailFenceCipher()
    encode_content_valueed_content_value = railfence.rail_fence_encode_content_value(content_value, secret_key)
    return f"content_value: {content_value}<br>/secret_key: {secret_key}<br>/encode_content_valueed content_value: {encode_content_valueed_content_value}"

@app.route("/railfence/decode_content_value", methods=['POST'])
def railfence_decode_content_value():
    content_value = request.form['inputCipherText']
    secret_key = int(request.form['inputKeyCipher'])
    railfence = RailFenceCipher()
    decode_content_valueed_content_value = railfence.rail_fence_decode_content_value(content_value, secret_key)
    return f"content_value: {content_value}<br>/secret_key: {secret_key}<br>/decode_content_valueed content_value: {decode_content_valueed_content_value}"



@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route("/transposition/encode_content_value", methods=['POST'])
def transposition_encode_content_value():
    content_value = request.form['inputPlainText']
    secret_key = int(request.form['inputKeyPlain'])  
    transposition = TranspositionCipher()
    encode_content_valueed_content_value = transposition.encode_content_value(content_value, secret_key)
    return f"content_value: {content_value}<br>/secret_key: {secret_key}<br>/encode_content_valueed content_value: {encode_content_valueed_content_value}"

@app.route("/transposition/decode_content_value", methods=['POST'])
def transposition_decode_content_value():
    content_value = request.form['inputCipherText']
    secret_key = int(request.form['inputKeyCipher'])  
    transposition = TranspositionCipher()
    decode_content_valueed_content_value = transposition.decode_content_value(content_value, secret_key)
    return f"content_value: {content_value}<br>/secret_key: {secret_key}<br>/decode_content_valueed content_value: {decode_content_valueed_content_value}"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
