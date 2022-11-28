from socket import socket
from select import select
import re


def check_if_ready(s: socket):
    ready, _, _ = select([s], [], [], 0.5) 
    if s in ready:
        return True
    else:
        return False
    
def  recv_file( s: socket, command: str): 
    try:
        data = ''
        while True:
            if check_if_ready(s):
                data += s.recv(1024).decode()
            else:
                break

        file_name = get_filename_with_format(command)
        
        with open(file_name, "w") as file:
            file.writelines(data)

        return file_name
        
    except Exception as e:
        print(e)

def send_file(s: socket, command: str):
    try:
        file_name = command.split(" ")[1]

        with open('./' + file_name, "r") as file:
            for i in file: 
                s.send(i.encode())
        return 'sent'

    except Exception as e:
        print(e)

def get_filename_with_format(command:str):
    format_regex = re.compile(r'\w*\.\w*')
    
    format = command.split(' ')[1]
    match_format = format_regex.findall(format)
 
    file_name = command.split(' ')[2] + '.' + match_format[len(match_format)-1].split('.')[1]

    return (file_name)




            

