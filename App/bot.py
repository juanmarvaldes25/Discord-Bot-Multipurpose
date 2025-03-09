from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests, bs4
from discord.ext import commands, tasks
from dataclasses import dataclass
import discord
import logging
import secrets
from session import Session
import busreq

BOT_TOKEN = '' #Bot token, very private
CHANNEL_ID = 1346296732547551353 #Channel id for 'Bot'
TASK_TIME_LIMIT_SECONDS = 40
 
logging.basicConfig(format='%(levelname)s:%(message)s', level = logging.INFO) #logging setup. Prints logging level before message
logger = logging.getLogger(__name__) #logger to print securely to console




bot = commands.Bot(command_prefix = "!", intents=discord.Intents.all()) #bot constructor, with all neccesary intents
session = Session() #new class of my type session

@bot.event
async def on_ready():
    logger.info("Bot Piufuiyan is ready to go!!") #will print this when ready!
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Piu, can you smell my fart?") #sends to specified channel, await needed as is asynchronous 
    
    
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
    if not session.is_active:
        await ctx.send("No Active Session Found: start one first")
        return
        
    session.is_active = False
    end_time = ctx.message.created_at.timestamp()
    duration = end_time - session.start_time
    
    #new function
    minutes = int(duration // 60)
    remaining_seconds = duration % 60

    formatted_time = f"{minutes} min {remaining_seconds:.2f}"
    print(formatted_time)


    await ctx.send(f"Session ended after {formatted_time} seconds")
    
@tasks.loop(minutes = TASK_TIME_LIMIT_SECONDS, count = 2)
async def reminder():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"Is anyone there?")
    
   
@bot.command()
async def bus(ctx, arg):
    bus_finder = busreq.BusFinder(logger)
    try:
     result = bus_finder.nextDeparture(arg)
     await ctx.send(result)
    
    except Exception as e:
     logger.error(f'Oh no! {e}')
     
    
#can be used to schedule things determed by x amount of ours


#to run the bot (will loop when run)
bot.run(BOT_TOKEN)
    
    









