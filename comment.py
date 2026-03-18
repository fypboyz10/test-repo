text = "python is fun and python is easy"

words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

for word, count in freq.items():
    print(f"{word}: {count}")
