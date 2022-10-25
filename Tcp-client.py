import socket 

def targetport():
    try:
        target_port = int(input("target port: "))
        return target_port
    except ValueError as error:
        print(f"You made a/an {error}, No strings are allowed ")
        return targetport()

# Getting the target host and port
target_host = input("IP address:")
target_port = targetport()

# creating ipv4 with tcp connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting the host to the target
client.connect((target_host, target_port))

# sending data to the client
data = input("send : ")
client.send(data)

# recieving and printing data
data, addr = client.recv(4096)
print(f"{addr} : {data}")

client.close()



