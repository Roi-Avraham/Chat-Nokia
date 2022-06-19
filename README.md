# Chat-Nokia

**Chat room - "whenApp"**
I worte 2 scripts in python using asyncio libary:
  1 - server
  2 - client
  
**Important note:** 
the server and client can be run on windows or linux. If you run the client on linux, you must put line 86 (in client script) in comment.

![image](https://user-images.githubusercontent.com/65657971/174467522-486f7fc5-f308-4b1a-b69d-2cfae2ce9017.png)


**Stages of activating the chat**
1. In the server, in lines 83 and 84 you can choose the server IP and PORT.
   ![image](https://user-images.githubusercontent.com/65657971/174473972-38ba4649-40a0-4edd-a53d-66bcf2b587b1.png)

   I put the ip 127.0.0.1 and the port to be 4444.
   If you want to change the ip or port of the server you must change them in the client script in lines 52-53 too.

2. Run the server in the command line(on pychram or other programming environment)/ terminal(on linux).

   ![image](https://user-images.githubusercontent.com/65657971/174240264-aa9e83c2-f41d-47aa-8113-7f2c859534e6.png)

3. Run how many clients you want to be in the chat room (there is only one chat room so all the clients that connecting to the server will reach the same room).
4. For each client, write your client name
  ![image](https://user-images.githubusercontent.com/65657971/174240736-04a77a3a-9cc3-4ff1-b393-5f58002e0b87.png)
5. Now you can start to send messges and they will be sent to all the clients in the room.

   Example (roee send to everyone "hello world!"):
   
   roi client - first client:
   ![image](https://user-images.githubusercontent.com/65657971/174241125-72f20163-29f0-4a56-864b-8bec99fef02f.png)
   roy client - secound client:
   ![image](https://user-images.githubusercontent.com/65657971/174241279-71779416-e7ed-49d5-aba0-6e38a9e6671a.png)
   roee client - third client:
   ![image](https://user-images.githubusercontent.com/65657971/174241443-060a34be-4e25-4a9d-b371-fae92de52d04.png)

6. To exit from the chat, the client can write "exit" or you can terminate his process.
7. If the server fell, all the clients get message that the server is disconnected. You need to press enter for finishing the client process.
   ![image](https://user-images.githubusercontent.com/65657971/174467657-d1e0f2fd-5aad-4b1b-922b-771fb3618cc6.png)

I hope you enjoy using the chat :)!

Thank you very much for the opportunity!
