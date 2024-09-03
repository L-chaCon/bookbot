def main():
    path = 'books/frankenstein.txt'
    book = get_book_text(path)
    print_report(book, path)


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def get_word_count(book: str) -> int:
    words = book.split()
    return len(words)


def get_character_count(book: str) -> dict:
    result = {}
    for letter in book:
        letter_lower = letter.lower()
        if letter_lower not in result:
            result[letter_lower] = 0
        result[letter_lower] += 1
    return result


def sort_on_number(dictionary: dict):
    return dictionary['number']


def sorted_characters_list(character_dict: dict) -> list[dict]:
    dict_list = []
    for key, value in character_dict.items():
        character_ocurrance = {}
        character_ocurrance['character'] = key
        character_ocurrance['number'] = value
        dict_list.append(character_ocurrance)
    dict_list.sort(reverse=True, key=sort_on_number)
    return dict_list


def print_report(book: str, path: str) -> None:
    print(f"--- Begin report of {path} ---")
    print(f"{get_word_count(book)} words found in the document\n")
    charater_list = get_character_count(book)
    sorted_list = sorted_characters_list(charater_list)
    for character in sorted_list:
        if character['character'].isalpha():
            print(f"The {character['character']} character was found {character['number']} times")
    print("--- End report ---")
    


if __name__ == "__main__":
    main()
