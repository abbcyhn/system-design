# Web Architecture

## Educative Questions

* Where does the user interface component of a web application render?
	* It can render on both the client and the server.

* What is the other name for the Fat client?
	* Thick client

* When should we implement a thick client for our application?

	* When we need to minimize the network latency.
	* When we need to reduce the bandwidth consumption in the client server communication, for a smooth user experience.

* Which protocol do the web browsers and the servers use to communicate with each other?
	* HTTP Protocol

* Who always initiates the communication in a client server, request-response model?
	* Client

* Why should we implement a REST API in our application?
	* To decouple the backend server code from multiple client implementations for a cleaner and a more flexible architecture.
	* To create a gateway, a single-entry point into the system that would help the system take care of the authorization, authentication, sanitizing the input data and other necessary tasks before it provides access to the application resources.

* Why should the backend server and its clients be implemented separately in different codebases?
	* This makes introducing new clients possible without affecting the backend code.
	* Code changes made in any of the clients have no impact on the backend code. The architecture of the application is loosely coupled.

* When do we need to implement the HTTP PUSH mechanism in our application?
	* When the application is a real-time application like an online multiplayer game, a LIVE sports app.
	* When we need to reduce the number of client requests hitting the server every now and then, checking for new information.

* Why does every browser request have a TTL Time To Live?
	* Because open connections between the client and the server are resource intensive and there is a limit to the number of open connections a server can manage.

* When do we need persistent connections in our application?
	* When we are certain that the response time of the server will be more than the TTL set by the browser.
	* When the frequency of request and response between the client and the server is high.

* Which HTTP PUSH based technology suits best for implementing a streaming media application?
	* Streaming Over HTTP

* Which technique suits best for implementing a browser-based multiplayer game?
	* Web Sockets

* When should we render the user interface on the server?
	* When the content to be rendered is static in nature.

## Person1 Questions

* Why is HTTP called a stateless protocol?
	* Because each request is executed independently, without any knowledge of the requests that were executed before it, which means once the transaction ends the connection between the browser and the server is also lost.

* What is AJAX and how it works? 
	* Ajax stands for Asynchronous JavaScript And XML.
	* With Ajax, web applications can send and retrieve data from a server asynchronously without interfering with the display and behaviour of the existing page.
	* It uses an XMLHttpRequest object to send the requests, this object is built in the browser and uses JavaScript to update the HTML DOM

* Which HTTP mechanims do you know? Give technology example.
	* HTTP PULL - 1) sending GET request manually; 2) AJAX Polling
	* HTTP PUSH - 1) Web Sockets; 2) AJAX Long Polling; 3) Server-Sent Events & HTML5 Event-Source API; 5) Stream over HTTP

* What are heartbeat interceptors?
	* The connection between the client and the server stays open with the help of Heartbeat Interceptors.
	* These are just blank request responses between the client and the server to prevent the browser from killing the connection.
	* This is resource-intensive

* Web server vs Application Server? Give technology examples.
	* https://www.nginx.com/resources/glossary/application-server-vs-web-server/
	* https://www.educative.io/answers/web-server-vs-application-server
	* Examples: 
		* IIS - both webserver and application server
		* Apache HTTP Server - web server (with plugins can be application server)
		* Apache Tomcat - both webserver and application server
		* NGINX - web server that can be used as a reverse proxy, load balancer and HTTP cache

* What is batch job server? Give technology examples.
	* It is a type of server or software system that manages and executes batch jobs. A batch job refers to a collection of tasks or commands that are grouped together and scheduled to be executed without any user interaction.
	* Examples:
		* Apache Airflow - an open-source platform for orchestrating and managing workflows, including batch jobs.
		* Jenkins -  is an open-source automation server primarily used for continuous integration and delivery (CI/CD) pipelines. However, it can also be used to schedule and execute batch jobs.
		* IBM Job Entry Sybsytems (EJS) - provides a batch job processing environment where users can submit, manage, and monitor batch jobsx