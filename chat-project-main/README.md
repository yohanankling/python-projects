# Server and Client Chat Application Readme

This repository contains two Python scripts for a simple chat application using TCP and UDP protocols. The application includes a server and a client that can connect to the server to exchange messages and files.

## Screenshots
sending messages:</br>
<img width="875" alt="text" src="https://github.com/yohanankling/python-projects/assets/93263233/6f0b6417-d9fe-443e-afc1-b39d267e7c57">
</br>broadcast:</br>
<img width="797" alt="broadcast" src="https://github.com/yohanankling/python-projects/assets/93263233/4ff3061d-8d59-4d72-92b6-c3d490fdb019">
</br>online list:</br>
<img width="532" alt="online" src="https://github.com/yohanankling/python-projects/assets/93263233/70fc3e53-3f5e-414d-adc4-ee6074b591d7">
</br>download a file from server, using UDP:</br>
<img width="698" alt="download" src="https://github.com/yohanankling/python-projects/assets/93263233/4c0dfbbf-fc07-4c22-916b-9fbe96e1efe9">

## Server

### Requirements
- Python 3.x

### Description

The server script (`server.py`) sets up a TCP socket and listens for incoming connections from clients. It allows multiple clients to connect and chat with each other. The server maintains a list of connected clients and their nicknames.

### Usage

1. Run the server script on the machine where you want to host the chat server.

   ```bash
   python server.py
   ```

2. The server will display a message indicating it is ready to serve incoming connections.

3. Clients can now connect to the server using the client script.

### Supported Commands

The server supports the following commands from the clients:

- `broadcast`: Send a message to all connected clients.
- `online`: Request a list of online clients.
- `user name,message`: send a private message to someone.
- `files`: Request a list of available files on the server.
- `download,<file_name>`: Download a file from the server.

### Note

The server should be hosted on a machine with a publicly accessible IP address or domain name to allow clients to connect from different devices.

## Client

### Requirements
- Python 3.x
- Tkinter (Python GUI library)

### Description

The client script (`client.py`) provides a simple graphical user interface (GUI) using Tkinter to interact with the chat server. Clients can connect to the server, send messages to other clients, request a list of online clients, and download files shared by the server.

### Usage

1. Run the client script on the machine where you want to use the chat client.

   ```bash
   python client.py
   ```

2. The script will prompt you to enter the server's IP address. If you leave it blank, the client will attempt to connect to the server running on the local machine.

3. Enter your desired nickname and click "Connect" to join the chat.

4. Use the input box to send messages. To send a message to a specific client, use the format `"person name,text"` (e.g., `"John,Hello John, how are you?"`).

5. You can also use the "Online List" button to request a list of online clients and the "Files List" button to request a list of available files on the server.

6. To download a file shared by the server, use the format `"download,file_name.type"` (e.g., `"download,image.jpg"`).

### Note

- The client script allows only one connection at a time. If you want to use multiple clients, run separate instances of the client script for each user.
- The client script will automatically disconnect if you close the application window.

## UDP section:

The UDP (User Datagram Protocol) section in the server and client scripts enables file transfer between them. UDP is a connectionless and unreliable protocol, so we implement a simple algorithm to ensure reliable data transfer:

1. **File Splitting**: The server splits the file into small packets and stores them in a list.

2. **UDP Sockets**: Both server and client create two UDP sockets for sending and receiving data.

3. **UDP Send and Receive Loops**: The server sends packets to the client, and the client acknowledges each received packet.

4. **ACK Mechanism**: The server retransmits packets if the client does not acknowledge them within a timeout.

5. **End of Transfer**: The server sends a special packet to indicate the end of the file transfer.

6. **File Reconstruction**: The client reconstructs the file from received packets.

Important: UDP lacks some features for robust data transfer, so for large or unreliable networks, other protocols like TCP may be more suitable.

## Contributing

Feel free to contribute to this project by creating issues or pull requests for bug fixes, improvements, or additional features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
