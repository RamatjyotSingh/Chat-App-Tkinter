import socket
import sys
import time
import traceback

HOST = 'localhost'
PORT = 50017
TIMEOUT =300
WARMUP = 60

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        start_time = time.time()
        message_sent = 0
        msg_received = 0
        try:
            while time.time() - start_time < TIMEOUT + WARMUP:  # Run for 5 minutes + 1 minute warmup
                client_socket.sendall((str(len("Test message")).zfill(4) + "Test message").encode('utf-8'))
                message_sent += 1
                
                client_socket.recv(1024)
                msg_received += 1
               
        except Exception as e:
            print(f"An error occurred: {e}")
            e.with_traceback()
        

        
        print(f"Messages sent: {message_sent}")
        print(f"Messages received: {msg_received}")
        print(f"Messages lost: {message_sent - msg_received}")
        print(f"Messages sent per second: {message_sent / TIMEOUT}")
        print(f"Messages received per second: {msg_received / TIMEOUT}")
        message_sent = 0
        msg_received = 0

try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    print("Exiting...")
    sys.exit(0)
except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()
    sys.exit(1)
