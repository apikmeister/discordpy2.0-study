from discord.embeds import Embed
import discord

def smallEmbed(title,description):
    embed = discord.Embed(title=title, description=description, color=discord.Color.red())
    return embed

def thumbnailEmbed(title,description,url):
    embed = discord.Embed(title=title, description=description, color=discord.Color.red())
    embed.set_thumbnail(url=url)
    return embed

def exceptionEmbed():
    embed = discord.Embed(title="Something went wrong :(", description="Please try again!", color=discord.Color.red())
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/yK1PgRCTUvZvC2uoRZgdLC3pT6M8G4gX-WGTPIcfsCQ/https/i.imgur.com/au2Yx3O.mp4")
    return embed