
from pickle import load
from keras.models import load_model
from predict.processer import utils
from predict.predict import caption_generator
from keras.preprocessing.image import load_img
from PIL import Image
import base64
import os 


ut = utils()

cg = caption_generator()

def gen_cap(input_image , model , tokenizer , max_length = 34 ):
	img =  input_image
	img.save("img.jpg")
	image = load_img("img.jpg", target_size=(224, 224))
	os.remove("img.jpg")
	photo = ut.extract_features(image)
	# generate description
	description = cg.generate_caption(model, tokenizer, photo, max_length)
	des = description[8:-6]
	return  des


