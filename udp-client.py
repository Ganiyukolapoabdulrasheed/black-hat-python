import socket

def targethost():
    try:
        target_host=int(input('target host : '))
        return target_host
    except ValueError as error:
        print(f"You made a/an {error}, No strings are allowed")
        return targethost()

def targetport():
    try:
        target_port = int(input("target port"))
        return target_port
    except ValueError as error:
        print(f"You made a/an {error}, No strings are allowed ")
        return targetport()


# Getting the target host and the target port 
target_host = targethost()  
target_port = targetport()


# creating a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# sending data
data = input("send : ")
client.sendto(data, (target_host, target_port))

# recieving and printing the data
data, addr = client.recvfrom(4096)
print(f"{addr}: {data}")


