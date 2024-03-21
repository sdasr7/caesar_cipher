#caesar_cipher    ----> Supriyo Das

def caesar(message, shift, direction):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    output_message = ""
    for char in message:
        if char in alphabets:
            index = alphabets.index(char)
            if direction == "encode":
                position = (index + shift) % 26
            elif direction == "decode":
                position = (index - shift) % 26
            output_message += alphabets[position]
        else:
            output_message += char
    return output_message

def main():
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
        message = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))

        shift = shift % 26  # Ensure shift is within 0-25 range

        encrypted_message = caesar(message, shift, direction)
        print(f"The {direction}d text is: {encrypted_message}")

        to_continue = input("Type 'yes' if you want to go again. Otherwise, type 'no': ").lower()

        if to_continue != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
