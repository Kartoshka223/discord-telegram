import random
import datetime
import discord
from discord.ext import commands
from PIL import Image
import requests
import os
import dog
import randomcatimage


TOKENDISCORD = ''
PREFIX = '/'
intents = discord.Intents().all()

bot = commands.Bot(command_prefix=PREFIX, intents=intents)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online)
    print(f'Bot {bot.user} is online.')
@bot.command()
async def tg(ctx, *args):
        trt = ''.join(args)
        print(trt)
        with open("file.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                        if trt in line:
                                
                                await ctx.send(lines) 

@bot.command()
async def img(ctx, *args):
     
     img_adres = ''.join(args)
#     img = requests.get(img_adres) 
     code = random.randint(1000,9999)
     print(code)
     papka = "papka_s_kartinkami"
     if not os.path.isdir(papka):
         os.mkdir(papka)
     out = open(f'{papka}/kartinka_{code}.jpg',"wb")
     out.write(img.content)
     out.close()
     await ctx.send(f'код: {code}')
     code = img_adres[-4:]
     directory = os.fsencode(papka)
     print(directory)

@bot.command()
async def sobak(ctx,*args):

        papka = "papka_s_sobakami"
        if not os.path.isdir(papka):
                os.mkdir(papka)
        img = random.randint(1000,9999)
        sobaka = dog.getDog(directory= papka, filename=f'dog_{img}')
        await ctx.send(file=discord.File(f'{papka}/dog_{img}.jpg'))

@bot.command()
async def cat(ctx,*args):
        cat = randomcatimage.getCat()
        papka = "papka_s_kotikami"
        if not os.path.isdir(papka):
                os.mkdir(papka)
        print(cat)
        img = random.randint(1000,9999)
        await ctx.send(cat)

@bot.command()
async def pol(ctx):
    try:
        with open("file.txt", "r") as file:
            lines = file.readlines()
            line = lines[-1:]
            line = line[0]
            line = line[11:-35]
            await ctx.reply(line)
    except FileNotFoundError:
        await ctx.reply('Ошибка: файл не найден.')
    except Exception as e:
        await ctx.reply(f'Произошла ошибка: {e}')

@bot.command()
async def otv(ctx, *args):
    code = random.randint(10043,99979)
    try:
        date = datetime.datetime.now()
        format_date = date.strftime("%Y-%m-%d %H:%M:%S")
        message = ' '.join(args)
        await ctx.send(f'Сообщение "{message}" сохранено.')
        format_message = f'\nсообщение: "{message}"' + f'код: {code}' + f' время отправки: {format_date}'
        with open("file.txt", "a") as file:
            file.write(format_message)

    except Exception as e:
        await ctx.send(f'Произошла ошибка при сохранении сообщения: {e}')

@bot.command()
async def start(ctx):
    await ctx.send('Привет, я бот для передачи сообщений из ДС в ТГ и наоборот. Чтобы написать сообщение, используйте /otv и ваше сообщение. Чтобы получить сообщение, используйте /pol.')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Команда не найдена. Проверьте правильность написания.')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Ошибка: не все обязательные аргументы предоставлены.')
    else:
        await ctx.send(f'Произошла ошибка: {error}')

bot.run(TOKENDISCORD)