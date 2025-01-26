def count_words(text: str) -> int:
    total_word_count: list[str] = []

    for word in text.split():
        total_word_count.append(word)

    return len(total_word_count)


def count_characters(text: str) -> dict[str, int]:
    total_char_count: dict[str, int] = {}

    for char in text.lower():
        
        
        

    return None


def main():
    with open(file="./books/frankenstein.txt") as f:
        file_contents: str = f.read()
        word_count: int = count_words(text=file_contents)
    print(word_count)


if __name__ == "__main__":
    main()
