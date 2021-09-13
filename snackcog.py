import discord
import menu
import random
from discord.ext import commands

class SnackCog(commands.Cog, name = '{snackcog}'):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name = 'парварда', aliases = ['parvarda'])
	async def order_parvarda(self, ctx):
		embed = discord.Embed(
				colour = 0x289566,
				description = random.choice(menu.ORDER_PHRASES)
			)
		embed.set_image(url = random.choice(menu.PARVARDA_PICS))
		embed.set_footer(text = random.choice(menu.PARVARDA_FACTS))

		await ctx.send(embed = embed)

	@commands.command(name = 'чипсы', aliases = ['chips', 'crisps'])
	async def order_chips(self, ctx):
		embed = discord.Embed(
				colour = 0x289566,
				description = random.choice(menu.ORDER_PHRASES)
			)
		embed.set_image(url = random.choice(menu.CHIPS_PICS))
		embed.set_footer(text = random.choice(menu.CHIPS_FACTS))

		await ctx.send(embed = embed)

	@commands.command(name = 'фрукты', aliases = ['fruits', 'фрукт', 'fruit'])
	async def order_fruits(self, ctx):
		embed = discord.Embed(
				colour = 0x289566,
				description = random.choice(menu.ORDER_PHRASES)
			)
		embed.set_image(url = random.choice(menu.FRUIT_PICS))
		embed.set_footer(text = random.choice(menu.FRUIT_FACTS))

		await ctx.send(embed = embed)


def setup(bot):
	bot.add_cog(SnackCog(bot))