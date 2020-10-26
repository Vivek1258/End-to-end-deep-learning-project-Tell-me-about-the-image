def get_pd():
	markdown = """

In this project, we will develop and deploy a Deep Learning model that can automatically generate captions for the given image. We will use the Flickr8K dataset to train our model and streamlit package to develop a simple UI so that users can play with it.


## INSTALLATION 
``` 
git clone https://github.com/Vivek1258/Automatic-Image-Captioning.git
cd Automatic-Image-Captioning
pip install requirements.txt
streamlit run main.py 
```


## METRICS

There are various ways to measure the performance of an image captioning model like BLEU, ROUGE, CIDEr, METEOR, SPICE, etc. but out of these BLEU( Bilingual Evaluation Understudy) is most common and widely used in the evaluation of image annotation results, which is based on the n-gram precision. For this project, we will be using the BLUE score to check and compare the performance of our model. The principle of the BLEU measure is to calculate the distance between the evaluated and the reference sentences. BLEU method tends to give a higher score when the caption is closest to the length of the reference statement.


## DATA EXPLORATION 

link : https://www.kaggle.com/shadabhussain/flickr8k


The dataset used for this project is the “Flickr8K” dataset[3].
Flickr8K dataset includes images obtained from the Flickr web-site
It is a labeled dataset. 
The dataset consists of 8000 photos.
There are 5 captions for each photo.
The dataset can be found at Kaggle[3]
The dataset is small and the size is 1.14 GB.
Thus this dataset is best for this project.

 

 

## ALGORITHMS AND TECHNIQUES 

We will use a combination of CNN(Convolutional Neural Network) and RNN(Recurrent Neural Network) to develop this system.
First, we will extract features of the image by using CNN, and then we will feed this feature vector to an LSTM language model that will generate captions. Thus we will have a CNN Encoder and an LSTM Decoder. (LSTM is a special kind of RNN, capable of learning long-term dependencies). We will also use pre-trained models on a standard Imagenet dataset(provided in Keras) to develop the CNN encoder. We will use pre-trained GLOVE 200d embeddings for words to improve the performance of our language model.

#### Thus this algorithm is a good example where we are using concepts like  Image Processing,  Natural Language Processing, and  Transfer learning.


 For complete documentation checkout : 

 



	"""

	return markdown


def get_um():
	markdown = """
	## About Me

#### Name : Vivek Ravindra Mankar 
#### [LinkedIn](https://www.linkedin.com/in/vivek-mankar-182735184/)


### Degrees& Nano-Degrees
 
#### ENTC enginnering

#### Machine Learning Enginnering
		
### Licenses & certifications

#### Specilization  in Deep Learning
by [deeplearning.ai](https://www.deeplearning.ai/)

#### Specilization in Applied data science
by IBM
 
### Honors & Awards

#### AWS Machine Learning Scholorship
-- Selected among top 325 students around the globe

#### Winner: 
Deep Leaning Hackathon by Syngenta India Pvt. Ltd.

### Volunteer Experience
#### 1. Enginnering Lead 
[Aivatan.ml](https://aivatan.herokuapp.com/)
 
#### 2. AI/ML Team-Lead 
[needmoremed.com](https://needmoremed.com/)


#### [Email](mankarvivek172000@gmail.com) 
#### [GitHub](https://github.com/Vivek1258)'
 

#### [LinkedIn](https://www.linkedin.com/in/vivek-mankar-182735184/)
"""
	return markdown