from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
import sys

path = sys.argv[1]
out_path = sys.argv[2]

model = VGG16(weights='imagenet', include_top=False)

img_path = path
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

features = model.predict(x)
#print(features)
features.dump(out_path)