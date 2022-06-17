import asyncio

# the list of all the clients
writers = []
name_of_clients = {}

'''
The function "send" gets client(writer), nick name of client(name) and message.
The function send to all the other clients the message in the name of 
the client she gets.  
'''


def send(writer, name, message):
    for w in writers:
        if w != writer:
            w.write(f"{name}: {message}".encode())
        else:
            w.write(f"You: {message}".encode())


def not_send_yourself(writer, name, message):
    for w in writers:
        if w != writer:
            w.write(f"{name}: {message}".encode())

'''
The function "handle" performs the communication between the server and the client
'''


async def handle(reader, writer):
    # add the current client to the list of all clients
    writers.append(writer)

    # receive the name of the client
    message = "Please enter your name: "
    writer.write(f"Server: {message}".encode())
    name = await reader.read(100)
    user = name.decode().strip()
    name_of_clients[writer] = user

    # sending welcome message
    message = f"welcome {user} to whenApp :) ! if you want to leave the group just write 'exit'"
    writer.write(f"Server: {message}".encode())
    # notify all the clients in the room that new client added to the room
    message = f"{user} added to the group"
    not_send_yourself(writer, "Server", message)

    while True:

        # receive message from the client
        data = await reader.read(100)
        if len(data) == 0:
            message = f"{user} left the group :("
            not_send_yourself(writer, "Server", message)
            break
        message = data.decode().strip()

        # check if the client wants to close the connection
        if message == "exit":
            message = f"{user} left the group :("
            not_send_yourself(writer, "Server", message)
            writer.write(f"Server: Bye".encode())
            break

        # sending the message to all the clients except to the client who wrote the message
        send(writer, user, message)
        # Wait until it is appropriate to resume writing to the stream
        await writer.drain()
    # remove the client form the list of the clients in the room
    writers.remove(writer)
    writer.close()

# the ip and port of the server
IP = '127.0.0.1'
PORT = 4444


async def main():
    # open the server
    server = await asyncio.start_server(
        handle, IP, PORT)
    print('Welcome to whenApp server:)')
    async with server:
        await server.serve_forever()


asyncio.run(main())
