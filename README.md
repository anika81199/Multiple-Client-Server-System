
# Multiple Client-Server System

A system designed in a way such that the server handles multiple clients at the same time.




## About

Client-Server system is basically the backbone of web browsing. We come across different types of client-server connections in our day-to-day life. The simplest example would be Google Search, it basically connects a client (i.e., user) to a server (i.e., Google Search) and provides the client with the information it needs.

Herein, we have designed a quiz-game which is essentially a basic client-server system, where connection is established when client approaches a server. As soon as the connection is established, the server throws basic arithmetic problems on the client, and based on the answers, marks will be awarded to the client.
## Background

Before moving forward with the code, we need to look at certain important functions used in the program.

### 1. Socket Programming

Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server. 
## User Manual

In order to execute this program, you need to follow the below steps in order :

1. Download the SERVER.ipynb and Client.ipynb file in your local machine.
2. Open both the programs in any local IDE, preferrably Jupyter Notebook, Spyder, etc.
3. The program is designed to run on the same machine, so host and port address will be modified accordingly.
4. 
