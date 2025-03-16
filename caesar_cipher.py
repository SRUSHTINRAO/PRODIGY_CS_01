def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    
    return result

if __name__ == "__main__":
    mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
    text = input("Enter text: ")
    shift = int(input("Enter shift value: "))
    
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode! Use 'encrypt' or 'decrypt'.")
    else:
        result = caesar_cipher(text, shift, mode)
        print(f"Result: {result}")
