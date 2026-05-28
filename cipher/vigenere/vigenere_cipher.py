# Rewritten source structure
class VigenereCipher:
    def __init__(self):
        pass

    def encode_content_value_content_value(self, plain_content_value, secret_key):
        encode_content_valueed_content_value = ""
        secret_key_index = 0
        for char in plain_content_value:
            if char.isalpha():
                secret_key_shift = ord(secret_key[secret_key_index % len(secret_key)].upper()) - ord('A')
                if char.isupper():
                    encode_content_valueed_content_value += chr((ord(char) - ord('A') + secret_key_shift) % 26 + ord('A'))
                else:
                    encode_content_valueed_content_value += chr((ord(char) - ord('a') + secret_key_shift) % 26 + ord('a'))
                secret_key_index += 1
            else:
                encode_content_valueed_content_value += char
        return encode_content_valueed_content_value

    def decode_content_value_content_value(self, encode_content_valueed_content_value, secret_key):
        decode_content_valueed_content_value = ""
        secret_key_index = 0
        for char in encode_content_valueed_content_value:
            if char.isalpha():
                secret_key_shift = ord(secret_key[secret_key_index % len(secret_key)].upper()) - ord('A')
                if char.isupper():
                    decode_content_valueed_content_value += chr((ord(char) - ord('A') - secret_key_shift) % 26 + ord('A'))
                else:
                    decode_content_valueed_content_value += chr((ord(char) - ord('a') - secret_key_shift) % 26 + ord('a'))
                secret_key_index += 1
            else:
                decode_content_valueed_content_value += char
        return decode_content_valueed_content_value
