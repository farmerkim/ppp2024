import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
 
token = "7468734547:AAF9VHlv9VXbNvnlZfykVj5GaW34bWNqoQ4"
id = "7078646539"
 
bot = telegram.Bot(token)
info_message = "자신의 MBTI를 입력해주세요(알파벳 전체 대문자/전체 소문자 식으로 알려드릴게요)"
bot.sendMessage(chat_id=id, text=info_message)

updater = Updater(token=token, use_context=info_message)
dispatcher = updater.dispatcher
updater.start_polling()
 

def handler(update, context):
    user_text = update.message.text
    if user_text in ["INTJ", "intj"]:
        bot.send_message(chat_id=id, text="https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-intj")
    elif user_text in ["INTP", "intp"]:
        bot.send_message(chat_id=id, text="https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-intp")
    elif user_text in ["ENTJ", "entj"]:
        bot.send_message(chat_id=id, text="https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-entj")
    elif user_text in ["ENTP", "entp"]:
        bot.send_message(chat_id=id, text="https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-entp")
    elif user_text in ["INFJ", "infj"]:
        bot.send_message(chat_id=id, text="https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-infj")
    elif user_text in ["INFP", "infp"]:
        bot.send_message(chat_id=id, text="https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-infp")
    elif user_text in ["ENFJ", "enfj"]:
        bot.send_message(chat_id=id, text="https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-enfj")
    elif user_text in ["ENFP", "enfp"]:
        bot.send_message(chat_id=id, text="https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-enfp")
    elif user_text in ["ISTJ", "istj"]:
        bot.send_message(chat_id=id, text="https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-istj")
    elif user_text in ["ISFJ", "isfj"]:
        bot.send_message(chat_id=id, text="https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-isfj")
    elif user_text in ["ESTJ", "estj"]:
        bot.send_message(chat_id=id, text="https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-estj")
    elif user_text in ["ESFJ", "esfj"]:
        bot.send_message(chat_id=id, text="https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-esfj")
    elif user_text in ["ISTP", "istp"]:
        bot.send_message(chat_id=id, text="https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-istp")
    elif user_text in ["ISFP", "isfp"]:
        bot.send_message(chat_id=id, text="https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-isfp")
    elif user_text in ["ESTP", "estp"]:
        bot.send_message(chat_id=id, text="https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-estp")
    elif user_text in ["ESFP", "esfp"]:
        bot.send_message(chat_id=id, text="https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-esfp")
    else:
        bot.send_message(chat_id=id, text="초면인데 이러시면 곤란합니다. 그냥 알려주세요")

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
