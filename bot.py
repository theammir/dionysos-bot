import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.presences = True

class HelpCommand(commands.HelpCommand):
	def __init__(self):
		super().__init__(command_attrs = {
				'name': 'хелп',
				'brief': 'Показывает это сообщение.',
				'aliases': ['help', 'меню', 'menu']
			})

	def format_command_aliases(self, command):
		if not (command.aliases):
			return

		return ', '.join(f'`{alias}`' for alias in command.aliases)

	async def send_bot_help(self, mapping):
		for key, value in mapping.items():
			mapping[key] = await self.filter_commands(value)

		embed = discord.Embed(colour = 0x289566, description = 'На территории барной стойки действует сухой закон, алкоголь не продаётся.',)
		value = []
		for cog, commands in mapping.items():
			commands = list(set(commands))
			for com in commands:
				value.append(f'`{self.context.prefix}{com.name}` - {self.format_command_aliases(com)}')

		embed.add_field(name = 'Список команд:', value = '\n'.join(value))
		embed.add_field(name = 'Сервер поддержки: ', value = '**https://discord.gg/A4NETzF**')

		await self.context.send(embed = embed)

def get_pre(bot, message):
	return ['a!', 'а!']

bot = commands.Bot(command_prefix = get_pre, intents = intents, status = discord.Status.dnd, activity = discord.Game(name = 'a!хелп'))
bot.help_command = HelpCommand()

@bot.event
async def on_ready():
	bot.load_extension('barcog')

with open('token.txt', 'r') as file:
	token = file.read()
bot.run(token)