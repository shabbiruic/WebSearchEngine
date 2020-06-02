from sklearn.metrics.pairwise import cosine_similarity
from Configuration import path_to_page_rank,path_data_frame,path_to_vectorizer,path_to_document_tfidf
from Vectorizer import calculate_tfidf_of_query,load_vectors
from utilities import load_dict_from_file,load_dataFrame
import numpy as np

# this fetchs the given number of relevant documents depending on the cosine similarity.
def get_relevant_document_list(query,number_of_results):
    docu_df = load_dataFrame(path_data_frame)
    vectorizer = load_vectors(path_to_vectorizer)
    query_tfidf = calculate_tfidf_of_query(query,vectorizer)
    doc_tfidf = load_vectors(path_to_document_tfidf)
    similarity = cosine_similarity(doc_tfidf,query_tfidf)
    flat = similarity.flatten()
    indexs = np.argpartition(flat, -1*number_of_results)[-1*number_of_results:]
    return docu_df.loc[docu_df['Doc_id'].isin(indexs)]['URL'].tolist()


# It orders the given documents on the basis of their page ranks
def order_by_page_rank(url_list,path_to_page_rank):

    global_page_rank_dict = load_dict_from_file(path_to_page_rank)
    page_rank_dict ={}
    order_url_list=[]
    for url in url_list:
        page_rank_dict[url] = global_page_rank_dict[url]
    for k in sorted(page_rank_dict, key=page_rank_dict.get, reverse=True):
        order_url_list.append(k)
    return order_url_list

# Accepts the input query and gives the relevant url in a order of relevence.
def search(query,number_of_results):
    url_list = get_relevant_document_list(query,number_of_results)
    return order_by_page_rank(url_list,path_to_page_rank)