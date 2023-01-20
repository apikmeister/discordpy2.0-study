import discord
import config
import requests
from bs4 import BeautifulSoup
from discord.ext import commands

from discord.embeds import Embed
from embed import *

import db

secure_url = ('https://pelajar.mynemo.umt.edu.my/exam/smp_x_all_bi.php')
login_url = ('https://pelajar.mynemo.umt.edu.my/portal_login_ldap.php')


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.command()
async def login(ctx, *, args=None):
    discord_id = ctx.author.id
    if isinstance(ctx.channel, discord.channel.DMChannel) and ctx.author != bot.user:
        if args != None and len(args.split()) == 2:
            username, password = args.split()
            try:  # Check if user exists
                if (db.checkUser(username)):
                    embed = smallEmbed(
                        "User already exists", "Please check +help for available commands")
                    await ctx.channel.send(embed=embed)
                else:
                    payload = {
                        'login': 'student',
                        'uid': username,
                        'pwd': password,
                        'submit': 'Log Masuk'
                    }
                    # db.getResponse(payload)
                    # s = requests.Session()
                    # response = s.post(login_url, data=payload, verify=False, allow_redirects=True)
                    if any(r.status_code == 302 for r in db.getResponse(payload).history):  # Successful login
                        db.addUser(discord_id, username, password)
                        embed = smallEmbed(
                            "User added!", "You can now use the bot's commands")
                        await ctx.channel.send(embed=embed)
                    else:  # Incorrect credentials
                        embed = smallEmbed(
                            "Incorrect credentials!", "Your login credentials don't match an account in our system")
                        await ctx.channel.send(embed=embed)
            except Exception as e:  # Error
                print(e)
                embed = exceptionEmbed()
                await ctx.channel.send(embed=embed)
        else:  # Invalid arguments
            embed = smallEmbed(
                "Invalid arguments", "Please check +help for available commands")
            await ctx.channel.send(embed=embed)
    elif not isinstance(ctx.channel, discord.channel.DMChannel):  # Invalid channel
        embed = smallEmbed(
            "Invalid channel", "Please use this command in DMs")
        await ctx.channel.send(embed=embed)


@bot.command()
async def gpa(ctx):
    discord_id = ctx.author.id
    if (db.checkUser(discord_id)):
        user = db.getUser(discord_id)
        try:
            r = db.getSession(user).get(secure_url)
            bs = BeautifulSoup(r.content, 'html.parser')
            gpa_element = bs.find_all(
            'td', text='Grade Points Average (GPA)')
            for all_siblings in gpa_element:
                gpa = all_siblings.find_next_sibling()
                embed = smallEmbed("Grade Points Average (GPA)", f"{gpa.text}")
                await ctx.channel.send(embed=embed)
        except Exception as e:
            print(e)
            embed = exceptionEmbed()
            await ctx.channel.send(embed=embed)


bot.run(config.TOKEN)
