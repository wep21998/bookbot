import sys
def main():
    book = open_book()
    print(f"There are {word_count(book)} words")
    print(f"character count is as follows : \n {character_count(book)}")

def word_count(book):
    words = book.split()
    #print(words)
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def character_count(book):
    contents = book.lower()
    characters = {}

    for character in contents:
        if characters.get(character) == None:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters


def open_book():
    title = f"{sys.argv[1]}.txt"
    #print(title)
    with open(f"books/{title}") as book:
        return book.read()
        

main()