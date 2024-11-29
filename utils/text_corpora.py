import nltk
import time

def download_corpora():
    # Download corpora to make TF-IDF understand which language it refers to
    nltk.download('stopwords')
    time.sleep(0.5)
    nltk.download('wordnet')
    time.sleep(0.5)
    nltk.download('punkt')