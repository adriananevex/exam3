def hidenp(small: str, big: str) -> bool:
    if not small:
        return True

    small_count = 0

    for char in big:
        if small_count < len(small) and char == small[small_count]:
            small_count += 1
    return small_count == len(small)


print(hidenp("abc", "a1b2c3"))
print(hidenp("ace", "abcde"))
print(hidenp("aec", "abcde"))
print(hidenp("", "abc"))
print(hidenp("abc", "ab"))
print(hidenp("aaaa", "aaa"))
print(hidenp("sing","subsequence testing"))