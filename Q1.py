import sys

def caesar_cipher(text, shift):
    result = ""

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch

    return result


# Check command-line arguments
if len(sys.argv) >= 4:
    mode = sys.argv[1].lower()
    text = sys.argv[2]
    
    try:
        shift = int(sys.argv[3])
    except ValueError:
        print("Shift must be an integer.")
        sys.exit(1)

else:
    mode = input("Enter mode (encode/decode): ").lower()
    text = input("Enter text: ")

    try:
        shift = int(input("Enter shift key: "))
    except ValueError:
        print("Shift must be an integer.")
        sys.exit(1)


# Validate mode
if mode not in ("encode", "decode"):
    print("Invalid mode. Use 'encode' or 'decode'.")
    sys.exit(1)

# Reverse shift for decoding
if mode == "decode":
    shift = -shift

result = caesar_cipher(text, shift)

print("Result:", result)