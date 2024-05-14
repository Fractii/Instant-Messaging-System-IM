import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("0.tcp.ap.ngrok.io" , 11227))
#127.0.0.1
nickname = input("Enter your nickname: ")

def receive():    
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK' :
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured")
            client.close()
            break
        
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))
        
receive_thread = threading.Thread(target=receive)
receive_thread.start()

writing_thread = threading.Thread(target=write)
writing_thread.start()