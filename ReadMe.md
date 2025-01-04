
# Multiple Client-Server System

A system designed in such a way that the server handles multiple clients simultaneously.




## About

Client-Server system is basically the backbone of web browsing. We come across different types of client-server connections in our day-to-day life. The simplest example would be Google Search, it basically connects a client (i.e., user) to a server (i.e., Google Search) and provides the client with the information it needs.

Herein, I have designed a quiz-game which is essentially a basic client-server system, where connection is established when client approaches a server. As soon as the connection is established, the server throws basic arithmetic problems on the client, and based on the answers, marks will be awarded to the client.


![pic2](https://github.com/anika81199/Multiple-Client-Server-System/blob/main/cl.jpg)

## Software used

The code has been written in Python on Jupyter Notebook.
## Background

Before moving forward with the code, we need to look at certain important concepts/functions used in the program.

### 1. Socket Programming [concept]

Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The most common type of socket applications are client-server applications, where one side acts as the server and waits for connections from clients. The server forms the listener socket while the client reaches out to the server. 

Socket is the endpoint of a bidirectional communication channel between server and client. The socket API are used to send messages across a network. They provide a form of inter-process communication (IPC). The network can be a logical, local network to the computer, or one that’s physically connected to an external network, with its own connections to other networks. The obvious example is the Internet, which you connect to via your ISP.



Socket programming is started by importing the socket library and making a simple socket. 

-> `import socket`

### 2. `socket_name=socket.socket(socket.AF_INET,socket.SOCK_STREAM)`

This command is used to create a socket object. There are two parameters passed in it. The first parameter is `AF_INET` and the second one is `SOCK_STREAM`. 
`AF_INET` refers to the address-family ipv4. The `SOCK_STREAM` means connection-oriented TCP protocol.

>
    Why should you use TCP? 
    
    * Is reliable: Packets dropped in the network are detected and retransmitted by the sender.
    * Has in-order data delivery: Data is read by your application in the order it was written by the sender.
    
Networks are a best-effort delivery system. There’s no guarantee that your data will reach its destination or that you’ll receive what’s been sent to you. Network devices, such as routers and switches, have finite bandwidth available and come with their own inherent system limitations. They have CPUs, memory, buses, and interface packet buffers, just like your clients and servers. TCP relieves you from having to worry about packet loss, out-of-order data arrival, and other pitfalls that invariably happen when you’re communicating across a network.

![pic1](https://github.com/anika81199/Multiple-Client-Server-System/blob/main/Screenshot%20(98).png)

The left-hand column represents the server. On the right-hand side is the client.

We have used this command seperately for *server side* socket and *client side* socket. For example,

-> `server_name=socket.socket()`

### 3. `socket.gethostbyname(hostName)`

It is a built-in function which returns the IP address of the host.
When the parameter `hostname` is omitted, hostname defaults to localhost.

### 4. `port` and `host`
The PORT and HOST are defined to establish communication with clients.

The IP address `127.0.0.1` is the standard IPv4 address for the loopback interface, so only processes on the host will be able to connect to the server. If you pass an empty string, the server will accept connections on all available IPv4 interfaces.

### 5. `socket_name.bind((host, port))`

This method connects the HOST and PORT to the socket server; this is the process that ensures server is bound to a specific IP and port so that it can listen to incoming client's requests on that IP and port.

### 6. `server_name.listen()`
A server has a `listen()` method which puts the server into listening mode. This allows the server to listen to incoming connections.The .listen() method has a backlog parameter. It specifies the number of unaccepted connections, that the system will allow before refusing new connections.

### 7. `server_name.accept()`
When a client connects, the server calls `.accept()` to accept, or complete, the connection. The `.accept()` method blocks execution and waits for an incoming connection. When a client connects, it returns a new socket object representing the connection and a tuple holding the address of the client. The tuple will contain (host, port) for IPv4 connections. 

### 8. `server_name.connect()`
The client calls `.connect()` to establish a connection to the server and initiate the three-way handshake. The handshake step is important because it ensures that each side of the connection is reachable in the network, in other words that the client can reach the server and vice-versa. It may be that only one host, client, or server can reach the other.

### 9. `recv()`
receives message sent through TCP.

### 10. `send()`
sends message sent through TCP.

### 11. `decode()`
decodes the message using the codec.

### 12. Multithreading [concept]
Threading is an ultimate elixir to make the program run swiftly. Multithreading is defined as the ability of a processor to execute multiple threads concurrently. 

In our program, we created a mechanism in which multiple clients can connect to the server, and every client is given an associated thread for managing client requests individually. The `start_new_thread` function handles the connection; it establishes a new thread for every client to perform server connection duty specifically.

### 13. `multi_threaded_client()`
This is a function that we designed to handle multiple clients together.
It connects every client from various addresses provided by the server simultaneously.

Within the `multi_threaded_client` function, the `connection.recv(2048)` method is separately getting the data from every client and returning the server response to a specific client.


## User Manual

In order to execute this program, you need to follow the below steps sequentially :

1. Download the **Server.py** and **Client.py** file in your local machine.
2. Open both the programs in any local IDE, preferrably Jupyter Notebook, Spyder, etc.
>  
    The program is designed to run on the same machine, so host and port addresses will be modified accordingly.
3. Run the Server.py script in Python application.
4. Run the Client.py script in Python application.
5. Read the rules of the game in the client terminal.
7. Enter your response YES or NO and press Enter key. 
>   
    Input= YES, the game will start.
    Input= NO, the game does not starts.

9.  Enter your name in the client terminal.
10. Input your answer for every question.
>
    Your marks will be displayed on the client terminal at the end of the game.


## Itinerary of code

Initially, I learnt to establish the connection between the *server* and *client* using **socket programming**. I made a simple chatbot in which the server used to send the exact same message that the client had sent. In the next step, I made a program for basic arithmetic-quiz in which the client sent a request for connection and then the server sent a total of 10 questions one after the other to the client and kept track of the marks at every correct or wrong answer. For every correct answer, the client got +1 mark and for every wrong answer, 0.25 marks was deducted. Then I modified this program for multiple clients using the concept of **multithreading**. The server opened a new thread for each client and kept track of the marks of each client. It closes the program after sending total marks to each of the client.

## Program Flow

### Server-side

* First of all, `socket` and `random` is imported, which is necessary.
* Then a socket object `ServerSideSocket` is created using `socket.socket()`.
* Using `socket.gethostbyname(hostName)` the IPv4 address of the machine on which the server program is running is accessed and then stored in `host`. Also, a particular `port` number in the machine is reserved, for e.g., `5000`.
* Then using `ServerSideSocket.bind((host,port))` the HOST and PORT are connected to the socket server.
* After that, `listen()` command enables the server to listen to incoming connections from the clients. Herein, we have restricted our server to listen to at *max 3 clients*.
* After that, inside the infinite `while` loop, `.accept()` provides the client socket object `ServerSideSocket` with the address of the client.
>
    The address of the connected client is shown in the server terminal.
* The `ThreadCount` is initialized with 0, and with the increment in no. of clients, the value of `ThreadCount` keeps incrementing by 1. 
>
    For every client sending a connection request to the server, a new thread is created.
    We have limited our server to entertain only 3 clients at a time.
* Then `start_new_thread()` function is created which starts a thread for the current connected client.
* It passes client's address as argument in the `multi_threaded_client` function to start the game.
* The server decodes the `message` received by the client by using `Client.recv(1024).decode()` method, and starts the game by checking an `if-else` condition if the message decoded is `yes`.
* `Client.recv(1024).decode()` command is used to get the name of the player from client's terminal to the server's terminal and stored in a variable `name`.
*  A `for` loop begins with the range 10 which executes the following instructions.
    * The values of `x` and `y` variables are initialized by 0.
    * The values of `x` and `y` are randomly selected to be integers between 0 to 9 using `random.randint(0,9)`.
    * A list `l1` is created which stores all the arithmetic operations as string.
    * Another variable `j` takes values between 0 to 3 by using `random.randint(0,3)`
    * `(f' -> {x}{l1[j]}{y}  ')` is used to generate an arithmetic problem in the form of `str` and stored in a variable called `reply`.
    * Variable `c` stores the evaluated value of this expression using `eval()`.
    * Question is sent to the client by `Client.send(reply.encode())`.
    * Answer is received by using `Client.recv(1024).decode()` and stored in a variable `inp`.
    * `marks` is initialized by 0.
    * Again `if-else` condition is used to check whether the answer given by the client is correct or not and respectively increment(+1) or decrement(-0.25) in `marks` is done and certain `message` is sent to the client's terminal.
* Finally at the end, total marks is sent to the client's terminal using `Client.send(M.encode())`.
* According to the marks obtained certain message is printed on the client's terminal.
* `ServerSideSocket.close()`is used to close the connection.
>
    These steps are repeated over and over again for multiple clients.

### Client-side

* `socket.socket()` used to create a socket object for client, namely, `ClientMultiSocket`.
* Using `socket.gethostbyname(hostName)` the IPv4 address of the machine on which the client program is running (assuming they both are running on the same machine) is accessed, and stored in `host`. Also, reserved a particular `port` number in the machine, for e.g., `5000`.
* Then using `ClientMultiSocket.connect((host,port))` the HOST and PORT are connected to the server socket.
* Certain printing statements are implemented to make the program user-friendly.
* Client's response to the question,**"Are you ready to play?"** gets stored in a variable `message` and sent to the server via `ClientMultiSocket.send(message.encode())`.
* `ClientMultiSocket.send(name.encode())` sends the name of the client to the server's terminal.
* `countdown()` function gives the countdown from 3 in order to begin the game. It is called when the `message==Yes`.
* `start=time.time()` stores the time at which the game starts.
* A `for` loop begins with the range 10 which executes the following instructions.
    * `ClientMultiSocket.recv(1024).decode()` is used to receive the questions from the server.
    * `message=input("-> Answer: ")` is used to take input from the client.
    * This answer is sent to the client's terminal via `ClientMultiSocket.send(message.encode())`.
    * Based on the answer a message is sent by the server and displayed on client's terminal.
* `end = time.time()` stores the time at which game ends.
* `tt` stores the total time taken by the player to finish the game.
* Final score and time taken is displayed on the client's terminal.
* `ClientMultiSocket.close()` is used to close the connection.


## Usage of this model

A lot of real life applications uses the client-server model. Examples include email, network printing, and the World Wide Web. When a bank customer accesses online banking services with a web browser (the client), the client initiates a request to the bank's web server. The customer's login credentials may be stored in a database, and the web server accesses the database server as a client. An application server interprets the returned data by applying the bank's business logic and provides the output to the webserver. Finally, the web server returns the result to the client web browser for display.

Hence, the usage of this model is everywhere in our daily life!
