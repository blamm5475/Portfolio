try:
    plain_text = input("Enter a plain text sentence: ")
    shift = 5

    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                char = char.lower()
            ascii_offset = ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted_char = char
        encrypted_text += encrypted_char

    print("The encrypted sentence is:", encrypted_text)
except Exception as e:
    print("An error occurred:", e)