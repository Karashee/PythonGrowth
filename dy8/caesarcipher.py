alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
 'h', 'i', 'j', 'k', 'l', 'm', 'n',
 'o', 'p', 'q', 'r', 's', 't', 'u',
 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt or 'decode' to decrypt: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

# def encrypt(original_text, shift_amount):
#     cipher_text =""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#
#     print(f"Here is the encoded result: {cipher_text}")
#
# def decrypt(original_text, shift_amount):
#     decipher_text =""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         decipher_text += alphabet[shifted_position]
#
#     print(f"Here is the decoded result: {decipher_text}")


def caesar(original_text, shift_amount, encode_or_decode):
    decipher_text = ""
    for letter in original_text:

        if letter not in alphabet:
            decipher_text += letter
        else:
            if encode_or_decode == "decode":
                shift_amount *= -1
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            decipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {decipher_text}")

should_continue = True
while_should_continue:


# encrypt(original_text=text, shift_amount=shift)
# decrypt(original_text=text, shift_amount=shift)

caesar(original_text=text, shift_amount= shift,encode_or_decode= direction)