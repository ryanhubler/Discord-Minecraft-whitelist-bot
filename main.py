import os
import discord
from discord.ext import commands
from mcrcon import MCRcon #mcrcon is used to create a remote console to your minecraft server

TOKEN = 'YOUR TOKEN GOES HERE'

bot = commands.Bot(command_prefix='#', help_command=None) #sets your prefix

@bot.event
async def on_ready():
   

@bot.command(name='whitelist')
async def whitelist(ctx, *, mess):
    usrname = mess #this is the username that the discord user types after #whitelist
    finalmsg = mess + " has been added" #adds usrname and has been added to the varible finalmsg
    with MCRcon("HOSTNAMEOFMCSERVER", "PASSWORDGOESHERE") as mcr: #send the whitelist command to minecraft server
        resp = mcr.command("/whitelist add " + usrname)
    await ctx.send(finalmsg) #sends finalmsg to the discord channel

bot.run('TOKEN')
