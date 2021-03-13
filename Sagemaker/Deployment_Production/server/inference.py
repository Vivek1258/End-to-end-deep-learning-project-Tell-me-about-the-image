import json
import os
import pickle
import requests
from pickle import load

import numpy as np
import tensorflow as tf 

from PIL import Image 

from utils import  id_to_word , texts_to_sequences , extract_features


def handler(data, context):
    
    """Handle request.
    Args:
        data (obj): the request data
        context (Context): an object containing request and configuration details
    Returns:
        (bytes, string): data to return to client, (optional) response content type
    """
    
    img = _process_input(data, context)
    
    
    feature = extract_features(img)
    
    
    print("sending processed_input to context.rest_uri:", context.rest_uri)
    
    
    """ generate the description of an image"""
    
    in_text = 'startseq' # to seed the generation process
    
    max_length = 34 # maximun length of the sequence 
    
    for i in range(max_length):
        
        
        # integer encode and pad input sequence 
        sequence = texts_to_sequences([in_text])
        sequence = tf.keras.preprocessing.sequence.pad_sequences([sequence], maxlen=max_length)[0]
    
        # predict next word
        input_data_np_json = {
                             "instances" : [{   
                                            "input_1": feature.tolist() , 
                                            "input_2": sequence.tolist()  
                                            }]
                              }
        
        # ref 1  : https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/using_tf.html
        
        # ref 2 https://stackoverflow.com/questions/57730978/error-in-giving-inputs-to-the-tensorflow-serving-model-on-sagemaker-error
 

        input_data_np_json_serialized = json.dumps(input_data_np_json)
        
        # send a POST request to the model ( TensorFlow Serving REST API )
        response = requests.post(context.rest_uri, data= input_data_np_json_serialized ) 
        
        result = response.json() # get the result dict from the response 
        
        yhat = np.argmax(result['predictions'][0]) # find the word_index of the highest probability word 
        
        # map integer to word
        word = id_to_word(yhat )
  
        
        # stop if we cannot map the word
        if word is None:
            break
        
        in_text += ' ' + word # append the input for generating the next word
        
        # stop if we predict the end of the sequence
        if word == 'endseq':
            break
       
    
    op_text = " ".join(in_text.split(" ")[1:-1])
    
    return _process_output(op_text, context)



def _process_input(data, context):
    
    """ 
    Pre-process request input before it is sent to TensorFlow Serving REST API
    
    Args:
        data (obj): the request data, in format of dict or string
        context (Context): an object containing request and configuration details
        
    Returns: a numpy array contaning image features 
         
    """
    
    
    if context.request_content_type == 'application/json':
        
        # pass through json (assumes it's correctly formed)
        
        d = json.loads(data.read().decode('utf-8'))
        
        arr = np.asarray(d if len(d) else '')
        
        arr = (arr * 255).astype(np.uint8)
        
        img = Image.fromarray(arr)

        return img
         
        
    raise ValueError('{{"error": "unsupported content type {}"}}'.format(
        context.request_content_type or "unknown"))


def _process_output(data, context):
    
    """
    Post-process TensorFlow Serving output before it is returned to the client.
    Args:
        data (obj): the TensorFlow serving response
        context (Context): an object containing request and configuration details
    Returns:
        (json_object, string): data to return to client, response content type
        
    """
    
    response_content_type = context.accept_header
    
    prediction = json.dumps(data)
    
    return prediction, response_content_type
