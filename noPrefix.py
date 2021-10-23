def noPrefix(words):
    for i, word in enumerate(words):
        for other in words[:i]:
            if word.startswith(other) or other.startswith(word):
                print('BAD SET')
                print(word)
                return
    print('GOOD SET')

def noPrefix(words):
    prefixes = set()
    processed_words = set()
    for word in words:
        if word in prefixes:
            print('BAD SET')
            print(word)
            return
        prefix = ''
        for c in word:
            prefix += c
            prefixes.add(prefix)
            if prefix in processed_words:
                print('BAD SET')
                print(word)
                return
        processed_words.add(word)
    print('GOOD SET')