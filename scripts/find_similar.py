import numpy as np
import os
import sys

path = sys.argv[1]
out_path = sys.argv[2]


root_dir = ".."
features_dir = root_dir + "/features"
input_filename = path
features_filename = path + ".f"



def load_array(filename):
    with open(filename) as file:
        return np.load(file)


os.system("test.py " + input_filename + " " + features_filename)


image_array = load_array(features_filename)


result = []

for filename in os.listdir(features_dir):
    if filename.endswith(".jpg.f"):
        current_array = load_array(filename)
        cur_dist = float(np.dot(image_array, current_array)) / np.product(current_array)
        result.append([cur_dist, filename])

result.sort()
size = min(10, len(result))
for i in range(size):
    print(result[i][1])