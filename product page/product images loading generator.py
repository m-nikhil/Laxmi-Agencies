file = open("product images loading.txt","w")

#declare a root directory in the js, before using

file.write("$('.image').css({\"background\": \"url(spinner.gif) center no-repeat #fff\"});")

string = """ 
                
                if(images[{b}])
                {
                $(\"#image{a}\").hide();
                var image_src = root+images[{b}];
                downloadingImage{a} = new Image();
                downloadingImage{a}.onload = function(){
                       $(\"#image{a}\").parent().parent().css({\"background\": \"url() no-repeat\"});
                       $(\"#image{a}\").attr(\"src\",downloadingImage{a}.src);
                       $(\"#image{a}\").show();
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
