import os
import json


cwd = os.getcwd()

imagesdir = cwd+"\products"


Dir = {}

key = []

x=[]

for subdir, dirs, files in os.walk(imagesdir):
	for file in files:

		relDir = os.path.relpath(subdir,imagesdir)
		menu_links_source = "\\"+relDir+"\\"+file
		

		Filepath = os.path.join(subdir, file)
		Sub = os.path.dirname(subdir)
		relFilepath = os.path.relpath(Filepath,Sub)
		menu_links = os.path.dirname(relFilepath)

		if(not Dir.has_key(str(menu_links))):
			Dir[str(menu_links)] = []

		Dir[str(menu_links)].append(menu_links_source)



	#x.append(os.path.relpath(subdir,imagesdir));

#print x;



Dir_grouped = {}
group = []


for menu_links in Dir:
	Dir_grouped[menu_links] = []
	count = 0
	for menu_links_source in Dir[menu_links]:
		if(count == 9):
			Dir_grouped[menu_links].append(group)
			group = []
			group.append(menu_links_source)
			count = 0
		else:
			count = count+1
			group.append(menu_links_source)

	Dir_grouped[menu_links].append(group)
	group = []
	count = 0



json = json.dumps(Dir_grouped)
formatted_json = json.replace("\\\\","/")

file = open("product_database.json", "w")
file.write(formatted_json)
file.close()





