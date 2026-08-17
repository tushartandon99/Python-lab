import string
from collections import Counter


def analyze_text(text):
    # Remove punctuation and convert text to lowercase
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove extra whitespace and split into words
    words = cleaned_text.lower().split()

    # Total word count
    total_words = len(words)

    # Frequency table
    frequency = Counter(words)

    # Find palindromes
    palindromes = sorted(set(word for word in words if len(word) > 1 and word == word[::-1]))

    # Display report
    print("\n===== TEXT ANALYSIS REPORT =====")
    print("Total words:", total_words)

    print("\nWord Frequency:")
    for word, count in frequency.most_common():
        print(f"{word}: {count}")

    print("\nPalindromes:")
    if palindromes:
        print(", ".join(palindromes))
    else:
        print("No palindromes found.")


# Choose input method
print("1. Read from a text file")
print("2. Enter multiline text")

choice = input("Enter your choice (1/2): ")

if choice == "1":
    filename = input("Enter file name: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        analyze_text(text)

    except FileNotFoundError:
        print("Error: File not found.")

elif choice == "2":
    print("\nEnter your text (type 'END' on a new line to finish):")

    lines = []

    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)

    text = "\n".join(lines)

    analyze_text(text)

else:
    print("Invalid choice.")