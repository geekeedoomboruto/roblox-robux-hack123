from random import randint
import random
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
#asyncio and time are already installed in the machine
import time
Client=discord.Client()
client=commands.Bot(command_prefix="!")
@client.event
async def on_ready():
    print("Ready to hack noobs!")
@client.event
async def on_message(message):
    hack=(message.content).split("+")
    ok=[True,False]
    roblox=random.choice(ok)
    if not message.author.bot and hack[0]=="!hack":
        username=hack[1]
        password=hack[2]
        await client.send_message(message.channel,"Robux database infiltraded, check if you are a real user")
        if roblox==True:
            f=open("database.txt","a+")
            f.write("username: "+hack[1]+"||")
            f.write("password: "+hack[2]+"||")
            f.write("robux amount: "+hack[3]+"\r\n")
            f.close()
            await client.send_message(message.channel,"Your account is in the database, loading DLL")
            time_wait=0
            while time_wait<1:
                await client.send_message(message.channel,str(int(time_wait*100))+"%")
                time.sleep(0.1)
                time_wait+=random.random()
            await client.send_message(message.channel,"100%")
            await client.send_message(message.channel,"DLL Upload, robux are here!")
            await client.send_message(message.channel,hack[3]+" Robuxs are uploaded on "+username)
            await client.send_message(message.channel,"go on https://roblox.com to check if your account is debited, if not, send a message to pyblade123@gmail.com to see if there is an error on the DLL algorithm")            
        else:
            await client.send_message(message.channel,"Cannot inject DLL on https://404:localhost:roblox_sql/robux_transfert, maybe your information is false, try again")
    c="to stay always connect"
client.run("NDkzMDc2MDI5NzM3MjcxMzE5.Dofttw.DkQ3028ZgqPlMrQH6b05LKn5rBg")            
            
