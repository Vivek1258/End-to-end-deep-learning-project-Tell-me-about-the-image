# Automatic-Image-Captioning
Machine Learning Engineer Nanodegree Capstone Project


Vivek Mankar 

mankarvivek172000@gmail.com

Pune India


 
## OVERVIEW

Artificial Intelligence shows us the tremendous possibility to change our way of working in different fields. Take the “Snapshot Serengeti”[1] project, Where more than 200 automatic cameras across the Savannah have amassed millions of photos of animals. But wildlife Biologists have had trouble figuring out how to actually deal with all that information. Means those were just photos and they needed data ( example, “Two lions are eating a buffalo“  rather than an Image )  which is easier to store and manipulate. Turning all those photos into data has taken more than  30,000 hours. The scientists build a computer program using AI( which usages Image classification and image captioning)  that completed the task in just one day. 
In this project, we will develop and deploy a Deep Learning model that can automatically generate captions for the given image[2]. We will use the Flickr8K dataset[3] to train our model and streamlit package to develop a simple UI so that users can play with it.

## PROBLEM STATEMENT

Image captioning has various applications in virtual assistants, for image indexing, for visually impaired persons, for social media, and several other natural language processing applications. 
For a scientific project Generating captions for images can become a tedious task and take years to complete. One of the examples is Project Snapshot Serengeti. 
Can we have a simple webpage that can allow the user to try and play with the image captioning models? 
PS: Develop a system that can automatically generate captions for a given image.

## INSTALLATION 
``` 
git clone 
cd 
streamlit run main.py 
```


## METRICS

There are various ways to measure the performance of an image captioning model like BLEU, ROUGE, CIDEr, METEOR, SPICE, etc.[4] but out of these BLEU( Bilingual Evaluation Understudy) is most common and widely used in the evaluation of image annotation results, which is based on the n-gram precision. [5 ] For this project, we will be using the BLUE score to check and compare the performance of our model. The principle of the BLEU measure is to calculate the distance between the evaluated and the reference sentences. BLEU method tends to give a higher score when the caption is closest to the length of the reference statement.
Scores are calculated for individual translated segments—generally sentences—by comparing them with a set of good quality reference translations. Those scores are then averaged over the whole corpus to reach an estimate of the translation's overall quality. Intelligibility or grammatical correctness are not taken into account. BLEU's output is always a number between 0 and 1. This value indicates how similar the candidate text is to the reference texts, with values closer to 1 representing more similar texts. Few human translations will attain a score of 1, since this would indicate that the candidate is identical to one of the reference translations. For this reason, it is not necessary to attain a score of 1. Because there are more opportunities to match, adding additional reference translations will increase the BLEU score.[8]


## DATA EXPLORATION 
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
In deep learning, a convolutional neural network (CNN, or ConvNet) is a class of deep neural networks, most commonly applied to analyzing visual imagery. CNN’s are regularized versions of multilayer perceptrons. Multilayer perceptrons usually mean fully connected networks, that is, each neuron in one layer is connected to all neurons in the next layer. The "fully-connectedness" of these networks makes them prone to overfitting data. Typical ways of regularization include adding some form of magnitude measurement of weights to the loss function. CNN takes a different approach towards regularization: they take advantage of the hierarchical pattern in data and assemble more complex patterns using smaller and simpler patterns. Therefore, on the scale of connectedness and complexity, CNNs are on the lower extremity.[9]
Long short-term memory (LSTM) is an artificial recurrent neural network (RNN) architecture used in the field of deep learning. Unlike standard feedforward neural networks, LSTM has feedback connections. It can not only process single data points (such as images), but also entire sequences of data (such as speech or video). LSTMs were developed to deal with the vanishing gradient problem that can be encountered when training traditional RNNs. Relative insensitivity to gap length is an advantage of LSTM over RNNs, hidden Markov models, and other sequence learning methods in numerous applications. The advantage of an LSTM cell compared to a common recurrent unit is its cell memory unit. The cell vector has the ability to encapsulate the notion of forgetting part of its previously-stored memory, as well as to add part of the new information. To illustrate this, one has to inspect the equations of the cell and the way it processes sequences under the hood.
First, we will extract features of the image by using CNN, and then we will feed this feature vector to an LSTM language model that will generate captions. Thus we will have a CNN Encoder and an LSTM Decoder. (LSTM is a special kind of RNN, capable of learning long-term dependencies). We will also use pre-trained models on a standard Imagenet dataset(provided in Keras) to develop the CNN encoder. We will use pre-trained GLOVE 200d embeddings for words to improve the performance of our language model.


Thus this algorithm is a good example where we are using concepts like  Image Processing,  Natural Language Processing, and  Transfer learning.




 
