#!/usr/bin/env python3
import sys
from socket import *
import os
import time
import threading
from select import *


def get_credentials():
    '''
            Return a dictionary of credentials from the
            credentials.txt file
            Credentials are in form {username: password}
    '''
    if (not os.path.exists("credentials.txt")):
        print("Please make sure credentials.txt exists with the right permissions in the current directory")
        exit()
    credentials = {}
    try:
        f = open("credentials.txt", "r")
        line = f.readline()
        while line:
            tmp = line.split(' ')
            credentials[tmp[0]] = tmp[1].rstrip()
            line = f.readline()
        f.close()
        return credentials

    except Exception:
        print("Please make sure credentials.txt has the right permissions")
        exit()


def new_credentials(username, password):
    if (not os.path.exists("credentials.txt")):
        print("Please make sure credentials.txt exists with the right permissions in the current directory")
    try:
        f = open("credentials.txt", "a")
        f.write(f"\n{username} {password}")
        f.close()
    except Exception:
        print("Please make sure credentials.txt has the right permissions")
        exit()


def isRegistered(username):
    credentials = get_credentials()
    if(username in credentials.keys()):
        return True
    return False


def isValidLogin(username, password):
    credentials = get_credentials()
    if(credentials[username] == password):
        return True
    return False


def isValidPassword(password):
    specialChars = '~!@#$%^&*_-+=|\(){}[]:\'\"<>,.?/'
    return (any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c in specialChars for c in password))


def fileExist(name):
    return os.path.exists(name)


def threadEmpty(name):
    fp = open(name, 'r')
    line = fp.readlines()
    return len(line) == 1


def createThread(username, name):
    fp = open(name, 'w')
    fp.write(username)
    fp.close()


def getMessageNumber(name):
    with open(name, 'r') as f:
        lines = f.readlines()
        res = 1
        for line in lines:
            try:
                res = int(line[0]) + 1
            except ValueError:
                continue
        return res


def writeMessage(filename, msg):
    with open(filename, "a") as f:
        f.write(f"\n{msg}")


def messageExists(filename, num):
    with open(filename, 'r') as f:
        line = f.readline()
        while(line):
            line = f.readline()
            lst = line.split(' ')
            if(lst[0] == num):
                return True
    return False


def messageModifiable(filename, num, username):
    with open(filename, 'r') as f:
        line = f.readline()
        while(line):
            line = f.readline()
            lst = line.split(' ')
            if(lst[0] == num and lst[1].split(':')[0] == username):
                return True

    return False


def deleteMessage(filename, num):
    with open(filename, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if(line.strip('\n').split(' ')[0] == num):
            lines.remove(line)
            break
    with open(filename, 'w') as f:
        count = 0
        last = lines[-1]
        for line in lines:
            if count == 0:
                f.write(line)
            elif last == line:
                tmp = line.strip('\n')
                f.write(f'{count} {" ".join(tmp.split(" ")[1:])}')
            else:
                f.write(f'{count} {" ".join(line.split(" ")[1:])}')

            count += 1


def editMessage(filename, num, username, msg):
    with open(filename, 'r') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if(lines[i].strip('\n').split(' ')[0] == num):
            lines[i] = f'{num} {username}: {msg}'
            lines[i] = '\n' + lines[i]
            if i != len(lines) - 1:
                lines[i] = lines[i] + '\n'
            break
    with open(filename, 'w') as f:
        count = 0
        last = lines[-1]
        for line in lines:
            if count == 0:
                f.write(line)
            else:
                f.write(f'{count} {" ".join(line.split(" ")[1:])}')

            count += 1


def isThreadCreator(username, threadtitle):
    with open(threadtitle, 'r') as f:
        line = f.readline()
        if(line.strip('\n') == username):
            return True
        return False


def removeThread(THREADS, threadtitle):
    print(THREADS)
    THREADS.remove(threadtitle)
    os.remove(threadtitle)


def deleteAllFiles(threads, files):
    for thread in threads:
        os.remove(thread)
    for file in files:
        os.remove(file)


def createFile(filename, threadname):
    f = open(f'{threadname}-{filename}', 'w+')
    f.close()


def checkThreadForFile(threadname, filename):
    with open(threadname, 'r') as f:
        l = f.readline()
        while(l):
            try:
                tmp = l.strip('\n')
                tmp = tmp.split(' ')
                if tmp[0].isnumeric():
                    l = f.readline()
                else:
                    if(tmp[1] == 'uploaded' and tmp[2] == filename):
                        return True
                    l = f.readline()
            except Exception:
                l = f.readline()

    return False


class Server:
    def __init__(self, server_port, adminPassword):
        self.THREADS = []
        self.FILES = []
        self.USERS = []
        self.CLIENTS = []
        self.adminPassword = adminPassword
        # Create server's socket
        # AF_NET -- underlying network is IPv4
        # SOCK_STREAM -- TCP socket
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.bind(('localhost', server_port))

    def handleUsernameRequest(self, client, username):

        if(username in self.USERS):
            print(f"{username} already logged in")
            response = 'LOGGEDIN'.encode('utf-8')
            client.send(response)
        elif(isRegistered(username)):
            response = 'PASSWORD'.encode('utf-8')
            client.send(response)
        else:
            print(f"new user {username}")
            response = 'NEWPASSWORD'.encode('utf-8')
            client.send(response)

    def handlePasswordRequest(self, client, username, password):
        if(isRegistered(username)):
            if(isValidLogin(username, password)):
                print(f"{username} logged in")
                self.USERS.append(username)
                response = "LOGIN".encode('utf-8')
                client.send(response)
                loggedin = True
            else:
                print(f"{username} wrong password")
                response = "INVALIDPASSWORD".encode('utf-8')
                client.send(response)
        else:

            new_credentials(username, password)
            print(f"new user {username} logging in")
            self.USERS.append(username)
            response = "LOGIN".encode('utf-8')
            client.send(response)

    def handleCreateThreadRequest(self, client, username, threadtitle):
        print(f'{username} issued the CRT command')

        if(fileExist(threadtitle)):
            print(f'Thread {threadtitle} exists')
            response = 'EXISTINGTHREAD'.encode('utf-8')
            client.send(response)
        else:
            print(f'Thread {threadtitle} created')
            createThread(username, threadtitle)
            self.THREADS.append(threadtitle)
            response = 'SUCCESS'.encode('utf-8')
            client.send(response)

    def handleMessageSendRequest(self, client, username, threadtitle, message):
        print(f'{username} issued the MSG command')

        if not fileExist(threadtitle):
            print(f'Thread {threadtitle} does not exist')
            response = 'NOTHREAD'.encode('utf-8')
            client.send(response)
        else:
            print(f'Message posted to {threadtitle} thread')
            msgNumber = getMessageNumber(threadtitle)
            msg = f'{msgNumber} {username}: {message}'
            writeMessage(threadtitle, msg)
            response = 'SUCCESS'.encode('utf-8')
            client.send(response)

    def handleMessageDeleteRequest(self, client, username, threadtitle, msgNo):
        print(f'{username} issued the DLT command')
        if not fileExist(threadtitle):
            print(f'Thread {threadtitle} does not exist')
            response = 'NOTHREAD'.encode('utf-8')
            client.send(response)
        elif not messageExists(threadtitle, msgNo):
            print(f'Message number {msgNo} does not exist')
            response = 'INVALIDMSGNO'.encode('utf-8')
            client.send(response)
        elif not messageModifiable(threadtitle, msgNo, username):
            print(f'Invalid permissions for {username} to delete the message')
            response = 'INVALIDCREDENTIALS'.encode('utf-8')
            client.send(response)
        else:
            print(f'Message {msgNo} deleted')
            deleteMessage(threadtitle, msgNo)
            response = 'SUCCESS'.encode('utf-8')
            client.send(response)

    def handleMessageEditRequest(self, client, username, threadtitle, msgNo, msg):
        print(f'{username} issued the EDT command')
        if not fileExist(threadtitle):
            print(f'Thread {threadtitle} does not exist')
            response = 'NOTHREAD'.encode('utf-8')
            client.send(response)
        elif not messageExists(threadtitle, msgNo):
            print(f'Message number {msgNo} does not exist')
            response = 'INVALIDMSGNO'.encode('utf-8')
            client.send(response)
        elif(not messageModifiable(threadtitle, msgNo, username)):
            print(f'Invalid permissions for {username} to modify the message')
            response = 'INVALIDCREDENTIALS'.encode('utf-8')
            client.send(response)
        else:
            print(f'Message {msgNo} modified')
            editMessage(threadtitle, msgNo, username, msg)
            response = 'SUCCESS'.encode('utf-8')
            client.send(response)

    def handleListThreadsRequest(self, client, username):
        print(f'{username} issued the LST command')
        if(self.THREADS):
            response = f'SUCCESS {" ".join(self.THREADS)}'.encode(
                'utf-8')
            client.send(response)
        else:
            response = 'NOTHREAD'.encode('utf-8')
            client.send(response)

    def handleRemoveThreadRequest(self, client, username, threadtitle):
        print(f'{username} issued the RMV command')
        if not fileExist(threadtitle):
            print(f'Thread {threadtitle} does not exist')
            response = 'NOTHREAD'.encode('utf-8')
            client.send(response)
        elif not isThreadCreator(username, threadtitle):
            print(f'Invalid permissions for {username} to delete the thread')
            response = 'INVALIDPERMISSIONS'.encode('utf-8')
            client.send(response)
        else:
            removeThread(self.THREADS, threadtitle)
            print(f'Thread {threadtitle} removed')
            response = 'SUCCESS'.encode('utf-8')
            client.send(response)

    def handleExitUserRequest(self, client, username):
        self.USERS.remove(username)
        print(f'{username} exited')
        response = 'SUCCESS'.encode('utf-8')
        client.send(response)
        self.CLIENTS.remove(client)

    def handleShutdownRequest(self, client, username, adminPassword):
        print(f'{username} issued the SHT command')
        if self.adminPassword == adminPassword:
            print('Server shutting down')
            deleteAllFiles(self.THREADS, self.FILES)
            response = f'SHUTDOWN {username}'.encode('utf-8')
            client.send(response)
            self.CLIENTS.remove(client)
            for c in self.CLIENTS:
                c.send(response)
            client.close()
            self.serverSocket.close()
            os._exit(1)
        else:
            print('Incorrect Password')
            response = 'INVALIDCREDENTIALS'.encode('utf-8')
            client.send(response)

    def handleReadThreadRequest(self, client, username, threadtitle):
        print(f'{username} issued the RDT command')
        if not fileExist(threadtitle):
            print(f'Thread {threadtitle} does not exist')
            response = 'NOTHREAD'.encode('utf-8')
            client.send(response)
        elif threadEmpty(threadtitle):
            response = 'THREADEMPTY'.encode('utf-8')
            client.send(response)
        else:
            f = open(threadtitle, 'r')
            data = f.readline()
            res = ''
            while(data):
                data = f.readline().strip('\n')
                res += data + '#'
            client.sendall(res.encode('utf-8'))
            print(f'Thread {threadtitle} Read')

    def handleUploadRequest(self, client, username, threadtitle, filename):
        print(f'{username} issued the UPD command')
        if not fileExist(threadtitle):
            print(f'Thread {threadtitle} does not exist')
            response = 'NOTHREAD'.encode('utf-8')
            client.send(response)
        else:
            response = 'SENDFILE'.encode('utf-8')
            client.send(response)
            data = client.recv(1024)
            if(data.decode('utf-8') == 'VOID'):
                return  # CHECK
            createFile(filename, threadtitle)
            f = open(f'{threadtitle}-{filename}', 'wb')
            data = client.recv(1024)
            while(data):
                f.write(data)
                data = client.recv(1024)
            f.close()
            msg = f'{username} uploaded {filename}'
            print(f'{filename} uploaded to thread {threadtitle}')
            writeMessage(threadtitle, msg)
            self.FILES.append(f'{threadtitle}-{filename}')
            response = 'SUCCESS'.encode('utf-8')
            client.send(response)

    def handleDownloadRequest(self, client, username, threadtitle, filename):
        if not fileExist(threadtitle):
            print(f'Thread {threadtitle} does not exist')
            response = 'NOTHREAD'.encode('utf-8')
            client.send(response)
        elif not checkThreadForFile(threadtitle, filename):
            print(f'File {filename} does not exist in thread {threadtitle}')
            response = 'NOFILEINTHREAD'.encode('utf-8')
            client.send(response)
        else:
            response = 'SEND'.encode('utf-8')
            client.send(response)
            with open(f'{threadtitle}-{filename}', 'rb') as f:
                l = f.read(1024)
                while(l):
                    client.sendall(l)
                    l = f.read(1024)
                    if not l:
                        break
                client.sendall(l)
                response = '#FILESENT'.encode('utf-8')
                print(f'{filename} downloaded from thread {threadtitle}')
                client.sendall(response)

    def client_recv(self, client):
        while True:
            try:
                request = client.recv(1024).decode('utf-8')
            except ConnectionError:
                print("Connection error; closing client")
                self.CLIENTS.remove(client)
                break
            requestList = request.split(' ')
            r = requestList[0]
            if r == 'USERNAME':
                self.handleUsernameRequest(client, requestList[1])
            elif r == 'PASSWORD':
                self.handlePasswordRequest(
                    client, requestList[1], requestList[2])
            elif r == 'CRT':
                self.handleCreateThreadRequest(
                    client, requestList[1], requestList[2])
            elif r == 'MSG':
                self.handleMessageSendRequest(
                    client, requestList[1], requestList[2], " ".join(requestList[3:]))
            elif r == 'DLT':
                self.handleMessageDeleteRequest(
                    client, requestList[1], requestList[2], requestList[3])
            elif r == "EDT":
                self.handleMessageEditRequest(
                    client, requestList[1], requestList[2], requestList[3], ' '.join(requestList[4:]))
            elif r == "LST":
                self.handleListThreadsRequest(client, requestList[1])
            elif r == "RMV":
                self.handleRemoveThreadRequest(
                    client, requestList[1], requestList[2])
            elif r == 'XIT':
                self.handleExitUserRequest(client, requestList[1])
            elif r == 'SHT':
                self.handleShutdownRequest(
                    client, requestList[1], requestList[2])
            elif r == 'RDT':
                self.handleReadThreadRequest(
                    client, requestList[1], requestList[2])
            elif r == 'UPD':
                self.handleUploadRequest(
                    client, requestList[1], requestList[2], requestList[3])
            elif r == "DWN":
                self.handleDownloadRequest(
                    client, requestList[1], requestList[2], requestList[3])

    def start(self):
        print("----The server is ready to receive---- \n")
        self.serverSocket.listen(10)
        while True:
            clientSocket, addr = self.serverSocket.accept()
            self.CLIENTS.append(clientSocket)
            thread = threading.Thread(
                target=self.client_recv, args=(clientSocket,)
            )
            thread.setDaemon(True)
            thread.start()


if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("Usage: ./Client.py {server_port} {admin_password}")
        exit()
    server_port = int(sys.argv[1])
    admin_password = str(sys.argv[2])
    server = Server(server_port, admin_password)
    server.start()
