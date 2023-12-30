from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import nltk
import re


class TextCleanPDF:
    def __init__(self, raw_text: str):
        self.text = raw_text
        text_list = self.text.split()
        main_terms = []
        flag = 0
        for text in text_list:
            if text.lower() == "text":
                flag = 0
            if flag == 1:
                main_terms.append(text.lower())
            if text.lower() == "lecture":  # Lecture
                flag = 1
        self.text = " ".join(main_terms)
        self.text_tokenize()
        # self.text_stemming()
        self.text_lemmatizer()
        self.text_remove_stop()
        self.text_remove_punc_number()

    def text_tokenize(self):
        def tokenization(text):
            tokens = text.split()
            return tokens

        self.text = tokenization(self.text)

    def text_stemming(self):
        def stemming(text):
            porter_stemmer = PorterStemmer()
            stem_text = [porter_stemmer.stem(word) for word in text]
            return stem_text

        self.text = stemming(self.text)

    def text_remove_stop(self):
        stopwords = nltk.corpus.stopwords.words('english')

        def remove_stopwords(text):
            output = [i for i in text if i not in stopwords]
            return output

        self.text = remove_stopwords(self.text)

    def text_lemmatizer(self):
        wordnet_lemmatizer = WordNetLemmatizer()

        def lemmatizer(text):
            lemm_text = [wordnet_lemmatizer.lemmatize(word) for word in text]
            return lemm_text

        self.text = lemmatizer(self.text)

    def text_remove_punc_number(self):
        def clean_punctuations(text):
            py_opstr = re.sub(r'[^\w\s0-9]', '', text)
            return py_opstr

        def clean_number(text):
            py_opstr = re.sub(r'[0-9]', '', text)
            return py_opstr

        result = []
        for i in self.text:
            a = clean_punctuations(i)
            a = clean_number(a)
            if a:
                result.append(a)
        self.text = result


class TextClean(TextCleanPDF):
    def __init__(self, raw_text):
        self.text = raw_text
        self.text_tokenize()
        self.text_lemmatizer()
        self.text_remove_stop()
        self.text_remove_punc_number()