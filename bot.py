import discord
from discord.ext import commands
import random
import requests

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def meme(ctx):
    try:
        memeAPI = requests.get("https://meme-api.com/gimme")
        memeData = memeAPI.json()
        memeUrl = memeData['url']
        memeName = memeData['title']
        memeSubreddit = memeData['subreddit']
        embed = discord.Embed(title=memeName, url=memeUrl, color=discord.Color.red())
        embed.set_image(url=memeUrl)
        await ctx.send(embed=embed)
    except Exception as e:
        print("Error fetching meme:", e)
        await ctx.send("Sorry, couldn't fetch a meme right now.")

@bot.command()
async def hello(ctx):
    await ctx.send(choose_randomly(greetings))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

# Greetings list
greetings = [
    "Hello!",
    "Hi there!",
    "Hey!",
    "Good morning!",
    "Good afternoon!",
    "Good evening!",
    "Howdy!",
    "Greetings!",
    "What's up?",
    "Hiya!",
    "Hola!",
    "Bonjour!",
    "Ciao!",
    "Salut!",
    "Namaste!",
    "Konichiwa!",
    "G'day mate!",
    "Yo!",
    "Sup?",
    "How's it going?",
    "Nice to see you!",
    "Welcome!",
    "Hi!",
    "Hey there!",
    "Hello, friend!",
    "Hey, buddy!",
    "Hiya, pal!",
    "Good to see you!",
    "How's everything?",
    "What's new?",
    "Pleased to meet you!",
]

def choose_randomly(greetings):
    return random.choice(greetings)

# Token
bot.run('YOUR TOKEN HERE')
