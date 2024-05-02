import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "192.168.60.165"
port = 9999
target_ip = (ip, port)

# Function to send file
def send_file(file_path):
    with open(file_path, "rb") as file:
        filename = file_path.split("/")[-1]
        s.sendto(filename.encode('utf-8'), target_ip)  # Sending filename first
        while True:
            data = file.read(1024)
            if not data:
                break
            s.sendto(data, target_ip)
    print("File sent successfully.")

# Example usage:
file_path = input("Enter the file path to send: ")
send_file(file_path)