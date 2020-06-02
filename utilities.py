import json
import pickle
import pandas as pd

def save_dict_to_file(filename,dict_to_save):
    with open(filename+'.json', 'w+') as fd:
        json.dump(dict_to_save, fd)
        
def load_dict_from_file(filename):
    with open(filename +'.json') as f:
        loaded_dict = json.load(f)
    return loaded_dict
            
def load_set_from_file(filename):
    with open (filename, 'rb') as fp:
        loaded_set = pickle.load(fp)
    return loaded_set

def save_dataFrame(data_frame,filePath):
    data_frame.to_csv(filePath +'.csv',index=False)
    
def load_dataFrame(filePath):
    return pd.read_csv(filePath+'.csv')

