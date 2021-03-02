

# importing neccossory liberies

import tensorflow as tf


def get_model(input_im_feature_shape = 1000  , vocab_size = 7579 , max_length = 34 ):
    
    
    """
    creates an encoder decocer  arcitechure

    Parameters:

    input_im_feature_shape 
    ==> The shape of the feature vector 
    of the images extrated using Transfer learniong model 

    vocab_size ==> size of the vocabolary ( determined during data preprocessing )

    max_length ==> maximum length of input sequence 

    Returns:
    keras.models.Model object 

    """

    # feature extractor model

    inputs1 = tf.keras.layers.Input(shape=(input_im_feature_shape,))
    
    fe1 = tf.keras.layers.Dense(256, activation='relu')(inputs1)
    fe2 = tf.keras.layers.Dropout(0.3)(fe1)


    # sequence model
    inputs2 = tf.keras.layers.Input(shape=(max_length,))
    
    se1 = tf.keras.layers.Embedding(vocab_size, 256, mask_zero=True)(inputs2)
    se2 = tf.keras.layers.Dropout(0.3)(se1)


    #merge layer
    merge = tf.keras.layers.Add()([fe2, se2]) 

    #language model

    decoder = tf.keras.layers.LSTM(256)(merge)
     

    #fully connected

    decoder__ = tf.keras.layers.Dense(1024, activation='relu')(decoder)
    bn = tf.keras.layers.BatchNormalization()(decoder__)
    do = tf.keras.layers.Dropout(0.1)(bn)


    outputs = tf.keras.layers.Dense(vocab_size, activation='softmax')(do)

    # tie it together [image, seq] [word]

    model = tf.keras.models.Model(inputs=[inputs1, inputs2], outputs=outputs)


    return model