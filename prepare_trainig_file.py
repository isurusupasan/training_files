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
if os.path.exists('.json' % match_id):
    file_name = '.json' % match_id
else:
    file_name = '.json' % match_id

new_json_file = []
json_file = json.load(open(file_name))

print(json_file)
