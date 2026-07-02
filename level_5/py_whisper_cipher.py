def whisper_cipher(text: str, shift: int) -> str:
    result = ""

    for char in text:
        if char.isalpha():
            if char.islower():
                base = ord("a")
            else:
                base = ord("A")

            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char

        else:
            result += char

    return result

print(whisper_cipher("hello", 3))
print(whisper_cipher("Hello World!", 1))
print(whisper_cipher("xyz", 3))
print(whisper_cipher("ABC123def", 5))
print(whisper_cipher("", 10))
print(whisper_cipher("abc", -3))