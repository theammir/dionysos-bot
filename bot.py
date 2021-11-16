import discord
import topgg
import config
import os
import tinydb
import asyncio
import humanize, datetime
import start
import local
import sys
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.presences = True; intents.members = True

class HelpCommand(commands.HelpCommand):
	def __init__(self):
		super().__init__(command_attrs = {
				'name': 'хелп',
				'brief': 'Показывает это сообщение.',
				'aliases': ['help', 'меню', 'menu']
			})

	def format_command(self, command):
		name, aliases = command.name, command.aliases
		if aliases:
			aliases = sorted(aliases, reverse=True)
			if not local.is_ru(self.context.guild):
				name, aliases[-1] = aliases[-1], name
				aliases = sorted(aliases)
		else:
			aliases = local.get_localized(self.context)['noAliases']

		return f"`{self.context.prefix}{name}` - " + ', '.join([f"`{alias}`" for alias in aliases] if isinstance(aliases, list) else aliases)



	async def send_bot_help(self, mapping):
		locs = local.get_localized(self.context)
		jishaku = False
		for key, value in mapping.items():
			mapping[key] = await self.filter_commands(value)
			if (key):
				cog_names = locs['cogs']
				key.name = key.qualified_name.format_map(cog_names)

				if (key.qualified_name == 'Jishaku'):
					jishaku = key

		if (jishaku):
			del mapping[jishaku]

		embed = discord.Embed(colour = 0x289566, description = locs['helpDesc'])
		embed.set_footer(text=locs['aliasWarn'])

		for cog, commands in mapping.items():
			commands = list(set(commands))
			value = []
			for com in commands:
				value.append(self.format_command(com))
			embed.add_field(name = f'{cog.name if cog else locs["nocog"]}:', value = '\n'.join(value))
		embed.add_field(name = locs['support'], value = '**https://discord.gg/A4NETzF**')

		await self.context.send(embed = embed)

def get_pre(bot, message):
	return ['a!', 'а!', 'A!', 'А!']

bot = commands.Bot(command_prefix = get_pre, intents = intents, status = discord.Status.dnd, activity = discord.Game(name = 'a!help | a!хелп'))
bot.help_command = HelpCommand()

bot.topggpy = topgg.DBLClient(bot, start.dbl_token)

@tasks.loop(minutes=30)
async def post_guild_count():
	await bot.topggpy.post_guild_count()

@bot.event
async def on_ready():
	curr_dir = os.listdir()
	for file in curr_dir:
		if (file.endswith('cog.py')):
			try:
				bot.load_extension(file[:-3])
			except Exception as e:
				print(f'[{file.upper()}]: LOAD FAIL! {type(e).__name__}: {e}')
			else:
				print(f'[{file.upper()}]: LOAD SUCCESS')

	bot.load_extension('jishaku')

@bot.event
async def on_guild_join(guild):
	if guild.name is None:
		return
	channel = bot.get_channel(config.LOG_CHANNEL)
	await channel.send(config.JOIN_MSG.format(guild = guild, count = len(bot.guilds)))

@bot.event
async def on_guild_remove(guild):
	if guild.name is None:
		return # Prevents some sudden messages
	channel = bot.get_channel(config.LOG_CHANNEL)
	await channel.send(config.LEAVE_MSG.format(guild = guild, count = len(bot.guilds)))

@bot.event
async def on_member_update(before, after):
	channel = bot.get_channel(config.LOG_CHANNEL)
	if (after.id == bot.user.id):
		if (before.display_name != after.display_name):
			await channel.send(config.CHANGE_NICKNAME_MSG.format(guild = after.guild, new = after.display_name))

@bot.command(name = 'язык', aliases = ['language', 'lang'])
async def switch_lang(ctx):
	locs = local.get_localized(ctx)
	if not (ctx.author.guild_permissions.administrator or ctx.author.guild_permissions.manage_guild):
		msg = await ctx.send(locs["adminWarn"])
		await asyncio.sleep(3)
		await msg.delete()
		return

	result = local.change_locs(ctx.guild)
	locs = local.get_localized(ctx)
	if result:
		await ctx.send(locs['sCon'])

@bot.command(name = 'настройки', aliases = ['settings'])
async def settings(ctx):
	def generate_embed(ctx):
		locs = local.get_localized(ctx)
		embed = discord.Embed(
				colour = 0x289566,
				title = locs['botS'],
				description = f'**{locs["switch"]}:** 🔁'
			)
		embed.description += f'\n\n{locs["con"]}: ✅'
		return embed
	emb_msg = await ctx.send(embed = generate_embed(ctx))

	await emb_msg.add_reaction('🔁')
	await emb_msg.add_reaction('✅')

	while True:
		locs = local.get_localized(ctx)
		embed = generate_embed(ctx)

		try:
			reaction, user = await bot.wait_for('reaction_add', timeout = 15.0, check = lambda rea, usr: str(rea) in '🔁✅' and usr == ctx.message.author and rea.message == emb_msg)
		except asyncio.TimeoutError:
			break



		if (str(reaction) == '✅'):
			await emb_msg.delete()
			await ctx.send(locs['sCon'])
			break

		if not (user.guild_permissions.administrator or user.guild_permissions.manage_guild):
			embed = generate_embed(ctx)
			embed.set_footer(text = f'❎ {locs["adminWarn"]}')
			await emb_msg.edit(embed = embed)

		else:
			if (str(reaction) == '🔁'):
				local.change_locs(ctx.guild)
				locs = local.get_localized(ctx)
				embed = generate_embed(ctx)

				embed.set_footer(text = f'✅ {locs["sCon"]}')
				await emb_msg.edit(embed = embed)


@bot.command(name = 'инвайт', aliases = ['invite'])
async def bot_invite(ctx):
	locs = local.get_localized(ctx)
	permissions = discord.Permissions(
			create_instant_invite = True,
			change_nickname = True,
			read_messages = True,
			send_messages = True,
			send_tts_messages = True,
			embed_links = True,
			attach_files = True,
			read_message_history = True,
			use_external_emojis = True,
			add_reactions = True
		)
	bot_id = bot.user.id
	await ctx.send(embed = discord.Embed(colour = 0x289566, description = f'{locs["invite"]}https://discord.com/api/oauth2/authorize?client_id={bot_id}&permissions={permissions.value}&scope=bot'))

@bot.command(name = 'воут', aliases = ['vote'])
async def dblvote(ctx):
	locs = local.get_localized(ctx)
	await ctx.send(embed = discord.Embed(colour = 0x289566, description = f'{locs["vote"]}https://top.gg/bot/{bot.user.id}/vote'))

@commands.cooldown(1, 60*60, commands.BucketType.user)
@bot.command(name = 'отзыв', aliases = ['feedback'])
async def give_feedback(ctx, *, feedback = ''):
	locs = local.get_localized(ctx)
	if (not feedback):
		await ctx.send(embed = discord.Embed(
				colour = 0x289566,
				description = locs['fbBrief']
			))
	else:
		owner = bot.get_user(343001477133893632)
		await owner.send(f'{ctx.author.name} ({ctx.author.id}): {feedback}')
		await ctx.send(embed = discord.Embed(
				colour = 0x289566,
				description = locs['sCon']
			))

@give_feedback.error
async def feedback_handler(ctx, error):
	locs = local.get_localized(ctx)
	if (local.is_ru(ctx.guild)):
		humanize.i18n.activate('ru_RU')
	else:
		humanize.i18n.deactivate()
	if (isinstance(error, commands.CommandOnCooldown)):
		await ctx.send(embed = discord.Embed(
				colour = 0xff5555,
				description = locs['onCd'].format(error.cooldown.rate,
					humanize.naturaldelta(datetime.timedelta(seconds = error.cooldown.per)),
					humanize.naturaldelta(datetime.timedelta(seconds = error.retry_after)))
			))

@bot.command(name = 'ответ', aliases = ['reply'], hidden = True)
async def reply(ctx, id, *, text):
	reply_user = bot.get_user(id)
	try:
		await reply_user.send(text)
	except discord.DiscordException as e:
		await ctx.send(type(e).__name__ + ': ' + e)

if ("--keep-alive" in sys.argv):
	import keep_alive
	keep_alive.keep_alive()
bot.run(start.bot_token)
