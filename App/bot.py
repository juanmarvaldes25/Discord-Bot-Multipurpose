from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from discord.ext import commands
from dataclasses import dataclass
import discord
import logging
import secrets

BOT_TOKEN = '...' #Bot token, very private
CHANNEL_ID = 1346296732547551353 #Channel id for 'Bot'
logging.basicConfig(format='%(levelname)s:%(message)s', level = logging.INFO) #logging setup. Prints logging level before message
logger = logging.getLogger(__name__) #logger to print securely to console
fartPhrases = ["So smelly!", "Yuck!", "No smell...", "Very nice", "It's wet...", "Singing fart!"]

@dataclass #new class to store study session data
class Session:
    is_active: bool = False
    start_time: int = 0


bot = commands.Bot(command_prefix = "!", intents=discord.Intents.all()) #bot constructor, with all neccesary intents
session = Session() #new class of my type session

@bot.event
async def on_ready():
    logger.info("Bot Piufuiyan is ready to go!!") #will print this when ready!
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Piu, can you smell my fart?") #sends to specified channel, await needed as is asynchronous 
    
@bot.command() #if needs to respond to user, use the command tag
async def fart(ctx): #ctx is context argument
    phraseIndex = secrets.choice(fartPhrases)
    logger.info("Sending message: %s", phraseIndex)
    await ctx.send(phraseIndex)
    
@bot.command() #as many string arguments as needed example
async def commonsense(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f"{len(args)} arguments: {arguments}")
    
@bot.command() #as many int arguments as required example
async def add(ctx, *arr):
    result = 0
    for i in arr:
        result+= int(i)
    await ctx.send(f"Result: {result}")
    
@bot.command() #start a session - may be useful for poker?
async def start(ctx):
    if session.is_active:
        await ctx.send("A session is already active!")
        return
    session.is_active = True
    session.start_time  = ctx.message.created_at.timestamp()
    human_readable_time = ctx.message.created_at.strftime("%H:%M:%S")
    await ctx.send(f"Session started at {human_readable_time}")
    
@bot.command()
async def end(ctx):
    #TODO
    
   
    
#to run the bot (will loop when run)
bot.run(BOT_TOKEN)
    
    









