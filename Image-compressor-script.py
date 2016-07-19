from PIL import Image
import os,sys
import shutil

cwd = os.getcwd()

imagesdir = cwd+"\original"



for subdir, dirs, files in os.walk(imagesdir):
                dir1 = subdir.split("\original")[1]
                dir1 = cwd + "\products" + dir1
                print dir1
                os.makedirs(dir1)
        
for subdir, dirs, files in os.walk(imagesdir):
                dir1 = subdir.split("\original")[1]
                dir1 = cwd + "\\bigimage" + dir1
                print dir1
                os.makedirs(dir1)

for subdir, dirs, files in os.walk(imagesdir):
        for fil in files:
                impath = subdir + "\\" + fil
                foo = Image.open(impath)
                lentuple = foo.size
                breadth = lentuple[0]
                length = lentuple[1]
                foo = foo.resize((200,(200*length)/breadth),Image.ANTIALIAS)
                
                y = impath.split('\original')
                a = y[0]
                b = y[1]
                newpath = a + "\products"+ b
                print newpath
                foo.save(newpath,optimize=True,quality=75)

for subdir, dirs, files in os.walk(imagesdir):
        for fil in files:
                flag = 0
                impath = subdir + "\\" + fil
                foo = Image.open(impath)
                lentuple = foo.size
                breadth = lentuple[0]   
                length = lentuple[1]

                if (breadth>800):
                        foo = foo.resize((800,(800*length)/breadth),Image.ANTIALIAS)
                        length = (800*length)/breadth
                        breadth = 800
                        flag = 1 
                if (length>800):
                        foo = foo.resize(((800*breadth)/length,800),Image.ANTIALIAS)
                        flag = 1
                print flag
                y = impath.split('\original')
                a = y[0]
                b = y[1]
                newpath = a + "\\bigimage"+ b
                if (flag):

                        print newpath
                        foo.save(newpath,quality=75)
                else:
                        print "old image .."
                        foo.save(newpath,quality=75)
                                   

