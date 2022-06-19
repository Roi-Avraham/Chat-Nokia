import asyncio

# The list of all the clients
writers = []


'''
The function "send" gets client(writer), nick name of client(name) and message.
The function sends the message in the name of 
the client she gets to all the clients in the room.
'''


def send(writer, name, message):
    for w in writers:
        if w != writer:
            w.write(f"{name}: {message}".encode())
        else:
            w.write(f"You: {message}".encode())


'''
The function "not_send_yourself" gets client(writer), nick name of client(name) and message.
The function send the message in the name of 
the client she gets to all the other clients except the client she got.
'''


def not_send_yourself(writer, name, message):
    for w in writers:
        if w != writer:
            w.write(f"{name}: {message}".encode())


'''
The function "handle" performs the communication between the server and the client.
'''


async def handle(reader, writer):
    # Adding the current client to the list of all clients.
    writers.append(writer)

    # Receiving the name of the client.
    message = "Please enter your name: "
    writer.write(f"Server: {message}".encode())
    name = await reader.read(100)
    user = name.decode().strip()

    # Sending welcome message.
    message = f"welcome {user} to whenApp :) ! if you want to leave the group just write 'exit'"
    writer.write(f"Server: {message}".encode())
    # Notify all the clients in the room that new client added to the room.
    message = f"{user} added to the group"
    not_send_yourself(writer, "Server", message)

    while True:

        # Receiving message from the client.
        data = await reader.read(100)
        if len(data) == 0:
            message = f"{user} left the group :("
            not_send_yourself(writer, "Server", message)
            break
        message = data.decode().strip()

        # Checking if the client wants to close the connection.
        if message == "exit":
            message = f"{user} left the group :("
            not_send_yourself(writer, "Server", message)
            writer.write(f"Server: Bye".encode())
            break

        # Sending the message to all the clients except the client who wrote the message.
        send(writer, user, message)
        # Wait until it is appropriate to resume writing to the stream.
        await writer.drain()
    # Removing the client from the list of the clients in the room.
    writers.remove(writer)
    writer.close()

# The ip and port of the server.
IP = '127.0.0.1'
PORT = 4444


async def main():
    # Opening the server.
    server = await asyncio.start_server(
        handle, IP, PORT)
    print('Welcome to whenApp server:)')
    async with server:
        await server.serve_forever()


asyncio.run(main())
