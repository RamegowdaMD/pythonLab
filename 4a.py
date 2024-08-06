def dictionary_functions():
    passwd = {'Rahul': 'genius', 'Kumar': 'smart', 'Ankita': 'intelligent'}

    def print_items(d):
        for key, value in d.items():
            print(f"{key}: {value}")

    def print_keys(d):
        for key in d.keys():
            print(key)

    def print_values(d):
        for value in d.values():
            print(value)

    print("All items in the dictionary:")
    print_items(passwd)
    print("\nAll keys in the dictionary:")
    print_keys(passwd)
    print("\nAll values in the dictionary:")
    print_values(passwd)

dictionary_functions()