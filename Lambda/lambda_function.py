import json

import numpy as np

from SME_caller import gen_caption

def lambda_handler(event, context):
    # TODO implement
     
    data = json.loads(event['body'])
    
    data = json.loads(data) 
    
    data = data['data']
    
    img = np.asarray(data)  
    
    caption = gen_caption(img)
    
    return {
        'statusCode': 200,
        'body': json.dumps(caption)
    }
