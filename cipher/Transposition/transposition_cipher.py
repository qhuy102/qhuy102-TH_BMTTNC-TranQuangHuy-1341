
class TranspositionCipher:

    # =========================
    # Encrypt
    # =========================
    def encrypt(self, plain_text, key):

        cipher_text = [''] * key

        for col in range(key):
            pointer = col

            while pointer < len(plain_text):
                cipher_text[col] += plain_text[pointer]
                pointer += key

        return ''.join(cipher_text)

    # =========================
    # Decrypt
    # =========================
    def decrypt(self, cipher_text, key):

        num_cols = int(len(cipher_text) / key)

        if len(cipher_text) % key != 0:
            num_cols += 1

        num_rows = key

        num_shaded_boxes = (num_cols * num_rows) - len(cipher_text)

        plain_text = [''] * num_cols

        col = 0
        row = 0

        for symbol in cipher_text:
            plain_text[col] += symbol
            col += 1

            if (
                col == num_cols or
                (col == num_cols - 1 and row >= num_rows - num_shaded_boxes)
            ):
                col = 0
                row += 1

        return ''.join(plain_text)

