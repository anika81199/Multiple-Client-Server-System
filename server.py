
import socket
import os
from _thread import *
import random
import time

ServerSideSocket = socket.socket()                  # creating a socket connection
host = '127.0.0.1'
port = 5000
ThreadCount=0                                       # keep track of no. of threads, i.e., no. of clients

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

ServerSideSocket.listen(5)                          # no. of clients that the server can serve

def multi_threaded_client(Client,address):
    marks=0
    connection=Client.recv(1024).decode()
    print("Does client wants to play?",connection)
    if(connection.lower()=="yes" or connection.lower()=="yess" or connection.lower()=="y"):
        name=Client.recv(1024).decode()
        print("Name of client:", name,"\n")
        n=10                                        # no.of questions to be asked
        for i in range(1,n+1):
            x=0
            y=0
            x=random.randint(0,9)
            y=random.randint(1,9)    
            j=random.randint(0,3)
            l1=['+','-','*','%']
            c=eval(eval('str(x)+l1[j]+str(y)'))     # actual Answer
            reply = (f' -> {x}{l1[j]}{y}  ')
            print("Question no.",str(i),"for",name,"(",str(address[1]),")",reply)
            print("Actual Ans:",c)                  # show actual ans in server's terminal
            Client.send(reply.encode())             # question Send
            inp = Client.recv(1024).decode()        # receive answer to the question asked
            print("Received from client: ",inp)     # show client's answer in server's terminal
            
#             if(inp=="None"):                        # if client doesn't answer
#                 marks=marks+0
#                 mess=str("Not answered!")
#                 Client.send(mess.encode())
                
            if(int(inp)!=c):                      # if client's answer is wrong
                marks=marks-0.25
                mess=str("Wrong answer👎")
                Client.send(mess.encode())
                
            elif(int(inp)==c):                      # if client's answer is correct
                marks+=1           
                mess=str("⭐ Correct answer ⭐")
                Client.send(mess.encode())
            print("Marks Count :", marks)
            print("________________________________________________","\n")
                      
        M=str(marks)
        Client.send(M.encode())                     # final marks send
        if(marks>5 and marks<9):
            endmess=str("You did great!")
            Client.send(endmess.encode())
        elif(marks>=9):
            endmess=str("Bravo!")
            Client.send(endmess.encode())
        else:
            endmess=str("Better luck next time!")
            Client.send(endmess.encode())
            
        print("Final marks count of",name,"(",str(address[1]),")",": ",M)
        print("------------------------------------------------")
        print("------------------------------------------------")
        
    else:
        mess=str("I hope you make a wise choice next time!")
        Client.send(mess.encode())
        
    Client.close()                                  # connection close
while True:                                         
    Client, address = ServerSideSocket.accept()     # for establishing the connection with multiple clients
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client,address ))
    ThreadCount += 1                                # for every client, new thread is created
    print('Thread Number: ' + str(ThreadCount),"\n")
ServerSideSocket.close()                            # socket close;

