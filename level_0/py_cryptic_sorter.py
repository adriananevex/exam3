def cryptic_sorter(t_list):
  def vowels_counter(s):
    counter = 0
    for i in s.lower():
      if i in "aeiou":
        counter += 1
    return counter
  final_list = sorted(t_list, key=lambda s: (len(s), s.lower(), vowels_counter(s)))
  return final_list

print(cryptic_sorter(["apple","cat","banana","dog","elephant"]))
print(cryptic_sorter(["aaa","bbb","AAA","BBB"]))
print(cryptic_sorter(["hello","world","hi","test"]))
print(cryptic_sorter([]))
print(cryptic_sorter([""]))