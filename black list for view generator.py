import os
import json


cwd = os.getcwd()

imagesdir = cwd+"\products"

black_list = []

for subdir, dirs, files in os.walk(imagesdir):

	black_list=black_list+dirs

json = json.dumps(black_list)
formatted_json = json.replace("\\\\","/")

file = open("black list.json","w")
file.write(formatted_json)
file.close()



