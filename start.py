import os
import dotenv

dotenv.load_dotenv('BOT_TOKEN.env')
dotenv.load_dotenv('DBL_TOKEN.env')

bot_token = os.getenv('BOT_TOKEN')
dbl_token = os.getenv('DBL_TOKEN')

if __name__ == '__main__':
    if not (bot_token):
        with open('BOT_TOKEN.env', 'w') as f:
            f.write('BOT_TOKEN=' + input('Enter bot token: '))

    if not (dbl_token):
        with open('DBL_TOKEN.env', 'w') as f:
            f.write('DBL_TOKEN' + input('Enter dbl token: '))

    print("You can start bot.py file now")
