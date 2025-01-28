from pprint import pprint


def count_words(text: str) -> int:
    total_word_count: list[str] = []

    for word in text.split():
        total_word_count.append(word)

    return len(total_word_count)


def count_characters(text: str) -> dict[str, int]:
    count: dict[str, int] = {}

    for char in text.lower():
        if char.isalpha():
            if char not in count:
                count[char] = 1
            else:
                count[char] = count[char] + 1

    return count


# Main execution

with open(file="./books/frankenstein.txt") as f:
    file_contents: str = f.read()
    word_count: int = count_words(text=file_contents)
    character_count: dict[str, int] = count_characters(text=file_contents)

print("--- Begin report of books/frankenstein.txt ---")

pprint(object=f"{word_count} words found in the document")
print("\n")

for letter, count in character_count.items():
    pprint(object=f"The '{letter}' character was found {count} times")

print("--- End report ---")
