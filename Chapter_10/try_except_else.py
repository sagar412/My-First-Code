# Working of try_except_esle with multiple files
def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_word = len(words)
        print(f" The file {filename.title()} has {num_word} number of words.")
