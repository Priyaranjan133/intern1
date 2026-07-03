def longest_word(words):
    longest = max(words, key=len)
    return longest, len(longest)


words = ["Python", "Programming", "AI", "Computer"]
word, length = longest_word(words)

print("Longest Word:", word)
print("Length:", length)