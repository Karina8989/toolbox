import nltk
#pip install unidecode
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

from nltk.corpus import stopwords 
import string
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize

def clean(text):
    for punctation in string.punctuation:
        text = text.replace(punctation,'') #remove punctation
    lowercased = text.lower() #lower case
    tokenized = word_tokenize(lowercased)
    words_only = [word for word in tokenized if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    without_stopwords = [word for word in words_only if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(word) for word in without_stopwords]
    return lemmatized

