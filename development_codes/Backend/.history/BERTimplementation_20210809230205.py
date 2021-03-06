from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances


def create_BERT_embeddings(tweets_data):
    print ("In BERT function")
    sbert_model = SentenceTransformer('bert-base-nli-mean-tokens')
    document_embeddings = sbert_model.encode(tweets_data['clean_text'])

    pairwise_similarities=cosine_similarity(document_embeddings)
    pairwise_differences=euclidean_distances(document_embeddings)
    
    print (pairwise_similarities)

    #most_similar(0,pairwise_similarities,'Cosine Similarity')
    #most_similar(0,pairwise_differences,'Euclidean Distance')

'''
def most_similar(doc_id,similarity_matrix,matrix):
    print (f'Document: {documents_df.iloc[doc_id]["documents"]}')
    print ('\n')
    print ('Similar Documents:')
    if matrix=='Cosine Similarity':
        similar_ix=np.argsort(similarity_matrix[doc_id])[::-1]
    elif matrix=='Euclidean Distance':
        similar_ix=np.argsort(similarity_matrix[doc_id])
    for ix in similar_ix:
        if ix==doc_id:
            continue
        print('\n')
        print (f'Document: {documents_df.iloc[ix]["documents"]}')
        print (f'{matrix} : {similarity_matrix[doc_id][ix]}')
'''