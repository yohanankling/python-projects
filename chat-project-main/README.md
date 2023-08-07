# Server and Client Chat Application Readme

This repository contains two Python scripts for a simple chat application using TCP and UDP protocols. The application includes a server and a client that can connect to the server to exchange messages and files.

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

## Contributing

Feel free to contribute to this project by creating issues or pull requests for bug fixes, improvements, or additional features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
