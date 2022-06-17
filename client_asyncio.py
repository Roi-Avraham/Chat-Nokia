import asyncio
from concurrent.futures import ThreadPoolExecutor


"""
The function "send_messages" gets input from the user (client) and
sending it to the server.
"""


async def send_messages(writer, prompt: str = "", ):
    with ThreadPoolExecutor(1, "AsyncInput") as executor:
        while True:
            try:
                # gets input asynchronously
                message = await asyncio.get_event_loop().run_in_executor(executor, input, prompt)

                # check if the client wants the exit the room
                if message == "exit":
                    writer.write(message.encode())
                    await writer.drain()
                    print("You left so you can not sending or receiving messages")
                    break
                else:
                    # sending the message the server
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
                print("the server is disconnected! please press enter to exit")
                break
            # check if the server disconnect the client
            if data.decode() == "Server: Bye" or len(data) == 0:
                break
            print(data.decode())
        except:
            break

# the ip and port of the server
IP = '127.0.0.1'
PORT = 4444


async def main():
    # open connection with the server
    reader, writer = await asyncio.open_connection(IP, PORT)
    # read the request from the server to write name
    data = await reader.read(100)
    print(data.decode())
    # get name from the user
    my_name = input()
    # send it to the server
    writer.write(my_name.encode())
    # read the welcome message from the server
    data = await reader.read(100)
    print(data.decode())
    # sending messages to the server asynchronously
    sending = asyncio.ensure_future(send_messages(writer))
    await asyncio.sleep(1)
    # receiving messages from the server asynchronously
    receiving = asyncio.ensure_future(receive_messages(reader))
    await asyncio.sleep(1)
    # wait until the client finishes sending and receiving messages - when the
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
