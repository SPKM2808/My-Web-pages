#! /usr/bin/env python3
import os
from PIL import Image

files=os.listdir('./supplier-data/images/')

for x in files:
        if x.startswith('0'):
                #print(x)      
                im=Image.open('./supplier-data/images/'+x).convert("RGB")
                im.resize((600,400)).save('./supplier-data/images/'+x.replace('tiff','jpeg'))
