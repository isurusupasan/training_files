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
    
#to find the next key    
# def next_key(data, current_key):
#     if isinstance(data, dict):
#         key = list(data.keys())
#         try:
#             current_index = key.index(current_key)
#             next_key = key[current_key+1]
#             print(next_key)

#         except(ValueError, IndexError):
#             print("no next key found")
#     else:
#         next_key(data, current_key)


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

    #print("Data has been added to '{filename}'")


# to delete the frames without labels
def remove_keys(data, remove_key):
    #print(remove_key)
    if isinstance(data, dict):
        for key, value in data.items():
            #print(f"key : {key}")
            #print(key,value)
            if(key == "events"):
                #print("*********u*********")
                #print(key, value)
                events = remove_keys(value, remove_key)
                #print(events)
                for i in events:
                    if len(i) == 3:
                        del i
                        #print(i)
                        json.dumps(data)
                    #    removed_value = key.pop(i)

                    #    print(removed_value)
                       
                #if remove_key not in events:
                #     print("fuck")
                #print(events)
                # if remove_key not in events:
                #     print("fuck")
                #print("########u#########")
            #print(key)
            #if key == "events":
                #print("d")
            #print("++++++b++++++")
    elif isinstance(data, list):
            for index, item in enumerate(data):
                #print(f"Index: {index}")
                #print(list(item))
                # for i in list(item):
                #     print(i)
                remove_keys(item, remove_key)
                #print(index, item)
                #print("####a#####")
    #else:
        #print(f"value: {data}")
    #print(data)
    #print(data)
    return data            

# def delete(data, remove_key):
#     if isinstance(data, dict):
#         keys_to_delete = [key for key, value in data.items() if isinstance(value, dict) or remove_key not in value]
#         print(keys_to_delete)
#         for key in keys_to_delete:
#             print(key)
#             del data [key]
            
#         for key, value in data.items():
#             delete(value, remove_key)

#     elif isinstance(data, list):
#         for item in data:
#             delete(item, remove_key)

    # data = json.dumps(data)
    return data
# # to change the fine-label into label
def rename(data, old_key, new_key):
    
    if isinstance(data, dict):
        for key in list(data.keys()):
            #print(data.keys())
            if key == old_key:
                data[new_key]=data.pop(old_key)
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
#to find the next key
# nextkey = next_key(json_file, "frame")

#to delete the frames without labels
updated_json1 = remove_keys(json_file, "fine_label")
print(updated_json1)

# # # check new method
updated_json = rename(updated_json1, "fine_label", "label")
# # # print(updated_json)



for clip_id, clip in enumerate(updated_json): 
    if clip ['check'] == 'NA':
        #print(clip_id, clip)
        keys_to_keep = ["events", "frame", "label", "check", "fps", "num_frames", "video", "far_name", "far_hand", "far_set", "far_game", "far_point", "near_name", "near_hand", "near_set", "near_game", "near_point"]
        add_data(clip, keys_to_keep)


print('Filtered data has been written to the jason file')


        

    


