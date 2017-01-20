# chatproject(not realtime)

1 install required libraries
-----------------------------
>pip install -r requirements.txt

2 make migrations in case missing
----------------------------------
>./manage.py makemigrations

>./manage.py migrate

3 create super user
-------------------
>./manage.py createsuperuser

4 start the server and login
-----------------------------
>./manage.py runserver

login at:
http://127.0.0.1:8000/admin/login/?next=/messages/

5 get all the messages
-------------------
GET /messages/
6 add a new message
---------------
POST /messages/

request.body(json):

{"body":"your message here",
"receiver_email":"receivers email here"}
7 add a new genre:
-----------------
8 remove a message
----------------
DELETE /messages/$id/
