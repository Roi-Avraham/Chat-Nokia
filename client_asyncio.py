import asyncio
from concurrent.futures import ThreadPoolExecutor


"""
The function "send_messages" gets input from the user (client) and
sends it to the server.
"""


async def send_messages(writer, prompt: str = "", ):
    with ThreadPoolExecutor(1, "AsyncInput") as executor:
        while True:
            try:
                # Getting input asynchronously.
                message = await asyncio.get_event_loop().run_in_executor(executor, input, prompt)

                # Checking if the client wants to exit the room.
                if message == "exit":
                    writer.write(message.encode())
                    await writer.drain()
                    print("You left so you can not sending or receiving messages")
                    break
                else:
                    # Sending the message the server
                    writer.write(message.encode())
                    await writer.drain()
            except:
                break


"""
The function "receive_messages" receive messages from the server.
"""


async def receive_messages(reader):
    while True:
        try:
            data = await reader.read(100)
            if len(data) == 0:
                print("The server is disconnected! please press enter to exit")
                break
            # Check if the server has disconnected the client.
            if data.decode() == "Server: Bye" or len(data) == 0:
                break
            print(data.decode())
        except:
            break

# The ip and port of the server
IP = '127.0.0.1'
PORT = 4444


async def main():
    # Opening connection with the server.
    reader, writer = await asyncio.open_connection(IP, PORT)
    # Reading the request from the server to write a name.
    data = await reader.read(100)
    print(data.decode())
    # Getting a name from the user.
    my_name = input()
    # Sending the name to the server.
    writer.write(my_name.encode())
    # Reading the welcome message from the server.
    data = await reader.read(100)
    print(data.decode())
    # Sending messages to the server asynchronously.
    sending = asyncio.ensure_future(send_messages(writer))
    await asyncio.sleep(1)
    # Receiving messages from the server asynchronously.
    receiving = asyncio.ensure_future(receive_messages(reader))
    await asyncio.sleep(1)
    # Wait until the client finishes sending and receiving messages - when the
    # client exit the room
    done, pending = await asyncio.wait(
        [receiving],
        return_when=asyncio.ALL_COMPLETED,
    )
    if receiving in done:
        sending.done()
        return

# put this line in comment if you are in linux
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
