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


# Manual check scores
match_id = '20130607-M-Roland_Garros-SF-Novak_Djokovic-Rafael_Nadal'
if os.path.exists('%s.json' % match_id):
    file_name = '%s.json' % match_id
else:
    print("error importing")
    
new_json_file = []
json_file = json.load(open(file_name))

#print(json_file)

for clip_id, clip in enumerate(json_file):
    if clip ['check'] == 'NA':
        print(clip_id, clip)


    


