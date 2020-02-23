#!/usr/bin/env python
# coding: utf-8

# ## loading SEED IV EOG data

# In[4]:


import scipy.io as sio

import numpy as np
from datetime import datetime, date, time
import pandas as pd
import os

#from lib.get_data import cutting_window_data


import pickle
import json
from random import shuffle


# ### get labels corresponding to eog data

# In[7]:


#directory where all data is stored
dir_ = ''
#dir where eog feature smooth data is stored 
eog_dir_ = dir_ + 'eye_feature_smooth/'

#extracted labels from README file
session1_label = [1,2,3,0,2,0,0,1,0,1,2,1,1,1,2,3,2,2,3,3,0,3,0,3]
session2_label =  [2,1,3,0,0,2,0,2,3,3,2,3,2,0,1,1,2,1,0,3,0,1,3,1]
session3_label = [1,2,2,1,3,3,3,1,1,2,1,0,2,3,3,0,2,3,0,0,2,0,1,0]

label_dict = {
    '1': session1_label,
    '2': session2_label,
    '3': session3_label
}

nb_of_trials = 24

channel_order = pd.read_excel(dir_ + 'Channel Order.xlsx', sheet_name=0, header = None)
channel_names = channel_order[0].values
channel_names


# ### get eog data from different sessions

# In[37]:


#get all necessary metainformation
filenamelist = list()
participantlist = list()


#store all information in this dict
metadata_ = dict() 

for sess in os.listdir(eog_dir_):
    sess_label = label_dict[sess]
    for file in os.listdir(eog_dir_ + '/' + sess):
        #get absolute path
        file_abs_path = eog_dir_ + '/' + sess + '/' + file
        #append absolute path due to nested session folders
        filenamelist.append(file_abs_path)
        
        #get participant id from filename (first number) -> in total we have 15 participants
        participant = int( file.split('_')[0] )
        participantlist.append(participant)
        metadata_[file] = dict()
        metadata_[file]['participant'] = participant
        metadata_[file]['labels'] = sess_label
        metadata_[file]['abspath'] = file_abs_path
        metadata_[file]['sess'] = sess
        
        print('file: {0}, participant:{1}'.format(file, participant))


# In[68]:


#save all data in this dict
all_data = dict()

index = 0
#open each file
for file in metadata_.keys():
    print(metadata_[file])
    participant = metadata_[file]['participant']
    labels = metadata_[file]['labels']
    #open file
    mat = sio.loadmat(metadata_[file]['abspath'])
    
    #each mat file consists of 24 trials
    session_keys = [x for x in mat.keys() if 'eye' in x]
    for session_key_ in session_keys:
        session_key_index = int( session_key_.split('_')[1] ) #get number (x) after 'eye_{x}'
        
        data_session = mat[session_key_]
        
        #get label of specific session
        label = labels[session_key_index - 1]
        
        
        all_data[index] = dict()
        all_data[index]['data'] = data_session
        all_data[index]['participant'] = participant
        all_data[index]['label'] = label
        index +=1
    


# In[76]:


shape_ = list()
for i in all_data.keys():
    print( all_data[i]['data'].shape ) #uneven number of columns
    shape_.append(all_data[i]['data'].shape[1] ) 
    


# In[97]:


#minimum number of obs
min_index = min(shape_)

max_index = max(shape_)

X = [] #eye input data
Y = [] #label data
P = [] #participant data


# In[98]:


for index_obs in all_data.keys():
    #print(index_obs)
    X.append( all_data[index_obs]['data'][:, ::] )
    Y.append( all_data[index_obs]['label'] )
    P.append( all_data[index_obs]['participant'] )
    
X = np.asarray(X)
Y = np.asarray(Y)
P = np.asarray(P)


np.save(eog_dir_+ 'data_X', X)
np.save(eog_dir_+ 'data_Y', Y)
np.save(eog_dir_+ 'data_P', P)


# ## save as file

# In[105]:





# In[ ]:




