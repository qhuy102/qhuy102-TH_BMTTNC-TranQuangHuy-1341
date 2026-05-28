# Rewritten source structure
from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET
        self.alphabet_len = len(self.alphabet)

    def encode_content_value_content_value(self, content_value: str, secret_key: int) -> str:
        encode_content_valueed_content_value = []
        try:
            secret_key = int(secret_key)  
            for letter in content_value:
                if letter.upper() in self.alphabet:  
                    letter_index = self.alphabet.index(letter.upper())
                    output_index = (letter_index + secret_key) % self.alphabet_len
                    output_letter = self.alphabet[output_index]
                    encode_content_valueed_content_value.append(output_letter if letter.isupper() else output_letter.lower())
                else:
                    encode_content_valueed_content_value.append(letter)  
        except ValueError as e:
            return f"Lỗi: {e}"
        return "".join(encode_content_valueed_content_value)

    def decode_content_value_content_value(self, content_value: str, secret_key: int) -> str:
        decode_content_valueed_content_value = []
        try:
            secret_key = int(secret_key)  
            for letter in content_value:
                if letter.upper() in self.alphabet:
                    letter_index = self.alphabet.index(letter.upper())
                    output_index = (letter_index - secret_key) % self.alphabet_len
                    output_letter = self.alphabet[output_index]
                    decode_content_valueed_content_value.append(output_letter if letter.isupper() else output_letter.lower())
                else:
                    decode_content_valueed_content_value.append(letter)
        except ValueError as e:
            return f"Lỗi: {e}"
        return "".join(decode_content_valueed_content_value)
