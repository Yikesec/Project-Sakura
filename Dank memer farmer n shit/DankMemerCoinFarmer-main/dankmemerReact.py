import discord, time, os

class MyClient(discord.Client):

    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):
        #if message.author == client.user:
        #    return
        channel = client.get_channel(752051281950015570)
        if message.author.id == 270904126974590976 and message.channel.id == 752051281950015570:
            #print("Message from {0.author}: {0.content}".format(message))
            message.content = message.content.replace('﻿','')
            if "god forbid" in message.content:
                print("Interacted with a Dragon !")
            if "EVENT TIME WOO!" in message.content:
                print("Interacting with a Event !")
            if "street" in message.content:
                time.sleep(1)
                await channel.send("street")
            if "couch" in message.content:
                time.sleep(1)
                await channel.send("couch")
            if "sink" in message.content:
                time.sleep(1)
                await channel.send("sink")
            if "christmas tree" in message.content:
                time.sleep(1)
                await channel.send("christmas tree")
            if "fridge" in message.content:
                time.sleep(1)
                await channel.send("fridge")
            elif "north pole" in message.content:
                time.sleep(1)
                await channel.send("north pole")
            elif "discord" in message.content:
                time.sleep(1)
                await channel.send("discord")
            elif "christmas card" in message.content:
                time.sleep(1)
                await channel.send("christmas card")
            elif "big bait catches big fish" in message.content:
                time.sleep(1)
                await channel.send("big bait catches big fish")
            elif "What type of meme do you want to post?" in message.content:
                time.sleep(1)
                await channel.send("k")
            elif "yes please" in message.content:
                time.sleep(1)
                await channel.send("yes please")
            elif "oh look a dragon" in message.content:
                time.sleep(1)
                await channel.send("oh look a dragon")
            elif "tree" in message.content:
                time.sleep(1)
                await channel.send("tree")
            elif "oh frick a dragon" in message.content:
                time.sleep(1)
                await channel.send("oh frick a dragon")
            elif "make snow angel" in message.content:
                time.sleep(1)
                await channel.send("make snow angel")                                             
            elif "frick off" in message.content:
                time.sleep(1)
                await channel.send("frick off")
            elif "glub glub glub" in message.content:
                time.sleep(1)
                await channel.send("glub glub glub")
            elif "mistletoe" in message.content:
                time.sleep(1)
                await channel.send("mistletoe")
            elif "krampus is a nerd" in message.content:
                time.sleep(1)
                await channel.send("krampus is a nerd")
            elif "push" in message.content:
                time.sleep(1)
                await channel.send("push")
            elif "dibs" in message.content:
                time.sleep(1)
                await channel.send("dibs")
            elif "happy holidays" in message.content:
                time.sleep(1)
                await channel.send("happy holidays")
            elif "throw snowball" in message.content:
                time.sleep(1)
                await channel.send("throw snowball")
            elif "get the camera ready" in message.content:
                time.sleep(1)
                await channel.send("get the camera ready")
            elif "whoville sucks" in message.content:
                time.sleep(1)
                await channel.send("whoville sucks")
            elif "build snowman" in message.content:
                time.sleep(1)
                await channel.send("build snowman")
            elif "hook line sinker" in message.content:
                time.sleep(1)
                await channel.send("hook line sinker")
            elif "dog" in message.content:
                time.sleep(1)
                await channel.send("dog")
            elif "pantry" in message.content:
                time.sleep(1)
                await channel.send("pantry")
            elif "mailbox" in message.content:
                time.sleep(1)
                await channel.send("mailbox")
            elif "dresser" in message.content:
                time.sleep(1)
                await channel.send("dresser")
            elif "uber" in message.content:
                time.sleep(1)
                await channel.send("uber")
            elif "grass" in message.content:
                time.sleep(1)
                await channel.send("grass")
            elif "pocket" in message.content:
                time.sleep(1)
                await channel.send("pocket")
            elif "laundromat" in message.content:
                time.sleep(1)
                await channel.send("laundromat")
            elif "bed" in message.content:
                time.sleep(1)
                await channel.send("bed")
            elif "air" in message.content:
                time.sleep(1)
                await channel.send("air")
            elif "f in chat" in message.content:
                await channel.send("f in chat")
            elif "fuck off karen" in message.content:
                await channel.send("fuck off karen")
            elif "i am so very bored" in message.content:
                await channel.send("i am so very bored")
            elif "wear a mask god damn it" in message.content:
                await channel.send("wear a mask god damn it")
            elif "dragon these nuts on your momma" in message.content:
                await channel.send("dragon these nuts on your momma")
            elif "dragon says rawr" in message.content:
                await channel.send("dragon says rawr")       
            elif "why didn't I just go fishing" in message.content:
                await channel.send("why didn't I just go fishing")
            
client = MyClient()
token = os.getenv("DISCORD_BOT_TOKEN")
client.run(token, bot = False)
