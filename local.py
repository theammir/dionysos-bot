import tinydb

global RUSSIAN, ENGLISH
RUSSIAN = {
	'helpDesc': 'На территории барной стойки действует сухой закон, алкоголь не продаётся.',
	'nocog': 'Прочее',
	'support': 'Сервер поддержки: ',
	'invite': 'Перейдите по следующей ссылке, что-бы пригласить бота на ваш сервер: ',
	'vote': 'Перейдите по следующей ссылке, что-бы проголосовать за бота: ',
	'cogs': {'barcog': 'Барная стойка', 'snackcog': 'Закуски', 'foodcog': 'Основные блюда', 'topggcog': '🥳СОБЫТИЕ'},
	'novotes': 'У вас недостаточно голосов для заказа данного пункта меню. Обратитесь в `a!воут`.',
	'bug0': 'Привет, это Амир. Я вижу, что некоторым людям стало интересно, что из себя представляет мой бот, но, к сожалению, пока-что шампанское не доступно по техническим причинам. Простите, если уже успели почувствовать себя обманутыми. :)',
	'botS': 'Настройки бота',
	'switch': 'Switch language',
	'adminWarn': 'Вы должны обладать правами администратора или правами управления сервером для данного действия.',
	'noAliases': "нет других названий",
	'aliasWarn': "А вы знали?: Вы можете использовать команды бота на обоих языках вне зависимости от установленного на сервере.",
	'sCon': 'Успешно изменён язык бота на сервере.',
	'con': 'Применить',
	'fbBrief': 'Это команда для отправки отзыва разработчику бота в личные сообщения. Вы можете использовать её раз в час - просто напишите своё сообщение через пробел после команды.',
	'onCd': 'Данную команду можно использовать {0} раз(а) в {1}. Попробуйте ещё раз через **{2}**.'
}

ENGLISH = {
	'helpDesc': 'There\'s no-alcohol law in our bar. We don\'t sell anything like that.',
	'nocog': 'Other',
	'support': 'Support server: ',
	'invite': 'Use this link to invite the bot to your server: ',
	'vote': 'Use this link to vote for the bot: ',
	'cogs': {'barcog': 'The bar', 'snackcog': 'Snacks', 'foodcog': 'Main dishes', 'topggcog': '🥳EVENT'},
	'novotes': 'You don\'t have enough vote points to order this menu item. Go for `a!vote`',
	'bug0': 'Hi, I am Amir. I see you are interested in my bot and its functions but I have to say event menu doesn\'t work yet. I\'m working on a solution. Sorry if you felt like I lied to you :)',
	'botS': 'Bot settings',
	'switch': 'Сменить язык',
	'adminWarn': 'You require admin or manage server permissions to do this.',
	'noAliases': "no aliases",
	'aliasWarn': "TIP: You know you don't have to copy russian command name to actually use it, right? Just use english 'a' letter followed by '!' and type any english alias that is provided above.",
	'sCon': 'Successfully changed server\'s bot language',
	'con': 'Confirm',
	'fbBrief': 'This is a command for giving your feedback to bot developer. You can use it 1time/hour. Just write your feedback right after command\'s name, followed by space. :)',
	'onCd': 'You can use this command {0} times in {1}. Try again in **{2}**.'
}

def get_localized(context):
	if (context.guild):
		query = tinydb.Query()
		guild_settings = tinydb.TinyDB('guild_settings.json')
		search = guild_settings.search(query.guild == context.guild.id)
		if (search):
			search = search[0]
			return RUSSIAN if search['isRU'] else ENGLISH
		else:
			return ENGLISH
	else:
		return ENGLISH

def change_locs(guild):
	gid = guild.id
	query = tinydb.Query()
	guild_settings = tinydb.TinyDB('guild_settings.json')
	search = guild_settings.search(query.guild == gid)
	if (search):
		search = search[0]
		if (search['isRU']):
			guild_settings.update({'isRU': False}, query.guild == gid)
		else:
			guild_settings.update({'isRU': True}, query.guild == gid)
	else:
		guild_settings.insert({'guild': gid, 'isRU': True})

	return True

def is_ru(guild):
	if (guild):
		gid = guild.id
		query = tinydb.Query()
		guild_settings = tinydb.TinyDB('guild_settings.json')
		search = guild_settings.search(query.guild == gid)
		if search:
			search = search[0]
			if (search['isRU']):
				return True
	return False
