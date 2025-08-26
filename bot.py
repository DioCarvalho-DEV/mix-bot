import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
bot = commands.Bot("!", intents=intents)

@bot.event
async def on_ready():
    print("Bot inicializado")
    sincs = await bot.tree.sync()
    print(f"{len(sincs)} comandos sincronizados!")

@bot.command()
async def ola(ctx:commands.Context):
    nome = ctx.author.mention
    await ctx.reply(f"Olá {nome}! Tudo bem?")

@bot.tree.command()
async def hello(interact:discord.Interaction):
    await interact.response.send_message(f"Hello my Friendo {interact.user.mention}!")

bot.run(TOKEN)