import re

def count_occurrences(text):
    vowels = len(re.findall(r'[aeiouAEIOU]', text))
    consonants = len(re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', text))
    digits = len(re.findall(r'\d', text))
    return vowels, consonants, digits

text = "Example text: 123 Hello World!"
vowels, consonants, digits = count_occurrences(text)
print(f"Vowels: {vowels}, Consonants: {consonants}, Digits: {digits}")