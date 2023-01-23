import csv
import socket
import time

host = "localhost"
port = 9999
address_tuple = (host, port)


socket_family = socket.AF_INET 


socket_type = socket.SOCK_DGRAM 


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 


input_file = open("lcd.csv", "r")

# use the built0in sorted() function to get them in chronological order
reversed = sorted(input_file)

# create a csv reader for our comma delimited data
reader = csv.reader(reversed, delimiter=",")

reader = csv.reader(sorted(reversed),delimiter=",")

for row in reader:
    
    State, Sex, Race_Ethnicity, Age_Group, First_Year, Last_Year, Rank, Cause_of_Death, Deaths = row


    fstring_message = f"[{State}, {Race_Ethnicity}, {Age_Group}, {First_Year}, {Last_Year}, {Rank}, {Cause_of_Death}, {Deaths}]"
    

    MESSAGE = fstring_message.encode()


    sock.sendto(MESSAGE, address_tuple)
    print (f"Sent: {MESSAGE} on port {port}.")

    # sleep for a few seconds
    time.sleep(1)
