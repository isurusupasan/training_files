import pandas as pd
import numpy as np
import json
from tqdm import tqdm 
import glob 
import warnings 
warnings.filterwarnings('ignore') 
paths = glob.glob('./tennis_data_update_v1/*.json') 
output_dir = 'output_tennis_data' 
for file_name in paths: 
    new_json_file = [] 
    json_file = json.load(open(file_name)) 
    for clip_id, clip in tqdm(enumerate(json_file)):
        if clip['check'] != 'NA': 
            continue 
        new_events = []
        for event_id, event in enumerate(clip['events']):
            if 'bounce' not in event['coarse_label']: 
                new_events.append({'frame': event['frame'], 'label': event['coarse_label']}) 
                clip['events'] = new_events 
                new_json_file.append(clip) 
                with open(file_name.replace('tennis_data_update_v1', output_dir), 'w') as outfile:
                    json.dump(new_json_file, outfile, indent=2)