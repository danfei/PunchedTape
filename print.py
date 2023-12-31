import serial
import argparse
import time

# Define a character to 16-bit hex mapping dictionary
char_to_hex_map = {
    'A': [0x3F, 0x48, 0x48, 0x48, 0x3F],
    'B': [0x7F, 0x49, 0x49, 0x49, 0x36],
    'C': [0x3E, 0x41, 0x41, 0x41, 0x22],
    'D': [0x7F, 0x41, 0x41, 0x41, 0x3E],
    'E': [0x7F, 0x49, 0x49, 0x49, 0x41],
    'F': [0x7F, 0x48, 0x48, 0x48, 0x40],
    'G': [0x3E, 0x41, 0x49, 0x49, 0x2E],
    'H': [0x7F, 0x08, 0x08, 0x08, 0x7F],
    'I': [0x41, 0x7F, 0x41],
    'J': [0x06, 0x01, 0x01, 0x01, 0x7E],
    'K': [0x7F, 0x08, 0x1C, 0x22, 0x41],
    'L': [0x7F, 0x01, 0x01, 0x01, 0x01],
    'M': [0x7F, 0x20, 0x18, 0x20, 0x7F],
    'N': [0x7F, 0x20, 0x10, 0x08, 0x7F],
    'O': [0x3E, 0x41, 0x41, 0x41, 0x3E],
    'P': [0x7F, 0x48, 0x48, 0x48, 0x30],
    'Q': [0x3E, 0x41, 0x45, 0x42, 0x3D],
    'R': [0x7F, 0x48, 0x4C, 0x4A, 0x31],
    'S': [0x32, 0x49, 0x49, 0x49, 0x26],
    'T': [0x40, 0x40, 0x7F, 0x40, 0x40],
    'U': [0x7E, 0x01, 0x01, 0x01, 0x7E],
    'V': [0x7C, 0x02, 0x01, 0x02, 0x7C],
    'W': [0x7F, 0x02, 0x0C, 0x02, 0x7F],
    'X': [0x63, 0x1C, 0x08, 0x1C, 0x63],
    'Y': [0x70, 0x08, 0x07, 0x08, 0x70],
    'Z': [0x43, 0x45, 0x49, 0x51, 0x61],
    '0': [0x3E, 0x45, 0x49, 0x51, 0x3E],
    '1': [0x21, 0x7F, 0x01],
    '2': [0x21, 0x43, 0x45, 0x49, 0x31],
    '3': [0x41, 0x49, 0x49, 0x49, 0x36],
    '4': [0x78, 0x08, 0x08, 0x08, 0x7F],
    '5': [0x79, 0x49, 0x49, 0x49, 0x46],
    '6': [0x3E, 0x49, 0x49, 0x49, 0x06],
    '7': [0x40, 0x40, 0x47, 0x48, 0x70],
    '8': [0x36, 0x49, 0x49, 0x49, 0x36],
    '9': [0x32, 0x49, 0x49, 0x49, 0x3E],
    '!': [0x7B],
    '.': [0x01],
    ',': [0x01, 0x06],
    '<': [0x08, 0x1C, 0x2A, 0x49, 0x08, 0x08],
    ' ': [0x00, 0x00, 0x00], # Add more mappings as needed
}

def send_hex_characters(punch, hex_values):
    for hex_value in hex_values:
        punch.write(bytes([hex_value]))
        time.sleep(0.1)  # 100 ms delay

def print_text(punch, text, mode):
    if mode == 'bin':
        for char in text:
            punch.write(bytes([ord(char)]))
            time.sleep(0.1)
    elif mode == 'shape':
        for char in text:
            if char in char_to_hex_map:
                hex_values = char_to_hex_map[char]
                send_hex_characters(punch, hex_values)
                punch.write(b"\x00\x00")  # Add two 00s between characters
            else:
                print(f"Character not found in the mapping: {char}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Serial Communication Example")
    parser.add_argument('port', help='Serial port for communication')
    parser.add_argument('file', help='File containing text to print')
    parser.add_argument('mode', choices=['bin', 'shape'], help='Print mode (bin or shape)')

    args = parser.parse_args()

    punch = serial.Serial(port=args.port, baudrate=4800)
    punch.write(b"\x12")  # Turn on the printer
    punch.write(b"\x00\x00\x00")
    with open(args.file, 'r') as file:
        text = file.read()

    print_text(punch, text, args.mode)
    punch.write(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    punch.write(b"\x14")  # Turn off the printer
    punch.close()
