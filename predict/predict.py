
# Python script to Generate the captions for the given image 

import numpy as np
from numpy import argmax
from keras.preprocessing.sequence import pad_sequences

from predict.processer import utils

ut = utils()

class caption_generator():

	def generate_caption(self, model, tokenizer, photo, max_length):

		text_input = 'startseq'
		
		for i in range(max_length): # iterate over the whole length of the sequence
	 
			seq = tokenizer.texts_to_sequences([text_input])[0]
			padded_seq = pad_sequences([seq], maxlen=max_length) # padding to the max_length 
			
			y_hat = argmax(model.predict([photo,padded_seq], verbose=0))# predicting next word
			
	  
			# map integer to word
			word = ut.id_to_word(y_hat, tokenizer)
			if word is None:
				break
			text_input += ' ' + word

			if word == 'endseq':
				break


		return text_input


 

