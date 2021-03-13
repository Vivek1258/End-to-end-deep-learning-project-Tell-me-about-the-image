
import boto3
import json
import numpy as np 

# define gloabel vareables
ENDPOINT_NAME = 'tensorflow-inference-2021-03-12-16-23-57-315'
sm_runtime_client= boto3.client('runtime.sagemaker')

## Note : Change the timeout settings to 10 sec

def gen_caption(img):
    
    """ Function to generate caption for the given image """
    
    """ Sagemaker Model End Point caller function """
    
    print("the shape of the imge is " , img.shape)
    
    image_list = img.tolist()
    image_json = json.dumps(image_list)
    
    ## invoke endpoint for inference
    response = sm_runtime_client.invoke_endpoint(
                                                EndpointName = ENDPOINT_NAME,
                                                Body=image_json,
                                                ContentType="application/json",
                                                )
    caption = json.loads(response['Body'].read().decode('utf-8'))
    
    return caption
