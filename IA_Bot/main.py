import discord
import random
import os
from discord.ext import commands
from bot_logic import *
from model import get_class
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def d20(ctx):
    n = random.randint(1,20)
    await ctx.send(str(n))
@bot.command()
async def d5(ctx):
    n = random.randint(1,5)
    await ctx.send(str(n))
@bot.command()
async def flip(ctx):
    await ctx.send(flip_coin())
@bot.command()
async def meme (ctx):
    memes: list[str] = random.choice(os.listdir("bot_images"))
    with open(f'bot_images/{memes}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file = picture)
@bot.command('dog')
async def dog(ctx):
    '''Uma vez que chamamos o comando duck, o programa chama a função get_duck_image_url '''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
@bot.command()
async def imagem(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./images/{file_name}")
            await ctx.send(f'Imagem recebida: ./images/{file_name}\nURL: {file_url}')
              
    else:
        await ctx.send('Por favor, envie uma imagem junto com o comando.')
@bot.command()
async def classificar(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./images/{file_name}")
            resultado, confianca = get_class("keras_model.h5", "labels.txt", f"./images/{file_name}")
            await ctx.send(f"Placa: **{resultado.strip()}** | Confiança: **{confianca * 100:.1f}%**")
    else:
        await ctx.send('Por favor, envie uma imagem junto com o comando.')

bot.run("discord_bot_token")