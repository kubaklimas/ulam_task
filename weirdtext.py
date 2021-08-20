import random, re


tokenize_re = re.compile(r'(\w+)', re.U)


def encode_word(word):
    if len(word) > 3:
        encoded_word = word
        while encoded_word == word:
            is_shuffled = True
            first_letter = word[0]
            last_letter = word[-1]
            letters_to_shuffle = [x for x in word[1:-1]]

            if letters_to_shuffle.count(letters_to_shuffle[0]) == len(letters_to_shuffle):
                encoded_word = word
                is_shuffled = False
                break

            random.shuffle(letters_to_shuffle)
            letters_to_shuffle.insert(0,first_letter)
            letters_to_shuffle.append(last_letter)

            encoded_word = ''.join(letters_to_shuffle)

    else:
        is_shuffled = False
        encoded_word = word
    return encoded_word, is_shuffled


def encoder(text):    
    shuffled_words = []
    splited_text = tokenize_re.split(text)

    for word in splited_text:
        encoded_word, is_shuffled = encode_word(word)
        if is_shuffled == True:
            shuffled_words.append(word)
            index = splited_text.index(word)
            splited_text[index]=encoded_word

    separator = '\n—weird—\n'
    encoded_text = ''.join(splited_text)
    print(encoded_text)
    print(separator,sorted(shuffled_words,key=str.lower))

    return encoded_text, shuffled_words


def decoder(encoded_text,shuffled_words):    
    splited_text = tokenize_re.split(encoded_text)
    
    for word in splited_text:
        if len(word)>3:
            for original_word in shuffled_words:
                if word[0]==original_word[0] and word[-1]==original_word[-1] and len(word)==len(original_word):
                    try:
                        splited_text[splited_text.index(word)]=original_word
                    except:
                        print("Exception while reading values")
    print(''.join(splited_text))
    
original_text = '''
This is a long looong test sentence,\n
with some big (biiiiig) words! '''

encoded_text, shuffled_words = encoder(original_text)
decoder(encoded_text,shuffled_words)


original_text = '''
I dont know what i wrote here hire hore,
bananas, baaanas, bataeas '''

encoded_text, shuffled_words = encoder(original_text)
decoder(encoded_text,shuffled_words)

#comss
