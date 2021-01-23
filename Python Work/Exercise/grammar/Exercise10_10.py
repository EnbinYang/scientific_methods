def count_common_words(filename, word):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        
        msg = word + " appears in " + filename + " about " + str(word_count) + " times."
        print(msg)

filename = 'alice.txt'
count_common_words(filename, 'the')