import os
import json


cwd = os.getcwd()

imagesdir = cwd+"\products"

ul_flag = False
li_flag = False




# limitation: Only for one depth file under each brand

f = open("navigation.html", "w")

number_of_files = {}

for subdir, dirs, files in os.walk(imagesdir):

	if(os.path.relpath(os.path.dirname(subdir),imagesdir) == "."):
		count = 0
		for subdir2, dirs2, files2 in os.walk(subdir):
			count+=len(files2)

		number_of_files[os.path.relpath(subdir,imagesdir)]=count




for subdir, dirs, files in os.walk(imagesdir):

	if(os.path.relpath(os.path.dirname(subdir),imagesdir) == "."):

		if(li_flag):
			f.write("\n\n</ul>\n</li>")

		f.write("\n\n<!-- ==========="+os.path.relpath(subdir,os.path.dirname(subdir))+"============= -->")
		f.write("\n\n\n<li class=\"brand\"><a class=\"menu\" id=\"head\"  data-toggle=\"collapse\" data-target=\"#"+os.path.relpath(subdir,os.path.dirname(subdir))+"\">"+os.path.relpath(subdir,os.path.dirname(subdir))+"<span class=\"badge pull-right\">"+str(number_of_files[os.path.relpath(subdir,os.path.dirname(subdir))])+"</span></a>\n\n<ul id=\""+os.path.relpath(subdir,os.path.dirname(subdir))+"\" class=\"collapse\">\n\n\n")
		li_flag = True




	elif(os.path.relpath(subdir,os.path.dirname(subdir))!="products"):
		 



		if(dirs):
			f.write("\n\n<li><a class=\"menu\" id=\"head\" data-toggle=\"collapse\" data-target=\"#"+os.path.relpath(subdir,os.path.dirname(subdir)).replace(" ", "")+"\"><b>"+os.path.relpath(subdir,os.path.dirname(subdir))+"</b><span class=\"glyphicon glyphicon-option-horizontal pull-right\"></span></a>\n<ul id=\""+os.path.relpath(subdir,os.path.dirname(subdir)).replace(" ", "")+"\" class=\"collapse\">\n")
			ul_flag = True
		else:
			if(os.path.relpath(os.path.dirname(os.path.dirname(subdir)),imagesdir) == "."):
				if(ul_flag):
					f.write("</ul></li>\n\n\n")
					ul_flag = False

			f.write("<li> <a class=\"menu\">"+os.path.relpath(subdir,os.path.dirname(subdir))+"</a></li>\n")




	

f.write("\n\n</ul>\n</li>")



f.close()