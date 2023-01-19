import csv
import socket
import time

host = "localhost"
port = 9999
address_tuple = (host, port)


socket_family = socket.AF_INET 


socket_type = socket.SOCK_DGRAM 


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 


input_file = open("Icd.csv", "r")

reader = csv.reader(delimiter=",")

for row in reader:
    
    State, Sex, Race_Ethnicity, Age_Group, First_Year, Last_Year, Rank, Cause_of_Death, Deaths = row


    fstring_message = f"[{State}, {Race_Ethnicity}, {Age_Group}, {First_Year}, {Last_Year}, {Rank}, {Cause_of_Death}, {Deaths}]"
    
    # prepare a binary (1s and 0s) message to stream
    MESSAGE = fstring_message.encode()

    # use the socket sendto() method to send the message
    sock.sendto(MESSAGE, address_tuple)
    print (f"Sent: {MESSAGE} on port {port}.")

    # sleep for a few seconds
    time.sleep(3)
