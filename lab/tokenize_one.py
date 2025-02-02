"""
Читает текст из файла и создает токены
"""
import sys

from settings import DICTIONARY

sys.path.append('../')

from analytics.functions import analyze_one_item

filename = 'tokenize_one.txt'

print('Read data from file...')
with open(filename, 'r', encoding='utf-8') as f:
    line = f.read()

one = line.strip()
print(f'{one} has been loaded')
one_tokens = analyze_one_item(one, DICTIONARY)
print('TOKENS:', one_tokens)