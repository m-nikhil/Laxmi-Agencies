import os
import json

cwd = os.getcwd()

imagesdir = cwd+"\\navigation"

black_list = []

for subdir, dirs, files in os.walk(imagesdir):

	black_list.append(os.path.relpath(subdir,os.path.dirname(subdir)))


del black_list[0]

json = json.dumps(black_list)
formatted_json = json.replace("\\\\","/")

file = open("black list navigation.json","w")
file.write(formatted_json)
file.close()