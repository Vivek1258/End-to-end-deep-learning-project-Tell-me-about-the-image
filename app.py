import streamlit as st 
import numpy as np
from PIL import Image
from pickle import load
from AIC import gen_cap
from keras.models import load_model
from doc import get_pd , get_um
import base64
import os 



max_length = 34 
model_path = "predict/model/saved_model_26_10_2020_No_of_epochs_10"
tokenizer_path = "predict/model/tokenizer.pkl"


@st.cache(suppress_st_warning=True)
def load_models(tokenizer_path , model_path):
    # load the tokenizer
    tokenizer = load(open(tokenizer_path, 'rb'))
    # load the model
    model = load_model(model_path)

    return model , tokenizer 



    
 
#with open("style.css") as f:
#    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)    
  

#################### TITLE SECTION ##############################

################### MAIN PAGE ###################################


st.title("Automatic Image Captioning")
#st.subheader("*Machine Learning Nanodegree Capstone Project*")

################ SLIDE BAR ####################################


st.sidebar.header('Hello, *World!* :sunglasses:')
st.sidebar.write("""

				I am Vivek and this is my Machine Learning Enginnering Nanodegree Cpstone Project.

				""" )

 


file_image = st.file_uploader("Upload your photoes here", type=['jpg'])

if st.button("check"):
	if file_image :
		#try :
		model , tokenizer = load_models(tokenizer_path , model_path)
		input_img = Image.open(file_image)
		st.write("**Input Photo**")
		st.image(input_img, use_column_width=True)
		#check = st.button("check")
		caption = gen_cap(input_img , model , tokenizer , max_length)
		st.write("**Generated Caption **")
		st.success("***" + caption + "***")
 
		#except:
		#	st.error(""" Unable to process 
		#	""")

	else :
		st.error("""Bad input ........:( ! 
			Please make sure the file upload is sucessful 
			""")
 


#################### BUTTONS: PROJ DOC   ##############################

proj_doc = None 
proj_doc = st.sidebar.button("Project Documentation and Code")

if proj_doc :

	st.write(get_pd())



#################### BUTTONS: ABOUT ME  ###############################


about = st.sidebar.button("""About Me""")

if about :
	st.write(get_um())
	





 
