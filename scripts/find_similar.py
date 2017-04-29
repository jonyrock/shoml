import numpy as np
import os
import sys
import csv

path = sys.argv[1]
out_path = sys.argv[2]


root_dir = "../"
data_dir = root_dir + "shoml_data/"
csv_file = "athletic_flatten.csv"
features_dir = root_dir + "features/"
input_filename = path
features_filename = path + ".f"



def load_array(filename):
    with open(filename) as file:
        res = np.load(file)
        return np.reshape(res, 25088)



os.system("python test.py " + input_filename + " " + features_filename)


image_array = load_array(features_filename)


result = []

with open(csv_file) as list_file:
    reader = csv.reader(csv_file, delimiter=' ')
    for row in reader:
        name = row[0]
        url = row[1]
        filename = features_dir + name + ".jpg.f"
        if not os.path.exists(features_dir + filename):
            continue
        current_array = load_array(features_dir + filename)
        mod = np.product(current_array)
        if mod > 0.:
            cur_dist = float(np.dot(image_array, current_array)) / np.product(current_array)
            result.append([cur_dist, url])

result.sort()
size = min(10, len(result))
for i in range(size):
    print(result[i][1])