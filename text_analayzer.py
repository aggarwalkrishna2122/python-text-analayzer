# -----------------------------
# PYTHON TEXT ANALYZER
# Beginner-Friendly AI/Tech Project
# -----------------------------

from collections import Counter

# Ask user for input
text = input("Enter your text here:\n")

# Basic text analysis
words = text.split()
word_count = len(words)
char_count = len(text)
sentence_count = text.count('.') + text.count('!') + text.count('?')

# Most common words (top 5)
word_freq = Counter(words)
most_common = word_freq.most_common(5)

# Display results
print("\n--- Text Analysis Report ---")
print(f"Total Words: {word_count}")
print(f"Total Characters: {char_count}")
print(f"Total Sentences: {sentence_count}")
print("Top 5 Most Frequent Words:")
for word, freq in most_common:
    print(f"{word}: {freq}")
