
import re

def analyze_text(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    print("\nWORD FREQUENCY ANALYSIS")
    print("-----------------------")

    for word, count in frequency.items():
        print(word, ":", count)

    print("\nMOST FREQUENT WORD")
    if frequency:
        max_word = max(frequency, key=frequency.get)
        print(max_word, ":", frequency[max_word])

    print("\nREPEATED WORDS")
    for word, count in frequency.items():
        if count > 1:
            print(word, ":", count)

    print("\nPATTERN ANALYSIS")
    pattern = input("Enter pattern to search: ").lower()

    matches = re.findall(pattern, text.lower())

    print("Pattern found:", len(matches), "times")

    if matches:
        print("Matches:", matches)
    else:
        print("No pattern found")


print("AUTOMATED WORD FREQUENCY AND PATTERN ANALYZER")

text = input("Enter your text: ")

analyze_text(text)
