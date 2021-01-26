import discord
import menu
import random
from discord.ext import commands

class BarCog(commands.Cog, name = 'Барная стойка'):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name = 'вода', aliases = ['water'])
	async def order_water(self, ctx):
		embed = discord.Embed(
				colour = 0x289566,
				description = random.choice(menu.ORDER_PHRASES)
			)
		embed.set_image(url = random.choice(menu.WATER_PICS))
		embed.set_footer(text = random.choice(menu.WATER_FACTS))

		await ctx.send(embed = embed)

	@commands.command(name = 'кефир', aliases = ['kefir'])
	async def order_kefir(self, ctx):
		embed = discord.Embed(
				colour = 0x289566,
				description = random.choice(menu.ORDER_PHRASES)
			)
		embed.set_image(url = random.choice(menu.KEFIR_PICS))
		embed.set_footer(text = random.choice(menu.KEFIR_FACTS))

		await ctx.send(embed = embed)

	@commands.command(name = 'кола', aliases = ['кока-кола', 'cola', 'coca', 'coca-cola', 'кока'])
	async def order_cola(self, ctx):
		embed = discord.Embed(
				colour = 0x289566,
				description = random.choice(menu.ORDER_PHRASES)
			)
		embed.set_image(url = random.choice(menu.COLA_PICS))
		embed.set_footer(text = random.choice(menu.COLA_FACTS))

		await ctx.send(embed = embed)

	@commands.command(name = 'квас', aliases = ['kvas'])
	async def order_kvas(self, ctx):
		embed = discord.Embed(
				colour = 0x289566,
				description = random.choice(menu.ORDER_PHRASES)
			)
		embed.set_image(url = random.choice(menu.KVAS_PICS))
		embed.set_footer(text = random.choice(menu.KVAS_FACTS))

		await ctx.send(embed = embed)

	@commands.command(name = 'молоко', aliases = ['milk'])
	async def order_milk(self, ctx):
		embed = discord.Embed(
				colour = 0x289566,
				description = random.choice(menu.ORDER_PHRASES)
			)
		embed.set_image(url = random.choice(menu.MILK_PICS))
		embed.set_footer(text = random.choice(menu.MILK_FACTS))

		await ctx.send(embed = embed)

	@commands.command(name = 'чай', aliases = ['tea'])
	async def order_tea(self, ctx):
		embed = discord.Embed(
				colour = 0x289566,
				description = random.choice(menu.ORDER_PHRASES)
			)
		embed.set_image(url = random.choice(menu.TEA_PICS))
		embed.set_footer(text = random.choice(menu.TEA_FACTS))

		await ctx.send(embed = embed)

	@commands.command(name = 'коктейль', aliases = ['coctail', 'cocktail'])
	async def order_cocktail(self, ctx):
		embed = discord.Embed(
				colour = 0x289566,
				description = random.choice(menu.ORDER_PHRASES)
			)
		embed.set_image(url = random.choice(menu.COCKTAIL_PICS))
		embed.set_footer(text = random.choice(menu.COCKTAIL_FACTS))

		await ctx.send(embed = embed)

	@commands.command(name = 'кофе', aliases = ['cofee', 'coffee'])
	async def order_coffee(self, ctx):
		embed = discord.Embed(
				colour = 0x289566,
				description = random.choice(menu.ORDER_PHRASES)
			)
		embed.set_image(url = random.choice(menu.COFFEE_PICS))
		embed.set_footer(text = random.choice(menu.COFFEE_FACTS))

		await ctx.send(embed = embed)

	@commands.command(name = 'милкшейк', aliases = ['shake', 'шейк', 'milkshake'])
	async def order_milkshake(self, ctx):
		embed = discord.Embed(
				colour = 0x289566,
				description = random.choice(menu.ORDER_PHRASES)
			)
		embed.set_image(url = random.choice(menu.MILKSHAKE_PICS))
		embed.set_footer(text = random.choice(menu.MILKSHAKE_FACTS))

		await ctx.send(embed = embed)

	@commands.command(name = 'сок', aliases = ['juice'])
	async def order_juice(self, ctx):
		embed = discord.Embed(
				colour = 0x289566,
				description = random.choice(menu.ORDER_PHRASES)
			)
		embed.set_image(url = random.choice(menu.JUICE_PICS))
		embed.set_footer(text = random.choice(menu.JUICE_FACTS))

		await ctx.send(embed = embed)

	@commands.command(name = 'кисель', aliases = ['jelly'])
	async def order_jelly(self, ctx):
		embed = discord.Embed(
				colour = 0x289566,
				description = random.choice(menu.ORDER_PHRASES)
			)
		embed.set_image(url = random.choice(menu.JELLY_PICS))
		embed.set_footer(text = random.choice(menu.JELLY_FACTS))

		await ctx.send(embed = embed)

	@commands.command(name = 'какао', aliases = ['cocoa'])
	async def order_cocoa(self, ctx):
		embed = discord.Embed(
				colour = 0x289566,
				description = random.choice(menu.ORDER_PHRASES)
			)
		embed.set_image(url = random.choice(menu.COCOA_PICS))
		embed.set_footer(text = random.choice(menu.COCOA_FACTS))

		await ctx.send(embed = embed)

	@commands.command(name = 'компот', aliases = ['compot'])
	async def order_compot(self, ctx):
		embed = discord.Embed(
				colour = 0x289566,
				description = random.choice(menu.ORDER_PHRASES)
			)
		embed.set_image(url = random.choice(menu.COMPOT_PICS))
		embed.set_footer(text = random.choice(menu.COMPOT_FACTS))

		await ctx.send(embed = embed)

def setup(bot):
	bot.add_cog(BarCog(bot))