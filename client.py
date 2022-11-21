#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
import time
import threading
import queue
import random


ClientMultiSocket = socket.socket()                                     # socket connect
host = '127.0.0.1'  
port = 5000
print(" /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ ")
print("___________________________________________")
print('\033[1m' + "---------Welcome to Math-magicians---------" + '\033[0m')
print("___________________________________________")
print(" \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/")
print("")
print("\n")
print("Rules are pretty simple ~")
print("1. There are a total of 10 questions.")
print("2. Simple arithmetic questions will be displayed on screen.")
#        "  you have to answer within 6 secs.")
# print("3. If you fail to answer in 6 secs, server will move to next question.")
print("3. For every correct answer you get 1 point.")
print("4. For any wrong answer 0.25 points will be deducted!","\n")
print("Are you ready? (Yes/No)")
ClientMultiSocket.connect((host, port))                                 # connecting the client to the server with this host and port
message = input(" -> ")                                                 # take input
print("\n")
ClientMultiSocket.send(message.encode())

def get_input(message, channel):
    response = input(message)
    channel.put(response)

# def input_with_timeout(message, timeout):
#     channel = queue.Queue()
#     message = message + " [{} sec timeout] ".format(timeout)
#     thread = threading.Thread(target=get_input, args=(message, channel))
#     # by setting this as a daemon thread, python won't wait for it to complete
#     thread.daemon = True
#     thread.start()

#     try:
#         response = channel.get(True, timeout)
#         return response
#     except queue.Empty:
#         response=str(None)
#         return response
#     sleep(1)

timeCount = 3
def countdown():
   local_count = timeCount
   while local_count > 0:
      print(local_count,"...")
      time.sleep(1)
      local_count -= 1
   print("~ START ~")

# game starts
start=time.time()                                                       # stores the time at which game starts
if(str(message.lower())=="yes" or str(message.lower())=="y" or str(message.lower())=="yess"):
    name= input(" -> Type your name:")
    ClientMultiSocket.send(name.encode())
    countdown()
    print("\n")
    for i in range(1,11):
        data = ClientMultiSocket.recv(1024).decode()                # receive question
        print('Received from server: Question ' +str(i)+ data)      # show in client's terminal
            
#        if __name__ == "__main__":
#           message = input_with_timeout("-> Answer: ", 5)

        message=input("-> Answer: ")
        ClientMultiSocket.send(message.encode())                    # send answer to the question asked
        Mess=ClientMultiSocket.recv(1024).decode()                  # receive whether answer is correct or not
        print("It is-->",Mess,)                                     # show in client's terminal
        print("_______________________________________________","\n")
            
    Marks = ClientMultiSocket.recv(1024).decode()                   # receive total marks scoredby client
    print("\n")
    print('\033[1m' + 'Your total score: ' + Marks+ '\033[0m')      # show in terminal  
    Endmess=ClientMultiSocket.recv(1024).decode()                   # final message from the server
    print('\033[1m' + Endmess + '\033[0m')                          # show in terminal

else:
    Message = ClientMultiSocket.recv(1024).decode()
    print("Received from server:", Message)

 
end = time.time()                                                       # stores the time at which game ends
tt=end-start                                                            # time taken by client to complete the quiz
print('\033[1m'+"Your time taken: ", round(tt,3), "seconds"+'\033[0m')  # show in client's terminal

ClientMultiSocket.close()                                               # close the connection

