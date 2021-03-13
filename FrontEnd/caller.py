import numpy as np
from PIL import Image

import json 
import requests


# import tensorflow as tf 


# def extract_features(img, model):
    
#     newsize = (224, 224) 
#     img = img.resize(newsize) 
    
#     # reshape & prepare the image for the VGG model
#     image = tf.keras.preprocessing.image.img_to_array(img)
#     image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
#     image = tf.keras.applications.vgg16.preprocess_input(image)
    
#     feature = model.predict(image, verbose=0)
    
#     return feature



def gen_cap(img  ):


	# img = extract_features(img, feature_extrator_model)


	#print(str(img[0]))


	newsize = (224, 224) 
	img = img.resize(newsize) 

	img= np.asarray(img)


	# calling the API endpoint 
	data = {
	        "data":  img.tolist()
	       }


	# print(data)

	Endpoint_URL = "https://2ep4arfqn8.execute-api.us-east-1.amazonaws.com/prod"

	response = requests.post( Endpoint_URL , json = json.dumps(data)).json()

	return response
