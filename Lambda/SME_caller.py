import boto3
import json
import numpy as np 

# define gloabel vareables
ENDPOINT_NAME = 'tensorflow-inference-2021-03-01-16-42-22-041'
sm_runtime_client= boto3.client('runtime.sagemaker')


def gen_caption(img_features):
    
    """ Function to generate caption for the given image """
    
    """ Sagemaker Model End Point caller function """
    
    image_list = img_features.tolist()
    image_json = json.dumps(image_list)
    
    ## invoke endpoint for inference
    response = sm_runtime_client.invoke_endpoint(
                                                EndpointName = ENDPOINT_NAME,
                                                Body=image_json,
                                                ContentType="application/json",
                                                )
    caption = json.loads(response['Body'].read().decode('utf-8'))
    
    return caption
    
