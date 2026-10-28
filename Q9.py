def clean_text(text):
    """Cleans formatting variances (spaces, casing)."""
    return "".join(char.lower() for char in text if char.isalnum())

def is_anagram_sort(text1, text2):
    """Checks anagrams using list sorting."""
    return sorted(clean_text(text1)) == sorted(clean_text(text2))

def is_anagram_dict(text1, text2):
    """Checks anagrams using dictionary counting techniques."""
    def count_chars(text):
        counts = {}
        for char in clean_text(text):
            counts[char] = counts.get(char, 0) + 1
        return counts
    return count_chars(text1) == count_chars(text2)

def group_anagrams(phrases):
    """Groups anagrams using immutable tuple keys for fast lookup."""
    anagram_map = {}
    for phrase in phrases:
        # Using a sorted tuple of characters as an immutable dictionary key
        key = tuple(sorted(clean_text(phrase)))
        if key not in anagram_map:
            anagram_map[key] = []
        anagram_map[key].append(phrase)
    return list(anagram_map.values())

# 1. Cleaning and Matching
p1, p2 = "Clint Eastwood", "Old West Action"
print(f"Phrase 1: '{p1}' | Phrase 2: '{p2}'")
print(f"Sort Match: {is_anagram_sort(p1, p2)}")
print(f"Dict Match: {is_anagram_dict(p1, p2)}\n")

# 2. Fast Lookup Grouping via Tuple Keys
phrases_list = ["Listen", "Silent", "Enlist", "Rat", "Art", "Tar", "Python"]
print("Original List:", phrases_list)
print("Grouped Anagrams:", group_anagrams(phrases_list))