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
7 remove a message
----------------
DELETE /messages/$id/


Suggestions
=============
there is many ways to change this to a realtime project, either to use Tornado or Gevent or have a Nodejs server that uses Socket.io.
our advice is to go with the Nodejs Socket.io and only use that for broadcasting the messages and receiving the messages.
then the Node.js server should send async requests to the django in case the service went down or interupted.
it is also adviced to persist those chats channels content in a cache storage solution(like redis).
NOTE : having javascript loading every timespan is a very bad way of doing it, since it will create requests that will just load the server.
