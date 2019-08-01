# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:48:50 2019

@author: Kedir
"""
from google.colab import files
import glob 
import svnh_semi_supervised_model_train as train
import zipfile

train.main()
model_files = sorted(glob.glob('./checkpoints/*'))

zipf = zipfile.ZipFile('checkpoints.zip', 'w', zipfile.ZIP_DEFLATED)
for file in model_files:
    zipf.write(file)

#files.download('./checkpoints.zip')
