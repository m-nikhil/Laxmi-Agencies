file = open("product images loading.txt","w")


file.write("var images = database[row][column];")

string = """ 
                
                if(images[{b}])
                {
                var image_src = \"./products/\"+images[{b}];
                downloadingImage{a} = new Image();
                downloadingImage{a}.onload = function(){
                       $(\"#image{a}\").attr(\"src\",downloadingImage{a}.src);
                };             
                 downloadingImage{a}.src = image_src;
                  $images_parts = images[{b}].split(\"/\");
                  $length = $images_parts.length;
                  $(\"#product{a}\").text(($images_parts[$length-1]).substring(0,($images_parts[$length-1]).lastIndexOf(\".\")));
                }
                else
                {
                  $(\"#image{a}\").attr(\"src\",\"./products/empty.png\");
                   $(\"#product{a}\").text(\"\");
                } 



          """

for i in range(1,10):
  file.write(string.replace("{a}",str(i)).replace("{b}",str(i-1)))
