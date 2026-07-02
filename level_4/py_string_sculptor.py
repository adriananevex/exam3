def string_sculptor(text: str) -> str:
    result = ""
    lower = True

    for char in text:
        if char == " ":
            result += char
            lower = True
        elif char.isalpha():
            if lower:
                result += char.lower()
            else:
                result += char.upper()

            lower = not lower
        
        else:
            result += char

    return result

print(string_sculptor("hello"))
print(string_sculptor("Hello World"))
print(string_sculptor("abc123def"))
print(string_sculptor("Python3.9!"))
print(string_sculptor(""))