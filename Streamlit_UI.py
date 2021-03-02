import streamlit as st 
import numpy as np
from PIL import Image
from pickle import load
import base64
import os 
from FrontEnd.caller import gen_cap

import tensorflow as tf 
# load  & re-structure the model

@st.cache(suppress_st_warning=True)
def load_model():
		model = tf.keras.applications.vgg16.VGG16()
		model.layers.pop()
		return tf.keras.models.Model(inputs=model.inputs, outputs=model.layers[-1].output)


feature_extrator_model =  load_model()


st.title("AIC-Bot")
st.subheader("*I can Tell you whats going on in an Image* :sunglasses: ")

################ SLIDE BAR ####################################

st.sidebar.header('Hello, World!')
st.sidebar.write("""
				I am Vivek and this is my Machine Learning Enginnering Nanodegree Cpstone Project.
				""" )

 
file_image = st.file_uploader("Upload your photoes here", type=['jpg'])


if st.button("check"):
	if file_image :
		
		input_img = Image.open(file_image)

		st.write("**Input Photo**")
		st.image(input_img, use_column_width=True)
 

		caption = gen_cap(input_img, feature_extrator_model)

		st.write("**Generated Caption **")
		st.success( caption )

	else :
		st.error("""Bad input ........:( ! 
			Please make sure the file upload is sucessful 
			""")
 

 
	





 