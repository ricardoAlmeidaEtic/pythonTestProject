import discord
from clients import OllamaAPI
from models import OllamaPrompt
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "ricardo", description = "write something to the bot...")
async def ricardo(ctx, *, message:str):
    ollamaAPI = OllamaAPI()
    await ctx.respond(await ollamaAPI.prompt(OllamaPrompt(prompt=message)))

bot.run('MTIyNTUzNDA4NzA5NjMwMzczNw.GS1hT9.U9YHcDAJa-0RhkjFexqwglgAofiBmsxUbDtntk')