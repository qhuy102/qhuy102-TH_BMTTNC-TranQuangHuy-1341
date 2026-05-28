# Rewritten source structure
class PlayFairCipher:
    def __init__(self) -> None:
        pass

    def create_playfair_matrix(self, secret_key):
        secret_key = secret_key.upper().replace("J", "I")  
        secret_key_set = set(secret_key)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining_letters = [letter for letter in alphabet if letter not in secret_key_set]
        matrix = list(secret_key)

        for letter in remaining_letters:
            matrix.append(letter)
            if len(matrix) == 25:
                break

        playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col

    def playfair_encode_content_value(self, plain_content_value, matrix):
        plain_content_value = plain_content_value.replace("J", "I").upper()
        encode_content_valueed_content_value = ""

        for i in range(0, len(plain_content_value), 2):
            pair = plain_content_value[i:i+2]

            if len(pair) == 1:  
                pair += "X"

            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:  
                encode_content_valueed_content_value += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  
                encode_content_valueed_content_value += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:  
                encode_content_valueed_content_value += matrix[row1][col2] + matrix[row2][col1]

        return encode_content_valueed_content_value

    def playfair_decode_content_value(self, cipher_content_value, matrix):
        cipher_content_value = cipher_content_value.upper()
        decode_content_valueed_content_value = ""

        for i in range(0, len(cipher_content_value), 2):
            pair = cipher_content_value[i:i+2]

            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:  
                decode_content_valueed_content_value += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  
                decode_content_valueed_content_value += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:  
                decode_content_valueed_content_value += matrix[row1][col2] + matrix[row2][col1]

        
        banro = ""
        for i in range(0, len(decode_content_valueed_content_value) - 2, 2):
            if decode_content_valueed_content_value[i] == decode_content_valueed_content_value[i+2]:
                banro += decode_content_valueed_content_value[i]
            else:
                banro += decode_content_valueed_content_value[i] + decode_content_valueed_content_value[i+1]

        if decode_content_valueed_content_value[-1] == "X":
            banro += decode_content_valueed_content_value[-2]
        else:
            banro += decode_content_valueed_content_value[-2]
            banro += decode_content_valueed_content_value[-1]


        return banro
