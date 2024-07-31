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



#to filter neseted values
def filter_keys(data, keys_to_keep):
    if isinstance(data, dict):
        return {key: filter_keys(value, keys_to_keep) for key, value in data.items() if key in keys_to_keep}
    elif isinstance(data, list):
        return [filter_keys(item, keys_to_keep) for item in data]
    else:
        return data
    

#add data into new json file
def add_data(new_data, keys_to_keep, filename='training_data.json'):

    #filter the data that needs to remain
    filtered_data = filter_keys(new_data, keys_to_keep)

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

    # change the name of fine_label into label  
    
    #append the new data
    data.append(filtered_data)
    
    #write updated data back to the file
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

    print("Data has been added to '{filename}'")

# # to change the fine-label into label
def rename(data, old_key, new_key):
    
    if isinstance(data, dict):
        # print('a')
        # print('----------------------')
        #to delete the frames without labels
        for key in list(data.keys()):
            if data.fromkeys(old_key) is None or old_key=="":
                del data[key]
            # print('b')
            # print(data.values())
            # if key == "frame":
            #     # print(data.fromkeys("frame"))
            #     # if data[old_key] is None or data[old_key] == "":
            #     #      del data[key]
            if key == old_key:
                # print(old_key)
                # print(new_key)
                # print('c')
                data[new_key]=data.pop(old_key)
                # print('d')
                # print(key)

            else:
                rename(data[key], old_key, new_key)
            # print('e')
                
    elif isinstance(data, list):
        for item in data:
            # print('f')
            rename(item, old_key, new_key)
            # print('g')
    return data                

# upload the json into code
match_id = '20130607-M-Roland_Garros-SF-Novak_Djokovic-Rafael_Nadal'
if os.path.exists('%s.json' % match_id):
    file_name = '%s.json' % match_id
else:
    print("error importing")
    #new_json_file = []
json_file = json.load(open(file_name))
# check new method
updated_json = rename(json_file, "fine_label", "label")
# print(updated_json)

for clip_id, clip in enumerate(updated_json): 
    if clip ['check'] == 'NA':
        print(clip_id, clip)
        keys_to_keep = ["events", "frame", "label", "check", "fps", "num_frames", "video", "far_name", "far_hand", "far_set", "far_game", "far_point", "near_name", "near_hand", "near_set", "near_game", "near_point"]
        add_data(clip, keys_to_keep)


# print('Filtered data has been written to the jason file')


        

    


