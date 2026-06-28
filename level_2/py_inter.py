def inter(s1: str, s2: str) -> str:
    set2 = set(s2)
    seen = set()
    result = []

    for char in s1:
        if char in set2 and char not in seen:
            result.append(char)
            seen.add(char)

    return ''.join(result)

print(inter("hello", "world"))
print(inter("banana", "band"))
print(inter("abcabc", "bc"))
print(inter("abc", "xyz"))
print(inter("", "abc"))