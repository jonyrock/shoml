import numpy as np
import os
import sys
import csv

path = sys.argv[1]
out_path = sys.argv[2]


root_dir = "../"
data_dir = root_dir + "shoml_data/"
csv_file = data_dir + "athletic_flatten.csv"
features_dir = root_dir + "features/"
input_filename = path
features_filename = path + ".f"



def load_array(filename):
    with open(filename) as file:
        res = np.load(file)
        return np.reshape(res, 25088)



os.system("python test.py " + input_filename + " " + features_filename)


image_array = load_array(features_filename)
print image_array

result = []

with open(csv_file) as list_file:
    for row in list_file.readlines():
        tokens = row.split(' ')
        name = tokens[0]
        url = tokens[1]
        filename = features_dir + name + ".jpg.f"
        #print(filename)
        if not os.path.exists(filename):
            continue
        current_array = load_array(filename)
        mod = np.sqrt(np.dot(current_array, current_array))
        
        cur_dist = float(np.dot(image_array, current_array)) / mod
        result.append([cur_dist, name, url])

result.sort()
result.reverse()
size = min(10, len(result))
for i in range(size):
    print(result[i])
