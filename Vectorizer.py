import re
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import os
import math
import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer 
import pickle
import re
import numpy as np
from utilities import load_dict_from_file,load_dataFrame,save_dataFrame
from Configuration import path_data_frame,path_to_vectorizer,path_to_document_tfidf,path_to_document_folder
from string import digits



# this removes the punctuation and gets the token.
def removePunctuationAndGetTokens(lines):
    remove_digits = str.maketrans('', '', digits)
    lines = lines.translate(remove_digits)
#     pattern = re.compile('[0-9].*')
#     lines = re.sub(pattern,' ',lines)
#     print(lines)
    translator = str.maketrans(string.punctuation,' '*len(string.punctuation))
    lines = lines.translate(translator)
    tokens = lines.split()
    return tokens

# takes list of words as a input and do stemming stopword removal and also removes token which are of length less than 
# or equal to two 
def removeSingleDoubleCharacterWordStopWordsAndStemming(tokens):
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    tokens = [ps.stem(token) for token in tokens if token not in stop_words] 
#     print(tokens) 
    return ' '.join([token for token in tokens if len(token)>2 and token not in stop_words])


# It creates the dataframe out of files which store URL and its content.
def create_data_frame_from_documents(folderName):
    df = pd.DataFrame()
    for fileName in os.listdir(folderName):
#         if fileName in ['10.txt','100.txt','103.txt','104.txt']:
            pathName = folderName+'\\'+ fileName
            fp = open(pathName, 'r',encoding='utf-8')
            url = fp.readline().split(':',1)[1].replace('\n','')
            url = url.strip()
            lines = fp.read()
            content = removeSingleDoubleCharacterWordStopWordsAndStemming(removePunctuationAndGetTokens(lines))
            doc_id = fileName.replace(".txt", "")
            df = df.append({'Doc_id':int(doc_id),'URL':url,'Content':content},ignore_index=True)
    return df
        
    
# This calculate the tf-idf of all the URL contents    
def calculate_tfidf_of_documents(dataframe_file):
    
    df = load_dataFrame(dataframe_file)
    df.sort_values(by=['Doc_id'], inplace=True)
    tfidf_vectorizer=TfidfVectorizer(use_idf=True)
    tfidf_documents=tfidf_vectorizer.fit_transform(df['Content'].values.astype('U'))
    return tfidf_vectorizer,tfidf_documents


def load_vectors(filename):
    with open(filename+'.pk', 'rb') as fp:
        return pickle.load(fp)

def save_vectors(vector,filename):
    pickle.dump(vector, open(filename+'.pk', 'wb'),protocol=pickle.HIGHEST_PROTOCOL)

# This function calculates the TF-IDF of query depending on the vectorizer we have saved earlier
def calculate_tfidf_of_query(query,tfidf_vectorizer):
    processed_query = removeSingleDoubleCharacterWordStopWordsAndStemming(removePunctuationAndGetTokens(query))
    return tfidf_vectorizer.transform([query])
    
# Main function that triggers the complete TF-IDF calculation process
def main():
    docu_df = create_data_frame_from_documents(path_to_document_folder)
    save_dataFrame(docu_df,path_data_frame)
    vectorizer, doc_tf_idf = calculate_tfidf_of_documents(path_data_frame)
    save_vectors(vectorizer,path_to_vectorizer)
    save_vectors(doc_tf_idf,path_to_document_tfidf)
    

    