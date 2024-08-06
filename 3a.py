def dictionary_operations():
    dictionary = {}

    def add_entry(word, meaning):
        dictionary[word] = meaning

    def search_word(word):
        return dictionary.get(word, "Word not found")

    def find_words_with_meaning(meaning):
        return [word for word, mean in dictionary.items() if mean == meaning]

    def remove_entry(word):
        if word in dictionary:
            del dictionary[word]
        else:
            print("Word not found")

    def display_sorted_words():
        for word in sorted(dictionary.keys()):
            print(f"{word}: {dictionary[word]}")

    while True:
        print("\nDictionary Operations:")
        print("1 - Add entry")
        print("2 - Search word")
        print("3 - Find words with same meaning")
        print("4 - Remove entry")
        print("5 - Display all words sorted")
        print("6 - Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            word = input("Enter word: ")
            meaning = input("Enter meaning: ")
            add_entry(word, meaning)
        elif choice == '2':
            word = input("Enter word to search: ")
            print(search_word(word))
        elif choice == '3':
            meaning = input("Enter meaning to search: ")
            print(find_words_with_meaning(meaning))
        elif choice == '4':
            word = input("Enter word to remove: ")
            remove_entry(word)
        elif choice == '5':
            display_sorted_words()
        elif choice == '6':
            break
        else:
            print("Invalid choice")

dictionary_operations()