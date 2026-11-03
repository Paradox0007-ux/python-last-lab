
def clean_word(word):
    return ''.join(
        char.lower() for char in word if char.isalnum()
    )


def sort_word(word):
    return ''.join(sorted(clean_word(word)))


def check_anagram(word1, word2):
    return sort_word(word1) == sort_word(word2)


def create_anagram_key(word):
    return tuple(sorted(clean_word(word)))


def group_anagrams(words):
    anagram_dict = {}

    for word in words:
        key = create_anagram_key(word)

        if key not in anagram_dict:
            anagram_dict[key] = []

        anagram_dict[key].append(word)

    return anagram_dict


while True:
    print("\n===== ANAGRAM DETECTOR =====")
    print("1. Check Two Words")
    print("2. Group Anagrams")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        word1 = input("Enter first word: ")
        word2 = input("Enter second word: ")

        if check_anagram(word1, word2):
            print("Both words are Anagrams!")
        else:
            print("Words are not Anagrams!")

    elif choice == "2":
        words = input("Enter words separated by spaces: ").split()

        result = group_anagrams(words)

        print("\nAnagram Groups:")

        for key, group in result.items():
            if len(group) > 1:
                print(group)

    elif choice == "3":
        print("Exiting Anagram Detector...")
        break

    else:
        print("Invalid choice! Try again.")
