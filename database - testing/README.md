
`This is displaying image stored manually in the database.`

#How to setup the database?

image1.sql is the database file. Export this file to your mysql.


For xampp, start mysql and apache services. And then go to localhost/phpmyadmin. There, in the toolbar click the export option. Select your file and click go. Ensure the format is sql.  

I know only for xammp. This is same for wampp and lampp.

#How to run?

* Install python.
* Then install the flask package, using the command
	`pip install flask`
* place these files in a folder.
* go to the folder and run this command 
	`python routes.py`
* open your browser, type http://127.0.0.1:5000/ in the address bar.
* Hope you see the images...