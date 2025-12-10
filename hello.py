import ntlk

def hello ():
    print("Hello")


def tokenize_sentence(sentence:str) -> list[str]:
    return [word for word in nltk.word_tokenize(sentence) if any(c.isalpha() for c in word)]

def convert_uppercase(s:str) -> str:
    return s.upper()