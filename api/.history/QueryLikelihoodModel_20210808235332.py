import re
import math
import numpy as np

UNK = None
SENTENCE_START = "<s>"
SENTENCE_END = "</s>"

ALPHA = 0.75
NORMALIZE_PROBABILITY = True

class UnigramLanguageModel:
    def __init__(self, sentences: list, mode="collection", smoothing=False):

        '''
            sentences: sentences of the dataset
            mode: whether this language model is for the whole corpus/collection or just a single document
            smoothing: add-one smoothing
        '''
        self.sentences = sentences
        self.mode = mode

        #for add one smoothing
        self.smoothing = smoothing

        
    def calculate_unigram_probability(self, word: str):
        '''
            calculate unigram probability of a word
        '''
        total_number_of_words = 0
        frequency_of_word = 0
        for sentence in self.sentences:
            for word_in_sentence in sentence:
                if word_in_sentence != SENTENCE_START and SENTENCE_END:
                    if word_in_sentence == word:
                        frequency_of_word += 1
                    total_number_of_words += 1
        
        if (self.smoothing and frequency_of_word == 0):
            frequency_of_word = 1

        return (frequency_of_word/total_number_of_words)
    
def calculate_interpolated_sentence_probability(sentence:list, doc:UnigramLanguageModel, collection: UnigramLanguageModel, alpha=ALPHA, normalize_probability=NORMALIZE_PROBABILITY):
    '''
        calculate interpolated sentence/query probability using both sentence and collection unigram models.
        sentence: input sentence/query
        doc: unigram language model a doc. HINT: this can be an instance of the UnigramLanguageModel class
        collection: unigram language model a collection. HINT: this can be an instance of the UnigramLanguageModel class
        alpha: the hyperparameter to combine the two probability scores coming from the document and collection language models.
        normalize_probability: If true then log of probability is not computed. Otherwise take log2 of the probability score.
    '''
    total_score = 1
    for word in sentence:
        if word != SENTENCE_START and word != SENTENCE_END:
            score_of_word = alpha*(doc.calculate_unigram_probability(word)) + (1 - alpha)*(collection.calculate_unigram_probability(word))
            total_score *= score_of_word

    if normalize_probability == True:
        return total_score
    else:
        return (math.log(total_score)/math.log(2))

def return_max_doc(doc1, doc2, doc3):
    #print ("doc1: {}, doc 2: {}, doc3: {}".format(doc1, doc2, doc3))
    return max(doc1, doc2, doc3)

if __name__ == '__main__':
    '''
        Question: for each of the test queries given in test.txt, find out best matching document/doc
        according to their interpolated sentence probability.
        Optional: Extend the model to bigram language modeling.
    '''

    
    collectionUnigramLanguageModel = UnigramLanguageModel(actual_dataset, smoothing=True)
    doc1UnigramLanguageModel = UnigramLanguageModel(doc1_dataset, smoothing=False)
    doc2UnigramLanguageModel = UnigramLanguageModel(doc2_dataset, smoothing=False)
    doc3UnigramLanguageModel = UnigramLanguageModel(doc3_dataset, smoothing=False)

    for sentence in actual_dataset_test:
        doc1score = calculate_interpolated_sentence_probability(sentence, doc1UnigramLanguageModel, collectionUnigramLanguageModel)
        doc2score = calculate_interpolated_sentence_probability(sentence, doc2UnigramLanguageModel, collectionUnigramLanguageModel)
        doc3score = calculate_interpolated_sentence_probability(sentence, doc3UnigramLanguageModel, collectionUnigramLanguageModel)

        highest_score = return_max_doc(doc1score, doc2score, doc3score)

        if highest_score == doc1score:
            doc = "doc 1"
        elif highest_score == doc2score:
            doc = "doc 2"
        elif highest_score == doc3score:
            doc = "doc 3"

        sentence.remove(SENTENCE_START)
        sentence.remove(SENTENCE_END)
        sentence_join = " ".join(sentence)
        if highest_score != 0:
            print ("For the sentence: '{}', the most relevant doc was {}, with a score of {} \n".format(sentence_join, doc, highest_score))
            pass
        else: 
            print ("For the sentence: '{}', the highest score was 0, hence no doc was returned \n".format(sentence))
            pass

    
    
