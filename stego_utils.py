from PIL import Image

def encode_message(image_path, message, output_path):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    message += chr(0)  # Null character as end marker
    message_bin = ''.join([format(ord(c), '08b') for c in message])

    data_index = 0
    for y in range(height):
        for x in range(width):
            if data_index < len(message_bin):
                r, g, b = img.getpixel((x, y))
                r = (r & ~1) | int(message_bin[data_index])  # LSB of red channel
                data_index += 1
                encoded.putpixel((x, y), (r, g, b))
            else:
                break
        if data_index >= len(message_bin):
            break

    encoded.save(output_path)

def decode_message(image_path):
    img = Image.open(image_path)
    width, height = img.size

    binary_data = ""
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            binary_data += str(r & 1)
    
    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ""
    for char in chars:
        decoded_char = chr(int(char, 2))
        if decoded_char == chr(0):
            break
        message += decoded_char

    return message
