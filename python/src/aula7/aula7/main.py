import discord
import asyncio
import aiohttp
from clients import OllamaAPI
from models import OllamaPrompt
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file
bot = discord.Bot()
request_tasks = {}

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="ricardo", description="write something to the bot...")
async def ricardo(ctx, *, message: str):
    sent_message = await ctx.respond("Processing answer...")
    if ctx.author.id in request_tasks:
        request_tasks[ctx.author.id].cancel()

    request_tasks[ctx.author.id] = asyncio.create_task(request(sent_message,message))

async def request(sent_message,message):
    try:
        await sent_message.edit(content="Gathering answer...")
        ollama_api = OllamaAPI()
        prompt = OllamaPrompt(model="gemma:2b", prompt=message, stream=False)
        response = await ollama_api.prompt(prompt)
        await sent_message.edit(content=response)
    except Exception as e:
        await sent_message.edit(content=f"An error occurred: {e}")

bot.run('MTIyNTUzNDA4NzA5NjMwMzczNw.G5IqLT.jqg-qLuK4E0TmpqjnQ_BV-nl6VLJ2bNT8t4Qbc')
