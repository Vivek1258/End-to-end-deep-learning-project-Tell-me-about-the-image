
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
 
![image](https://user-images.githubusercontent.com/53163419/109760212-56a86a00-7c14-11eb-8933-239c0908d4c7.png)



## Data 

link : https://www.kaggle.com/shadabhussain/flickr8k


The dataset used for this project is the “Flickr8K” dataset[3].
Flickr8K dataset includes images obtained from the Flickr web-site
It is a labeled dataset. 
The dataset consists of 8000 photos.
There are 5 captions for each photo.
The dataset can be found at Kaggle[3]
The dataset is small and the size is 1.14 GB.
Thus this dataset is best for this project.



## Algothrims

We will use a combination of CNN(Convolutional Neural Network) and RNN(Recurrent Neural Network) to develop this system.
First, we will extract features of the image by using CNN, and then we will feed this feature vector to an LSTM language model that will generate captions. Thus we will have a CNN Encoder and an LSTM Decoder. (LSTM is a special kind of RNN, capable of learning long-term dependencies). We will also use pre-trained models on a standard Imagenet dataset(provided in Keras) to develop the CNN encoder. We will use pre-trained GLOVE 200d embeddings for words to improve the performance of our language model.

#### Thus this algorithm is a good example where we are using concepts like  Image Processing,  Natural Language Processing, and  Transfer learning.

 
 
## Metrics

There are various ways to measure the performance of an image captioning model like BLEU, ROUGE, CIDEr, METEOR, SPICE, etc. but out of these BLEU( Bilingual Evaluation Understudy) is most common and widely used in the evaluation of image annotation results, which is based on the n-gram precision. For this project, we will be using the BLUE score to check and compare the performance of our model. The principle of the BLEU measure is to calculate the distance between the evaluated and the reference sentences. BLEU method tends to give a higher score when the caption is closest to the length of the reference statement.


## Machine Learning Engineer Nanodegree 

I got to learn advanced machine learning techniques and algorithms and how to package and deploy trained models to a production environment. Gained practical experience using Amazon SageMaker to deploy trained models to a web application and evaluate the performance of the models. Also A/B testing on models and learned how to update the models as you gather more data, an important skill in industry. 

![image](https://user-images.githubusercontent.com/53163419/109755751-9408f980-7c0c-11eb-8635-2f424f4db3b6.png)



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
 
