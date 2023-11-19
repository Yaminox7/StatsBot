import discord
from discord.ext import commands, tasks
import time
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
token = os.getenv("TOKEN")

@bot.event
async def on_ready():
	print("Bot is ready!")

@bot.command()
async def ping(ctx):
	print("Message !")
	#print(ctx.author, "sent in", ctx.channel, ctx.message)
	start = time.monotonic()
	msg = await ctx.send("Pong🏓 !")
	end = 1000*(time.monotonic() - start)
	await msg.edit(content=f"Pong🏓 ! ({int(end)}ms)")
	
@bot.command(alias=["eval"])
async def evaluate(ctx, *, op):
	try:
		await ctx.send(f"{op} = {eval(op)}")
	except:
		await ctx.send("Error !")

bot.run(token)