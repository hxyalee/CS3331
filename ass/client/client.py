#!/usr/bin/env python3

import sys
from socket import *
from time import sleep
import select
import os

if (len(sys.argv) != 3):
    print("Usage: ./Client.py {server_IP} {server_port}")
    exit()

server_IP = str(sys.argv[1])
server_port = int(sys.argv[2])

# Create client's socket
# AF_NET -- underlying network is IPv4
# SOCK_STREAM -- TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)
# Establish TCP connection between client and server
clientSocket.connect((server_IP, server_port))
isLoggedIn = False

while not isLoggedIn:
    print("Please enter a username: ")
    username = sys.stdin.readline().rstrip()
    payload = f"USERNAME {username}"
    clientSocket.send(payload.encode("utf-8"))
    response = clientSocket.recv(1024)
    response_code = response.decode('utf-8')
    if(response_code == "PASSWORD"):
        print("Please enter your password: ")
        password = sys.stdin.readline().rstrip()
        payload = f'PASSWORD {username} {password}'.encode("utf-8")
        clientSocket.send(payload)
        response = clientSocket.recv(1024)
        response_code = response.decode('utf-8')
        if(response_code == 'LOGIN'):
            isLoggedIn = True
            break
        elif(response_code == "INVALIDPASSWORD"):
            print('Wrong password. Please try again')
    elif(response_code == 'NEWPASSWORD'):
        print("Please enter your new password: ")

        password = sys.stdin.readline().rstrip()
        payload = f"PASSWORD {username} {password}".encode("utf-8")

        clientSocket.send(payload)
        response = clientSocket.recv(1024)
        response_code = response.decode('utf-8')
        if(response_code == 'LOGIN'):
            isLoggedIn = True
            break
        elif(response_code == "INVALIDPASSWORD"):
            print('Weak password. Please make sure your password has upper case characters, lowercase characters, digits, and special characters')
    elif response_code == 'LOGGEDIN':
        print(
            f'{username} is already logged in! Please try again with another username')
print("Welcome to the forum")
while True:
    print("\nPlease enter one of the following commands: CRT, MSG, DLT, EDT, LST, RDT, UPD, DWN, RMV, XIT, SHT:\n")
    (input_ready, output_ready, exception) = select.select(
        [sys.stdin, clientSocket], [], [])
    for i in input_ready:
        if i == sys.stdin:
            cmd = sys.stdin.readline().rstrip()
            cmdList = cmd.split(' ')
            if(cmdList[0] == "CRT"):
                if(len(cmdList) != 2):
                    print('Threadname can only be one word')
                    continue

                payload = f'CRT {username} {cmdList[1]}'.encode('utf-8')
                clientSocket.send(payload)
                response = clientSocket.recv(1024)
                response = response.decode('utf-8')
                if(response == 'EXISTINGTHREAD'):
                    print(f'Thread with title {cmdList[1]} already exists.')
                elif(response == "SUCCESS"):
                    print(
                        f'Thread with title {cmdList[1]} created successfully.')

            if(cmdList[0] == 'MSG'):
                if(len(cmdList) < 3):
                    print("Please enter your message")
                    continue
                payload = f'MSG {username} {cmdList[1]} {" ".join(cmdList[2:])}'.encode(
                    'utf-8')
                clientSocket.send(payload)
                response = clientSocket.recv(1024)
                response = response.decode('utf-8')
                if(response == 'NOTHREAD'):
                    print(f"Thread with title {cmdList[1]} does not exist")
                elif(response == 'SUCCESS'):
                    print(
                        f"Message written to {cmdList[1]} sent successfullly")
            if(cmdList[0] == 'DLT'):
                if(len(cmdList) != 3):
                    print(
                        'Invalid input. Usage: DLT {threadtitle} {messagenumber}')
                    continue
                payload = f'DLT {username} {cmdList[1]} {cmdList[2]}'.encode(
                    'utf-8')
                clientSocket.send(payload)
                response = clientSocket.recv(1024)
                response = response.decode('utf-8')
                if(response == 'NOTHREAD'):
                    print(f"Thread with title {cmdList[1]} does not exist")
                elif(response == 'INVALIDMSGNO'):
                    print(
                        f"Message with message number {cmdList[2]} does not exist")
                elif(response == "INVALIDCREDENTIALS"):
                    print(f"You cannot delete this message because you did not send it")
                elif(response == 'SUCCESS'):
                    print(f"Message deleted successfully")
            if(cmdList[0] == 'EDT'):
                if(len(cmdList) < 4):
                    print(
                        'Invalid input. Usage: EDT {threadtitle} {messagenumber} {message}')
                    continue
                payload = f'EDT {username} {cmdList[1]} {cmdList[2]} {" ".join(cmdList[3:])}'.encode(
                    'utf-8')
                clientSocket.send(payload)
                response = clientSocket.recv(1024)
                response = response.decode('utf-8')
                if(response == 'NOTHREAD'):
                    print(f"Thread with title {cmdList[1]} does not exist")
                elif(response == 'INVALIDMSGNO'):
                    print(
                        f"Message with message number {cmdList[2]} does not exist")
                elif(response == "INVALIDCREDENTIALS"):
                    print(f"You cannot edit this message because you did not send it")
                elif(response == 'SUCCESS'):
                    print(f"Message edited successfully")
            if(cmdList[0] == "LST"):
                if(len(cmdList) != 1):
                    print("Invalid input. Usage: LST")
                    continue
                payload = f"LST {username}".encode('utf-8')
                clientSocket.send(payload)
                response = clientSocket.recv(1024)
                response = response.decode('utf-8')
                if response == "NOTHREAD":
                    print(
                        'There are no threads at the moment. Please create one using the CRT command')
                elif(response.split(' ')[0] == "SUCCESS"):
                    threads = response.split(' ')[1:]
                    for thread in threads:
                        print(thread)
            if(cmdList[0] == 'RMV'):
                if(len(cmdList) != 2):
                    print("Usage: RMV {threadname}")
                    continue
                threadtitle = cmdList[1]
                payload = f"RMV {username} {threadtitle}".encode('utf-8')
                clientSocket.send(payload)
                response = clientSocket.recv(1024)
                response = response.decode('utf-8')
                if response == "NOTHREAD":
                    print(f'There is no thread named {threadtitle}')
                elif response == 'INVALIDPERMISSIONS':
                    print(
                        f'You cannot delete thread {threadtitle} because you did not create it')
                elif(response == "SUCCESS"):
                    print(f"Thread {threadtitle} deleted successfully!")

            if(cmdList[0] == "XIT"):
                payload = f"XIT {username}".encode('utf-8')
                clientSocket.send(payload)
                response = clientSocket.recv(1024)
                response = response.decode('utf-8')
                if(response == 'SUCCESS'):
                    print(f"Good bye {username}!")
                    clientSocket.close()
                    exit()
                else:
                    print('Something went wrong! Please try again')
            if(cmdList[0] == 'SHT'):
                if(len(cmdList) != 2):
                    print("Usage: SHT {admin_password}")
                    continue
                adminPass = cmdList[1]
                payload = f"SHT {username} {adminPass}".encode('utf-8')
                clientSocket.send(payload)
                response = clientSocket.recv(1024)
                response = response.decode('utf-8').split(' ')
                if(response[0] == 'SHUTDOWN'):
                    print(f"Shutting server down...")
                    print(f"Good bye {username}!")
                    os._exit(1)
                elif(response == 'INVALIDCREDENTIALS'):
                    print('Wrong admin password! Please try again')
                else:
                    print('Something went wrong! Please try again')

            if cmdList[0] == 'RDT':
                if len(cmdList) != 2:
                    print("Usage: RDT {threadtitle}")
                    continue
                threadtitle = cmdList[1]
                payload = f"RDT {username} {threadtitle}".encode('utf-8')
                clientSocket.send(payload)
                response = clientSocket.recv(1024).decode('utf-8')
                if(response == 'NOTHREAD'):
                    print(f"Thread with title {cmdList[1]} does not exist")
                elif(response == "THREADEMPTY"):
                    print(f"Thread with title {threadtitle} is empty")
                else:
                    res = response.split('#')
                    for msg in res:
                        if(msg):
                            print(msg)

            if(cmdList[0] == 'UPD'):
                if(len(cmdList) != 3):
                    print("Usage: UPD {threadtitle} {filename}")
                    continue
                threadtitle = cmdList[1]
                filename = cmdList[2]
                payload = f"UPD {username} {threadtitle} {filename}".encode(
                    'utf-8')
                clientSocket.send(payload)
                response = clientSocket.recv(1024)
                response = response.decode('utf-8')
                if(response == 'NOTHREAD'):
                    print(f"Thread with title {cmdList[1]} does not exist")
                elif(response == 'SENDFILE'):
                    try:
                        with open(filename, 'rb') as f:
                            payload = f"SEND".encode('utf-8')
                            clientSocket.send(payload)
                            l = f.read(1024)
                            while(l):
                                clientSocket.send(l)
                                l = f.read(1024)
                            clientSocket.shutdown(SHUT_WR)
                            response = clientSocket.recv(1024)
                            response = response.decode('utf-8')
                            if(response == 'SUCCESS'):
                                print(
                                    f'Successfully uploaded the file {filename} to thread {threadtitle}')
                                # IFFY ABOUT THIS CHECK
                                clientSocket = socket(AF_INET, SOCK_STREAM)
                                clientSocket.connect((server_IP, server_port))

                    except Exception:
                        print(
                            'Please make sure the file exists and you have the correct permissions')
                        payload = f"VOID".encode('utf-8')
                        clientSocket.send(payload)
            if cmdList[0] == "DWN":
                if(len(cmdList) != 3):
                    print("Usage: DWN {threadtitle} {filename}")
                    continue
                threadtitle = cmdList[1]
                filename = cmdList[2]
                payload = f"DWN {username} {threadtitle} {filename}".encode(
                    'utf-8')
                clientSocket.send(payload)
                response = clientSocket.recv(1024)
                response = response.decode('utf-8')
                if(response == 'NOTHREAD'):
                    print(f"Thread with title {cmdList[1]} does not exist")
                elif(response == 'NOFILEINTHREAD'):
                    print(
                        f'File {filename} does not exist in thread {threadtitle}')
                elif(response == 'SEND'):
                    with open(filename, 'wb+') as f:
                        data = clientSocket.recv(1024)
                        while(data):
                            f.write(data)
                            if(b"#FILESENT" in data):
                                break
                            data = clientSocket.recv(1024)

                    clientSocket = socket(AF_INET, SOCK_STREAM)
                    clientSocket.connect((server_IP, server_port))
                    print(f"{filename} downloaded successfully!")

                else:
                    print('Something went wrong. Please try again later')

        elif i == clientSocket:
            resposne = clientSocket.recv(1024).decode('utf-8')
            response_code = resposne.split(' ')
            if response_code[0] == "SHUTDOWN":
                print(f"{response_code[1]} issed a SHT command")
                print("Server shutting down")
                clientSocket.close()
                exit()
clientSocket.close()
