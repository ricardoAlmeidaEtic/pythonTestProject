import discord
import asyncio
import aiohttp
from clients import OllamaAPI
from models import OllamaPrompt

client = discord.Bot()
ollamaAPI = OllamaAPI()

@client.event
async def on_ready():
    print('Bot is connected!!')

@client.slash_command(name="ask", description="write something to the bot...")
async def ask(ctx, *, question: str):
    try:
        await ctx.defer()
        asyncio.run(await request(ctx,question))
    except Exception as e:
        print("An interaction error occurred:", e)
        # Log the error or notify the user appropriately
        await ctx.send("Sorry, there was an error processing your request. Please try again later.")

async def request(ctx,question):
    question_prompt = OllamaPrompt(prompt=question)
    response = await ollamaAPI.prompt(prompt=question_prompt)
    
    if not response.done:
        await ctx.send(":poop Oops! Unable to generate a response.")
    else:
        await ctx.send(response.response)

if __name__ == "__main__":
    client.run('MTIyNjk3NzY2OTgyMDk3MzA3OA.GvuZZX.lpIiyDax4ZUg0_weT93py0Oo9VieLXzRyYPZ6Y')
