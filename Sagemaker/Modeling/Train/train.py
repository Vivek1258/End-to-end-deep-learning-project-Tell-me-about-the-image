# train.py


import argparse
import os
import numpy as np
import json


## Get the model 

from model import get_model 

import tensorflow as tf



def _load_training_data(train_dir):
    """ loading training data from S3 """

    X1train = np.load(os.path.join(train_dir, 'X1train.npz'))['arr_0']
    X2train = np.load(os.path.join(train_dir, 'X2train.npz'))['arr_0']

    ytrain = np.load(os.path.join(train_dir, 'ytrain.npz'))['arr_0']

    return X1train,  X2train , ytrain

def _load_testing_data(test_dir):
    """ loading testing data from S3 """

    X1test = np.load(os.path.join(test_dir, 'X1test.npz'))['arr_0']
    X2test = np.load(os.path.join(test_dir, 'X2test.npz'))['arr_0']
    ytest = np.load(os.path.join(test_dir, 'ytest.npz'))['arr_0']

    return X1test,  X2test , ytest


def _parse_args():
    
    """ Parsing the arguments """
    parser = argparse.ArgumentParser()

    # Data, model, and output directories
    # model_dir is always passed in from SageMaker. By default, this is an S3 path under the default bucket.
    parser.add_argument('--model_dir', type=str)

    parser.add_argument('--sm-model-dir', type=str, default=os.environ.get('SM_MODEL_DIR'))

    parser.add_argument('--train', type=str, default=os.environ.get('SM_CHANNEL_TRAIN'))
    parser.add_argument('--test', type=str, default=os.environ.get('SM_CHANNEL_TEST'))


    return parser.parse_known_args()


if __name__ == "__main__":

    # parsing the arguments
    args, unknown = _parse_args()

    # loading the train and test data
    X1train,  X2train , ytrain = _load_training_data(args.train)
    X1test,  X2test , ytest = _load_testing_data(args.test)
    
    # get model  

    model = get_model()

    #compile

    opt = tf.keras.optimizers.Adam(lr = 0.001)
    BATCH__SIZE = 128

    model.compile(optimizer=opt,
              loss='categorical_crossentropy',
              )

    # train on 10 epoches
    model.fit(
          [ X1train,  X2train ], 
          ytrain, 
          batch_size = BATCH__SIZE ,
          epochs=3, 
          verbose=2,
          validation_data=( [ X1test,  X2test ] , ytest)
          )
          
    print("Saving The model ...." )
    
    model.save(os.path.join(args.sm_model_dir, '0001'), 'my_model_ic.h5')
    
    
