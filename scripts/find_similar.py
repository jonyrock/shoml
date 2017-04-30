import numpy as np
import os
import sys
import simplejson as json

path = sys.argv[1]
out_path = path + ".json"


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

weights = []

with open(csv_file) as list_file:
    for row in list_file.readlines():
        tokens = row.strip().split(' ')
        name = tokens[0]
        url = tokens[1]
        filename = features_dir + name + ".jpg.f"
        if not os.path.exists(filename):
            continue
        current_array = load_array(filename)
        mod = np.sqrt(np.dot(current_array, current_array))
        
        cur_dist = float(np.dot(image_array, current_array)) / mod
        weights.append([cur_dist, name, url])

weights.sort()
weights.reverse()
size = min(10, len(weights))
result = []
for i in range(size):
    result.append({
        'name': weights[i][1],
        'image': weights[i][2],
        'weight': weights[i][0],
    })

with open(out_path, "w+") as file:
    file.write(json.dumps(result, ensure_ascii=False))
