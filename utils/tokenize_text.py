from utils.text_clean import preprocess_and_clean

def tokenize(sentence):
  '''
    INPUT: This func receives input from text_clean.preprocess_and_clean
    LOGIC: 
        1. It will tokenize manually which takes a word and its next word, respectively
        2. If it comes to the very last word, it will not pair with any other words.
        3. This is so-called unigram and bigram pairs
    OUTPUT:
        1. It returns pair of unigram and bigram tokens.
        This is done to make sure our TF-IDF understand more context. By calculate what word follows
        any word.
  '''
  cleaned_text = preprocess_and_clean(sentence)
  # Unigrams stop right here
  text_split   = cleaned_text.split()
  text_arr     = []

  for index, word in enumerate(text_split):
    text_arr.append(word)

    # Check whether index of a word is last index or no
    # If yes, then no need to pair it with next pairs
    if index != (len(text_split) - 1):
      text_arr.append(" ".join([word, text_split[index + 1]]))
  return text_arr