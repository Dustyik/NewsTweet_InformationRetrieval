from BM25implementation import BM25Class, QueryParsers
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import tempfile
import numpy as np
import pandas as pd
from BM25implementation import *

MIN_COUNT = 5 #min count of words when training model, default is 5
SIZE = 50 #dimensions of embedding, default 100
WORKERS = 3 #number of partitions during training, default workers is 3, used for training parallelization 
WINDOW = 3 #max window size of words around it, default 5 
SG = 0 #training algo, either CBOW (0) or SKIPGRAM (1), default CBOW
VECTOR_SIZE = 100 #dimensional space that Word2Vec maps the words onto, default 100
EPOCHS = 1

GENSIM_MODEL_FILEPATH = ""

class Word2VecModel:
    def __init__(self, tweets_data):
        self.tweets_data = tweets_data
        self.corpus = self.process_corpus(tweets_data)
        self.model = self.create_model(self.corpus)
        
    def process_corpus(self, tweets_data):
        list_of_list = [row.split(',') for row in tweets_data.clean_text]
        return list_of_list
        
    def create_model(self, corpus):
        return Word2Vec(sentences = corpus, 
                        min_count = MIN_COUNT,
                        workers = WORKERS, 
                        window = WINDOW, 
                        sg = SG,
                        vector_size = VECTOR_SIZE)
    
    def store_model(self):
        with tempfile.NamedTemporaryFile(prefix='IR-gensim-model', delete=False) as tmp:
            temporary_filepath = tmp.name
            print ("Saving Model Temporary Filepath", temporary_filepath)
            self.save(temporary_filepath)
            
    def load_model(self):
        loaded_model = Word2Vec.load(GENSIM_MODEL_FILEPATH)
        return loaded_model
    
    def train_model(self):
        self.model.train()
        
    def document_embedding_w2v(self, clean_text):
        doc_tokens = list(clean_text.split(" "))
        print (doc_tokens)
        embeddings = []
        if len(doc_tokens) < 1:
            return np.zeros(VECTOR_SIZE)
        else:
            for tok in doc_tokens:
                #if tok in self.model.wv.vocab:
                embeddings.append(self.model.wv.word_vec(tok))
                #else:
                #    embeddings.append(np.random.rand(VECTOR_SIZE))
            # mean the vectors of individual words to get the vector of the document
            return np.mean(embeddings, axis=0)
        
    
    def return_most_significant_tweets(self, query):
        query_vector = QueryParsers(query).query
        print
        #self.tweets_data["vector"] = self.tweets_data.apply(lambda row:(self.document_embedding_w2v(row.clean_text)), axis=1)
        return 
        self.tweets_data['similarity']=self.tweets_data['vector'].apply(lambda x: cosine_similarity(np.array(query_vector).reshape(1, -1),np.array(x).reshape(1, -1)).item())
        self.tweets_data.sort_values(by='similarity',ascending=False,inplace=True)
        
        return 
    
        
    #function to tokenize query
    
        
    