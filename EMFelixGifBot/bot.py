import discord
import asyncio
import urllib.request, json
import re

from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix='!', description='None')

regex = re.compile("(hi|what's up|yo|hey|hello) felix", re.IGNORECASE)
getgif = re.compile("felix gif ", re.IGNORECASE)


key = "Your key here"
botauth2 = "auth2 for discord bot"

@bot.command(pass_context=True)
async def message_me():
	print("test")

# an example python version of the live stream
# https://www.youtube.com/watch?v=tqT3O0S38gY&t=617s
@bot.event
async def on_message(message):
	if regex.match(message.content):
		await bot.send_message(message.channel, "hello")
	elif getgif.match(message.content):
		gif = message.content.split(" ")[2]

		await bot.send_message(message.channel,
			"Let me get that for you!")

		try:
			data = json.loads(urllib.request.urlopen(\
			"https://api.giphy.com/v1/gifs/search"\
			+ "?api_key=" + key\
			+ "&q=" + gif\
			+ "&limit=1"\
			+ "&offset=0"\
			+ "&rating=R"\
			+ "&lang=en").read())

			await bot.send_message(message.channel, data["data"][0]["embed_url"])
		except Exception as e:
			await bot.send_message(message.channel,
				"I'm sorry I couldn't find that")




bot.run("botauth2")

# keys in commit history have been regenerated.
