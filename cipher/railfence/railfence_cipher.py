# Rewritten source structure
class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encode_content_value(self, plain_content_value, num_rails):
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  
        
        for char in plain_content_value:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        
        cipher_content_value = ''.join(''.join(rail) for rail in rails)
        return cipher_content_value

    def rail_fence_decode_content_value(self, cipher_content_value, num_rails):
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_content_value)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_content_value[start:start + length]))
            start += length

        plain_text = ""
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_content_value)):
            plain_text += rails[rail_index][0]
            rails[rail_index] = rails[rail_index][1:]
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return plain_text
