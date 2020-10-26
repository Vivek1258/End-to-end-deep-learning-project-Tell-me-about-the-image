

from keras.models import Model

from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.image import img_to_array

from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input

 

class utils():
    def extract_features(self, img):

      # load  & re-structure the model
      model = VGG16()
      model.layers.pop()
      model = Model(inputs=model.inputs, outputs=model.layers[-1].output)
 

      # reshape & prepare the image for the VGG model
      image = img_to_array(img)
      image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
      image = preprocess_input(image)

      feature = model.predict(image, verbose=0)

      del model

      return feature


     
 
    def id_to_word(self, integer, tokenizer):
    	for word, index in tokenizer.word_index.items():
    		if index == integer:
    			return word
    	return None
 
 

