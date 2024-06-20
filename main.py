import ptbot
from dotenv import load_dotenv
import os
from pytimeparse import parse


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def finish(chat_id, message, bot):
    bot.send_message(chat_id, "Время вышло!")


def notify_progress(secs_left, chat_id, message_id, message, bot):
    bot.update_message(chat_id, message_id, f'''Осталось {secs_left} секунд, 
    {render_progressbar(parse(message), secs_left)}''')

def wait(chat_id, message, bot):
    message_id = bot.send_message(chat_id, "Запускаю таймер")  
    bot.create_countdown(parse(message), notify_progress, chat_id=chat_id, message_id=message_id, message=message, bot=bot)
    bot.create_timer(parse(message), finish, chat_id=chat_id, message=message, bot=bot)

def main():
    load_dotenv()
    TG_TOKEN = os.environ['TELEGRAM_TOKEN']
    TG_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']
    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(wait, bot=bot)
    bot.run_bot()
    

if __name__ == '__main__':
    main()
 


