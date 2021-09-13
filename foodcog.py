import discord
import random
import menu
from discord.ext import commands

class FoodCog(commands.Cog, name = '{foodcog}'):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name = 'пицца', aliases = ['pizza'])
	async def order_pizza(self, ctx):
		embed = discord.Embed(
				colour = 0x289566,
				description = random.choice(menu.ORDER_PHRASES)
			)
		embed.set_image(url = random.choice(menu.PIZZA_PICS))
		embed.set_footer(text = random.choice(menu.PIZZA_FACTS))

		await ctx.send(embed = embed)

	@commands.command(name = 'пельмени', aliases = ['pelmeni, dumplings'])
	async def order_pelmeni(self, ctx):
		embed = discord.Embed(
				colour = 0x289566,
				description = random.choice(menu.ORDER_PHRASES)
			)
		embed.set_image(url = random.choice(menu.PELMENI_PICS))
		embed.set_footer(text = random.choice(menu.PELMENI_FACTS))

		await ctx.send(embed = embed)


def setup(bot):
	bot.add_cog(FoodCog(bot))