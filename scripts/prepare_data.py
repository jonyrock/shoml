import os

root_dir = "/home/user/"
data_dir = root_dir + "shoml_data/"
features_dir = root_dir + "features/"
scripts_dir = root_dir + "scripts/"
list_filename = data_dir + "folders_list.csv"
database = data_dir + "database.csv"
extract_features = scripts_dir + "extract_features.py"


with open(list_filename) as list_file:
    with open(database, "w+") as out_file:
        for line in list_file.readlines():
            dir_name = line.strip()
            image_dir = data_dir + dir_name
            os.system("python " + extract_features + " " + image_dir + " " + features_dir)

            for dirName, subdirList, fileList in os.walk(image_dir):
                # print('Found directory: %s' % dirName)
                for fname in fileList:
                    full_path = os.path.join(os.path.abspath(dirName), fname)

                    name = fname.split(".")[0]
                    file_extension = os.path.splitext(fname)[1]
                    if file_extension == '.jpg':
                        out_file.write(name + " http://142.0.206.116:3001/" + dir_name + fname + "\n")

