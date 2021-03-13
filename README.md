
# AIC(Automatic-Image-Captioning)- Bot
### Machine Learning Engineer Nanodegree Capstone Project

![Github License](https://img.shields.io/aur/license/android-studio)
![Code Coverage](https://img.shields.io/badge/coverage-80%25-green)
![python Version](https://img.shields.io/pypi/pyversions/Django)
 
## Table of content

- [Project Overview ](#Project-Overview )
- [Output](#Output)
- [Data](#Data)
- [Algothrims](#Algothrims)
- [Metrics](#Metrics)
- [Machine Learning Nanodegree Graduation](#Machine-Learning-Engineer-Nanodegree)
- [Built With](#built-with)
- [Contributing](#contributing)
- [License](#license)
- [Get Help](#get-help)
- [Contact](#contact)


## Project Overview

In this project, I have developed a web application that can automatically generate Captions for the given Image using Deep Learning. The Deep Learning Model is developed, trained, and deployed(as a REST API ) on AWS Cloud using  SageMaker, Lambda Function, S3 Storage, and API GateWay services. I have used Streamlit UI to develop the Frontend of the web app. The FrontEnd is deployed on Heroku Cloud.

![image](https://user-images.githubusercontent.com/53163419/109759121-940bf800-7c12-11eb-827d-8d5a135c51f6.png)



## Output 
 
![image](https://user-images.githubusercontent.com/53163419/110333609-c8831800-8047-11eb-8a4d-5102f7daa946.png)



## Data 

The dataset used for this project is the “Flickr8K” dataset. Flickr8K dataset includes images obtained from the Flickr web-site
 - It is a labeled dataset. 
 - The dataset consists of 8000 photos.
 - There are 5 captions for each photo.
 - The dataset is small and the size is 1.14 GB.
 - The dataset can be found at Kaggle


link : https://www.kaggle.com/shadabhussain/flickr8k

## Algothrim

I have used a combination of CNN(Convolutional Neural Network) and RNN(Recurrent Neural Network) to develop this system. i.e. The model we will have a CNN Encoder and an LSTM Decoder.

![image](https://user-images.githubusercontent.com/53163419/110330610-f8302100-8043-11eb-8534-bbc082af77c9.png)


First, I have extracted the features of an image by using CNN, and then we will feed this feature vector to an LSTM language model that will generate captions.  (LSTM is a special kind of RNN, capable of learning long-term dependencies). 

I have also used pre-trained models on a standard Imagenet dataset(provided in Keras) to develop the CNN encoder and GLOVE 200d embeddings for words to improve the performance of our language model.


#### Thus this algorithm is a good example where we are using concepts like  Image Processing,  Natural Language Processing, and  Transfer learning.

 
 
## Metrics

There are various ways to measure the performance of an image captioning model like BLEU, ROUGE, CIDEr, METEOR, SPICE, etc. but out of these BLEU( Bilingual Evaluation Understudy) is most common and widely used in the evaluation of image annotation results. 


For this project, I have used the BLUE score to check and compare the performance of our model. The principle of the BLEU measure is to calculate the distance between the evaluated and the reference sentences. BLEU method tends to give a higher score when the caption is closest to the length of the reference statement.


## Machine Learning Engineer Nanodegree 

I got to learn advanced machine learning techniques and algorithms and how to package and deploy trained models to a production environment. Gained practical experience using Amazon SageMaker to deploy trained models to a web application and evaluate the performance of the models. Also A/B testing on models and learned how to update the models as you gather more data, an important skill in industry. 

![image](https://user-images.githubusercontent.com/53163419/111025500-86bced80-840a-11eb-8fdb-8b8e1d3e7b74.png)




## Built With

Python

TensorFlow 

Keras 

Streamlit UI


## Contributing

#### Issues
In the case of a bug report, bugfix or suggestions, please feel free to open an issue.

#### Pull request
Pull requests are always welcome, and I will do my best to do reviews as fast as we can.


## License

This project is licensed under the [Apache License](https://github.com/Vivek1258/Django-Ecommerce-website-backend/blob/main/LICENSE)

## Get Help

- If appropriate, [open an issue](https://github.com/Vivek1258/End-to-end-deep-learning-project-Tell-me-about-the-image/issues) on GitHub

## Contact 

- Contact me on [LinkedIn](https://www.linkedin.com/in/vivek-mankar-182735184/) 
- Email mankarvivek172000@gmail.com
 
