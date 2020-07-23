Loading the Database
To create the dump file mysqldump: TPO -u root -p > TPO.sql
To create an empty database: mysqladmin -u root -p create TPO
To load the dump into database: mysql -u root -p db3 < TPO.sql

python-social-auth is used for google authentication
It can be downloaded using 
pip install python-social-auth

Django Version 1.7 is used, and MySQLdb is used for accessing the SQL database
To start the website
	python manage.py runserver , inside the root directory of the tpoportal

The home screen prompts the user to login using his google email address.
After successfull google authentication
1) The user can login as an admin, if he is an admin
2) The user can login as a student, if he is a student
3) The user can register as a student
4) The user can see the various messages and notifications of the portal
5) The user can access department tpr details and email address for contacting them
6) The user can see the contact details of people added by the admins for assisting the users
7) The user may logout and access the portal through a different email id
After registering as a student, the user can login as a student

After logging in as an admin, the admin can
1) Add a post, to be displayed under messages and notifications tab of the website
2) The admin can register a person for helping and assisting other users
3) The admin can register a company for placements and internships
4) The admin can open willingness of a company for a particular class and department
5) The admin can register a student as a TPR of his department
6) The admin can register other users as administrators

After logging in as a student, the student can 

1) Upload his willingness for a company he is eligible for
2) The student may update his personal details
3) The student may upload/update his resume
4) The student may upload/update his profile picture
5) The student may upload/update his grades
