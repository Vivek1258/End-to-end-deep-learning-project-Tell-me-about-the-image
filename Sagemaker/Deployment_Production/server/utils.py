import os

import pickle
from pickle import load

import numpy as np
from numpy import argmax

from tok import num_to_word , word_to_num 


# tokenizer = load(open('tokenizer.pkl' ,'rb'))


def id_to_word(integer):
    
    """ function to map an integer to a word"""
    try :
        return num_to_word[str(integer)]
    except :
        return None

    
    
def texts_to_sequences(lis):
    
    """ function to  encode word to a number """

    return [int(word_to_num[word]) for word in lis[0].split()]


    


    