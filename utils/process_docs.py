from sklearn.feature_extraction.text import TfidfVectorizer
from utils.tokenize_text import tokenize

def define_model():
   '''
      This function will return TF-IDF feature extractor to supply
      the web with. 
   '''
   vectorizer = TfidfVectorizer()
   return vectorizer
   
def simplify_docs(sentence):
   '''
      This function is used to create a TF-IDF score based on tokenize_text.tokenize()
      function. This function typically works in two ways:
      1. It extracts calculated features (which are tokens)
      2. It calculate TF (frequency) and IDF (importance) score of each features

      INPUT: 
      Input is parameterized on sentence args. It is supposed to be filled by extracted PDF texts.
      Thus, this func will calculate TF-IDF score based on that input

      OUTPUT:
      The final output of this function is top 3 feature with highest possible TF-IDF scores.
      Meaning it is frequent and it is important.
   '''

   # Get the text token 
   tokenized_text = tokenize(sentence)

   # Pack the token to a compact document (a single string).
   document = ' '.join(tokenized_text)
   
   # Call the TF-IDF
   vectorizer = define_model()

   # Pack a string to an iterable (list-form). Since there is only a string, it iterates just one
   # TF-IDF requires an iterable data types.
   tfidf_matrix = vectorizer.fit_transform([document])

   # Extract features 
   feature_names = vectorizer.get_feature_names_out()

   # For each features, sort by the top 3 highest possible TF-IDF score. Merge the feature to each score
   for index, vector in enumerate(tfidf_matrix):
    scores = vector.toarray().flatten()
    top_indices = scores.argsort()[-3:][::-1]
    top_terms = [(feature_names[i], scores[i]) for i in top_indices]

   return top_terms