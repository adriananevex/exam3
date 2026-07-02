def anagram(s1: str, s2: str) -> bool:
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")

    return sorted(s1) == sorted(s2)

print(anagram("listen", "silent"))
print(anagram("Triangle", "Integral"))
print(anagram("Dormitory", "Dirty Room"))
print(anagram("hello", "world"))
print(anagram("", ""))
print(anagram("abc", "abcc"))