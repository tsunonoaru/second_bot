import os
from dotenv import load_dotenv
import ptbot
from pytimeparse import parse


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def reply(chat_id, text):
    answer = parse(text)
    message_id = bot.send_message(chat_id, "Запускаю таймер...")
    bot.create_countdown(answer, notify_progress, chat_id=chat_id, message_id=message_id, answer=answer)
    bot.create_timer(answer, last_message, chat_id=chat_id, message=text)


def notify_progress(secs_left, chat_id, message_id, answer):
    total_time = answer
    progress = render_progressbar(total_time,secs_left)
    message = f"{progress}\nОсталось {secs_left} секунд!"
    bot.update_message(chat_id, message_id, message)


def last_message(chat_id, message):
    bot.send_message(chat_id, "Время вышло")


if __name__ == "__main__":
    load_dotenv() 
    TG_TOKEN = os.environ['TG_TOKEN']
    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(reply)
    bot.run_bot()    
    


