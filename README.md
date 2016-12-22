# myinstagram
A simple  instagram-like web app

A web app concentrate on server side scalability

### Features:
1.	User account system. Users could sign up new accounts, login and logout.
2.	Photos storage service. Users are able to upload images to server, view them and remove them.
3.	Keyword search service. Users are optional to write descriptions when they upload images, and they could search keywords inside the descriptions afterwards to find out the specific images.
4.	Social network. Users are able to find other users in lobby, and they could choose to follow others so that they could quickly find them in the following list. In addition, users are free to watch each other’s photos.
5.	Email digest service. A user will be notified when someone start to follow him or his following users just upload new images.

### Architecture and implementation
1.	The project is created in Server-Client model.
2.	At server side, feature functions are implemented as services.
3.	The Nginx is used as load balancer.
4.	Gunicorn is used as Python web server.
5.	Two Flask application server replicas are currently deployed.
6.	MongoDB is used as database system.
7.	RabbitMQ is used as asynchronous message queues broker.
8.	Redis is used as cache.


### Screenshots
<img src="https://github.com/freewheel70/myinstagram/blob/master/screenshots/login.png">
<img src="https://github.com/freewheel70/myinstagram/blob/master/screenshots/profile.png">
<img src="https://github.com/freewheel70/myinstagram/blob/master/screenshots/search.png">
<img src="https://github.com/freewheel70/myinstagram/blob/master/screenshots/lobby.png">