# File: bot.py
# By: Senior Duckie.
# Date: Sep 9.
# Purpose: A driver for the hangman solver. (4 letter words are hard :( )

import discord
import asyncio
import hmai.hmai as hm

from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix='plant ', description='None')
client = discord.Client()
server = discord.Server

@bot.event
async def on_ready():
	print("goooood to go.")

config = json.load(open("../config.json", "r"))

POSSIBLELETTER = 'abcdefghijklmnopqrstuvwxyz-'
channel = ""

hmbot = None

wins = 0
losses = 0

@bot.event
async def on_message(message):
	global hmbot
	global wins
	global losses

	await bot.process_commands(message)
	if message.channel.id != channel:
		print("wrong channel %s != %s" % (channel, message.channel.id))
		return

	for emb in message.embeds:
		if emb["title"] == "Duckie hangman":
			if emb["description"][0] != "T":
				hmbot.nextData(emb["description"].split("\n")[0].split(" ")[3:-1])
				hmbot.calcProb()
				hmbot.lightprint()

				await bot.send_message(message.channel, "~ letter " +\
					hmbot.getRecommended())
			else:
				hmbot = hm.Hangman(emb["description"].split("\n")[1].split(" ")[3:-1])
				hmbot.calcProb()
				hmbot.lightprint()

				await bot.send_message(message.channel, "~ letter " +\
					hmbot.getRecommended())
	if message.author.id == "479873253004017664":
		if "Nice" in message.content:
			wins = wins + 1
			await bot.send_message(message.channel, "~ hangman")
			print("CURRENT SCORE %d / %d" % (wins, losses))
		elif "You've" in message.content:
			losses = losses + 1
			await bot.send_message(message.channel, "~ hangman")
			print("CURRENT SCORE %d / %d" % (wins, losses))

bot.run(config["bot_key"])
