import os
import sys
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np


path = sys.argv[1]
fpath = sys.argv[2]

model = VGG16(weights='imagenet', include_top=False)

def dumpOn(full_path):
    img_path = full_path
    if os.path.exists(full_path)
        return
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    features = model.predict(x)
    #print(features)

    rel_path = full_path.split('/')[-1]
    # print(fpath + '/' + rel_path + '.f')
    features.dump(fpath + '/' + rel_path + '.f')

total_items = 0

for dirName, subdirList, fileList in os.walk(path):
    # print('Found directory: %s' % dirName)
    for fname in fileList:
        full_path = os.path.join(os.path.abspath(dirName), fname)

        file_extension = os.path.splitext(fname)[1]
        if file_extension == '.jpg':
            total_items += 1
            # dumpOn(full_path)

items = 0

for dirName, subdirList, fileList in os.walk(path):
    # print('Found directory: %s' % dirName)
    for fname in fileList:
        full_path = os.path.join(os.path.abspath(dirName), fname)

        file_extension = os.path.splitext(fname)[1]
        if file_extension == '.jpg':
            items += 1
            print(str(items) + "/" + str(total_items))
            dumpOn(full_path)
            # print("image: " + full_path)
        # print('\t%s' % fname)
