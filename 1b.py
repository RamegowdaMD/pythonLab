strings = ["arr","cherry","black"]
tuple_list = [(string,len(string)) for string in strings]
sorted_tuple = sorted(tuple_list , key=lambda x:x[1])
print(sorted_tuple)
