import discord
import config
import asyncio
import requests
import pymongo
from bs4 import BeautifulSoup
from discord.ext import commands

from discord.embeds import Embed
from embed import *

import db

# client = pymongo.MongoClient("mongodb+srv://" + config.DB_USERNAME + ":" +
#                              config.DB_PASSWORD + "@umt-bot.upexdyb.mongodb.net/?retryWrites=true&w=majority")
# db = client.usersinfo
login_url = ('https://pelajar.mynemo.umt.edu.my/portal_login_ldap.php')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

# @bot.command()
# async def facts(ctx):
#     print("test facts")


@bot.command()
async def login(ctx, *, args=None):
    if isinstance(ctx.channel, discord.channel.DMChannel) and ctx.author != bot.user:
        if args != None and len(args.split()) == 2:
            username, password = args.split()
            # payload = {
            #     'login': 'student',
            #     'username': username,
            #     'password': password,
            #     'submit': 'Log Masuk'
            # }
            # response = requests.post(
            #             login_url, data=payload, verify=False)
            try: # Check if user exists     
                if (db.checkUser(username)): 
                    embed = smallEmbed(
                        "User already exists", "Please check +help for available commands")
                    await ctx.channel.send(embed=embed)
                else:
                    payload = { 
                        'login': 'student',
                        'username': username,
                        'password': password,
                        'submit': 'Log Masuk'
                    }
                    response = requests.post(login_url, data=payload, verify=False)
                    if response.status_code == 200: # Successful login
                        db.addUser(username, password)
                        # res = db.addUser(
                        #     {"username": username, "password": password})
                        embed = smallEmbed(
                            "User added!", "You can now use the bot's commands")
                        await ctx.channel.send(embed=embed)
                    else:
                        embed = smallEmbed(
                            "Incorrect credentials!", "Your login credentials don't match an account in our system")
                        await ctx.channel.send(embed=embed)
            except:
                embed = exceptionEmbed()
                await ctx.channel.send(embed=embed)
        else:
            embed = smallEmbed(
                "Invalid arguments", "Please check +help for available commands")
            await ctx.channel.send(embed=embed)
    elif not isinstance(ctx.channel, discord.channel.DMChannel):
        embed = smallEmbed(
            "Invalid channel", "Please use this command in DMs")
        await ctx.channel.send(embed=embed)

# @bot.event
# async def on_ready():
#     print("Online.")

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#     await message.channel.send("Hello")


# async def setup():
#     print("Setting up...")


# async def main():
#     await setup()
#     await bot.start(config.TOKEN)

# asyncio.run(main())

bot.run(config.TOKEN)
