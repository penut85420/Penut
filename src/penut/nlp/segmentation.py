import re
import string

def character_base(sent):
    return [ch for ch in sent]

def whitespace_seg(sent, whitespace=string.whitespace):
    return re.split(f'[{whitespace}]', sent)

if __name__ == "__main__":
    sent = 'Hello, today is a good day!\nHow about you?'
    print(character_base(sent))
    print(whitespace_seg(sent))
