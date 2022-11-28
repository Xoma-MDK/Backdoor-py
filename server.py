import socket 
import select 
import controler 
import re



client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client_socket.bind(("127.0.0.1", 9990))
client_socket.listen() 
conn, addr = client_socket.accept() 

print('send_file, get_file, help [command]')

while True: 
    try:
        command = input('>> ') 
        conn.send(command.encode())
        if 'help' in command:
            if 'get_file' in command:
                print('\n\nget_file [getting file] [new file name without extension]\nExtension will be the same as "getting file"\n\n')
            elif 'send_file' in command:
                print('\n\nsend_file [sending file] [new file on socket computer without extension]\nExtension will be the same as "sending file"\n\n')
            else:
                output = conn.recv(2000).decode()
                print(output)
        elif 'get_file' in command: 
            print(controler.recv_file(conn,command))
        elif 'send_file' in command:
            print(controler.send_file(conn, command))
        else:
            if(controler.check_if_ready(conn)):
                output = conn.recv(2000).decode()
            else:
                continue
            print(output)
    except Exception as e:
        print(e)
