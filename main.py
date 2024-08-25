import sys
def main():
    title = f"{sys.argv[1]}.txt"
    book = open_book(title)
    characters = character_count(book)
    print(f"There are {word_count(book)} words")
    print(f"Begining report on {title}:")
    for i in range(len(characters)):
        print(f"The was found {characters[i]} times")

def word_count(book):
    words = book.split()
    #print(words)
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def character_count(book):
    contents = book.lower()
    characters = []

    for character in contents:
        #print(character)
        #print(characters)
        #print({"char" : character} in characters)
        if character.isalpha() == True:
            if len(characters) == 0: #Determines if character is a letter
                characters.append({"char" : character, "count" : 1})
            elif  next((item for item in characters if item["char"] == character), None) == None: #Searches to see if letter is in list
                characters.append({"char" : character, "count" : 1})
            else:
                for i in range(len(characters)):
                    if characters[i]["char"] == character:
                        characters[i]["count"] +=1
    characters.sort(reverse=True, key=sort_on) #Sort by number of letters found
    print(characters)
    return characters

def sort_on(dict):
    return dict["count"]

def open_book(title):
    with open(f"books/{title}") as book:
        return book.read()
        

main()