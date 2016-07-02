# Laxmi-Agencies

Laxmi-Agencies is an official website to showcase the sales items.

This site is developed using python flask and bootstrap framworks.

# Contibution

* Always push a commit to the development branch (not master).
* The commit must be a new branch.
* The name of commit and branch is same.
* The name should be relevant to the issue being solved and prefixed with it's ID (eg. 32 update ui).
* If you find no issues relevant to your work, do open a new issue.

You are welcome to open issues to pose questions for clarification, discussion and any related stuffs.

#Deployment 

* we are to deploy in the `openshift`.

For deployment testing, create a "hello world" python flask and then configure the server and download the dependencies to host "hello world" site.

`This takes place in 'hosting-test' branch.`

#Resources

* http://www.tutorialspoint.com/flask
* https://www.ntu.edu.sg/home/ehchua/programming/webprogramming/Python3_Flask.html
* http://getbootstrap.com/
* https://openoox.com/folder/shopping-themes

# Development

basic file structure:
``` ruby
.
+-- app
|   +-- static
|   |   +-- css
|   |   +-- images
|   |   +-- js
|   |   +-- jquey
|   +-- templates
|   |   + home.html
|   +-- routes.py
+-- resources
+-- .gitignore
+-- README.md
```
* app is the beginning of the flask application.
* static file contains the css,images,scripts.
* templates contain all the html files
* routes.py is the basic route for the application
* resources contain the images/pics and description of the layout

`NOTE: THis is just the basic hierarchy. Needs to to updated depend on the requirement.`

NOTICE: If there's any bug in this project, do file a issue with a description stating the problem and the location.



