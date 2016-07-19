import os
import shutil

cwd = os.getcwd()

# Create a folder "brands" in the same directory/location of the "products"
# Rename the image to be used as "folder.png" and place it again in the same directory

imagesdir = cwd+"\products"

to_dir = cwd+"\\navigation"+"\\Brands\\"


dir = []

for subdir, dirs, files in os.walk(imagesdir):

	file = ((to_dir+os.path.relpath(os.path.dirname(subdir),imagesdir)).replace("\\","/"))


	if os.path.relpath(os.path.dirname(subdir),imagesdir) == ".":
		continue

	if os.path.relpath(subdir,imagesdir) == ".":
		continue

	

	if not os.path.exists(file):
		os.makedirs(file)

	shutil.copyfile("folder.png",file+"\\"+os.path.relpath(subdir,os.path.dirname(subdir)).replace("\\","/")+".png")



brand_dir = cwd+"\\brand logos"

for subdir, dirs, files in os.walk(brand_dir):
	for file in files:
		shutil.copyfile(subdir+"\\"+file,to_dir+file)



