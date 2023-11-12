import serial
import argparse
import sys
import time
from getch import getch

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
    ' ': [0x00, 0x00, 0x00],  # Space with two 00s
    # Add more mappings as needed
}

# Function to send a list of 16-bit hex characters
def send_hex_characters(punch, hex_values):
    for hex_value in hex_values:
        punch.write(bytes([hex_value]))
        time.sleep(0.1)
# Main entry point when called as an executable script.
if __name__ == '__main__':
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description="Serial Communication Example")
    parser.add_argument('port', help='Serial port for communication')

    # Parse the command-line arguments.
    args = parser.parse_args()

    # Open the serial port
    punch = serial.Serial(port=args.port, baudrate=4800)
    punch.write(b"\x12")  # Turn on the printer

    try:
        while True:
            # Use getch to get character input without waiting for Enter
            user_input = getch()

            if user_input in char_to_hex_map:
                hex_values = char_to_hex_map[user_input]
                send_hex_characters(punch, hex_values)
                print("Pressed:", user_input)  # Echo the pressed character
                punch.write(b"\x00\x00")  # Add two 00s between characters
            else:
                print("Character not found in the mapping.")

    except KeyboardInterrupt:
        pass

    # Close the serial port at the end
    punch.write(b"\x14")  # Turn off the printer
    punch.close()
