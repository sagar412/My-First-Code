glossary = {
    'print':'get the output on the screen.',
    'get' : 'get value of a key if its value is not prsent in the key.',
    'title': 'just changing the first letter of the word into captals',
    'del': 'delete the value of a list or a key value pair from a dictionary',
}
for word, use in glossary.items():
    print(f"\n{word.title()}: is used to {use}")
