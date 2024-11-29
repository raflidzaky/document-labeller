# Delete stopwords
import re
import string
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

'''
    This module is used to pre-process the data. It receives INPUT from text_parser.extract_from_pdf().
    Those texts will be pre-processed here such as:
    1. Erasing numbers, links, punctuations, and lower them
    2. Eliminate stopwords (like 'a', 'the', and else)
    3. Transform each word to their base word (lemmatization). For example, 'doing' becomes 'do'
    4. Unify each preprocessing steps into one single logic (preprocess_and_clean) function

    It returns cleaned text that is being ready to be tokenized.
'''

def preprocess_text(text):
    '''Preprocess text by making it lowercase, removing text in square brackets, removing links, removing punctuation, and removing words containing numbers.'''
    cleaned_text = re.sub(r'\[.*?\]|\w*\d\w*|https?://\S+|www\.\S+|<.*?>+|[%s]' % re.escape(string.punctuation), '', str(text).lower())
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)  
    cleaned_text = re.sub(r'\n+', ' ', cleaned_text)
    return cleaned_text

def eliminate_stopwords(text):
    '''Remove stopwords from the text'''
    stop_words = stopwords.words('english')
    # Tokenize words (splitting it piece by piece)
    words = text.split(' ')
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

# I skip stemming because it also filter out non-suffixes --> for example, athlete become athlet which is not contextual.
def apply_lemms(sentence):
    lemms = WordNetLemmatizer()

    # Unite the words as a compact sentence again
    return ' '.join(lemms.lemmatize(word) for word in sentence.split(' '))

def preprocess_and_clean(sentence):
    '''Preprocess and clean the text'''
    cleaned_text = preprocess_text(sentence)
    stop_words = stopwords.words('english')
    removed_stopwords_text = ' '.join(word for word in cleaned_text.split(' ') if word not in stop_words)
    lemms_text = ' '.join(apply_lemms(word) for word in removed_stopwords_text.split(' '))
    return lemms_text