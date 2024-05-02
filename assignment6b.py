import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "192.168.60.1"
port = 6969
complete_address = (ip, port)
s.bind(complete_address)

# Function to receive file
def receive_file():
    data, sender_address = s.recvfrom(1024)
    filename = data.decode('utf-8')
    with open(filename, "wb") as file:
        while True:
            data, sender_address = s.recvfrom(1024)
            if not data:
                break
            file.write(data)
    print(f"File '{filename}' received successfully.")

# Main loop to receive messages or files
while True:
    data, sender_address = s.recvfrom(1024)
    message = data.decode('ascii')
    print(message)

    # Check if it's a file transfer request
    if message.lower() == "file":
        receive_file()
    else:
        # Handle regular messages
        reply_message = "Thanks for your feedback"
        s.sendto(reply_message.encode('ascii'), sender_address)