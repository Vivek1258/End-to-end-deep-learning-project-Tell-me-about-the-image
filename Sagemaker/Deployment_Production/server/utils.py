import os

import pickle
from pickle import load

import numpy as np
from numpy import argmax

from tok import num_to_word , word_to_num 

import tensorflow as tf 

from PIL import Image 

def load_model():
    
    """ Function to load the model """
    
    model = tf.keras.applications.vgg16.VGG16()
    model.layers.pop()
    new_model = tf.keras.models.Model(inputs=model.inputs, outputs=model.layers[-1].output)
    
    print("Model Loaded ...") 
    return new_model


def extract_features(img):

    """ 
    Function to extract features from an image using VGG16 model
    
    Parameter :  A PIL Image object 
        
    Returns a feature vector of length 1000 
    
    """ 
    
    # newsize = (224, 224) 
    # img = img.resize(newsize) 
    
    # reshape & prepare the image for the VGG model
    image = tf.keras.preprocessing.image.img_to_array(img)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = tf.keras.applications.vgg16.preprocess_input(image)
    
    
    model =  load_model()
    
    feature = model.predict(image, verbose=0)[0] # The output shape is (1, 1000) but we want only (1000,) 
    
    
    return feature

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


    


    
