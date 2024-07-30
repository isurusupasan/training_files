import pandas as pd
import numpy as np
import json
import random
from tqdm import tqdm
import cv2
import os
import glob
from PIL import Image
from torchvision.transforms.functional import perspective
import warnings
warnings.filterwarnings('ignore')


#add data into new json file
def add_data(new_data, filename='training_data.json'):
    #to check whether file is 
    if os.path.exists(filename):
        #load the existing data
        with open(filename, 'r') as f:
            try:
                data=json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        #if the file not existed start with empty list
        data = []

    #append the new data
    data.append(new_data)
    
    #write updated data back to the file
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

    print("Data has been added to '{filename}'")




# Manual check scores
match_id = '20130607-M-Roland_Garros-SF-Novak_Djokovic-Rafael_Nadal'
if os.path.exists('%s.json' % match_id):
    file_name = '%s.json' % match_id
else:
    print("error importing")
    #new_json_file = []
json_file = json.load(open(file_name))

for clip_id, clip in enumerate(json_file):
    if clip ['check'] == 'NA':
        print(clip_id, clip)
        add_data(clip)
    

print('Filtered data has been written to the jason file')


        

    


