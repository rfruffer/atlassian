from telegram import Bot
from telegram import Update
from telegram import ParseMode
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackQueryHandler
from telegram.utils.request import Request
import requests
from requests.auth import HTTPBasicAuth

import json

import allowusers
import inlinebuttons
import tables
from inlinebuttons import get_inline_keyboard
import jira
import auth

print ("Begining work...")
tables.createTables()

def log (str):
    r = open("log.txt", "r")
    read = r.read()
    text = read+'\n'
    text += '\n'.join(str)
    f = open("log.txt", "w")
    f.write(text)
    f.close()

def keyboard_callback_handler(update: Update, context: CallbackContext):
    """ Обработчик ВСЕХ кнопок со ВСЕХ клавиатур
    """
    query = update.callback_query
    data = query.data
    chat_id = update.effective_message.chat_id

    isApprove = data == inlinebuttons.Approve
    isEdit = data == inlinebuttons.Edit
    isProject1 = data == inlinebuttons.Project1
    isProject2 = data == inlinebuttons.Project2
    isProject3 = data == inlinebuttons.Project3
    isProject4 = data == inlinebuttons.Project4
    isProject5 = data == inlinebuttons.Project5
    isProject6 = data == inlinebuttons.Project6
    #isProject7 = data == inlinebuttons.Project7
    isSummaryAwaiting = tables.sql_getSummary(chat_id) == "Awaiting"
    isProjectAwaiting = tables.sql_getProject(chat_id) == "Awaiting"
    isProjectSelected = tables.sql_getProject(chat_id) == "Selected"

    if isApprove and isSummaryAwaiting:
        context.bot.edit_message_text(
            chat_id = chat_id,
            text='Напишите, под этим сообщением, *ТЕМУ* запроса',
            parse_mode=ParseMode.MARKDOWN,
            message_id=query.message.message_id
        )

    elif isApprove and not isSummaryAwaiting and isProjectAwaiting:
        context.bot.edit_message_text(
            chat_id = chat_id,
            text='Выберите проект из списка:',
            parse_mode=ParseMode.MARKDOWN,
            message_id=query.message.message_id,
            reply_markup=get_inline_keyboard(inlinebuttons.inline_projects)
        )
        tables.setProject("Selected",chat_id)
    elif isEdit and not isSummaryAwaiting and isProjectAwaiting:
        context.bot.edit_message_text(
            chat_id = chat_id,
            text='Напишите, под этим сообщением, *ТЕМУ* запроса',
            parse_mode=ParseMode.MARKDOWN,
            message_id=query.message.message_id
        )
        tables.setSummary("Awaiting",chat_id)
    elif isEdit and not isSummaryAwaiting and not isProjectAwaiting:
        context.bot.edit_message_text(
            chat_id = chat_id,
            text='Выберите проект из списка:',
            parse_mode=ParseMode.MARKDOWN,
            message_id=query.message.message_id,
            reply_markup=get_inline_keyboard(inlinebuttons.inline_projects)
        )
        tables.setProject("Selected",chat_id)
    elif isApprove and tables.sql_getTemp(chat_id) is not None:
        project = tables.sql_getTemp(chat_id)
        tables.setProject(project,chat_id)
        result = [
            "*Тема:*\n`%s`" %(tables.sql_getSummary(chat_id)),
            "---------",
            "*Описание:*\n`%s`" %(tables.sql_getDescription(chat_id)),
            "---------",
            "*Проект:*\n`%s`" %(tables.sql_getProject(chat_id)),
            ]
        context.bot.edit_message_text(
            chat_id = chat_id,
            text='*Настройки завершены*',
            parse_mode=ParseMode.MARKDOWN,
            message_id=query.message.message_id
        )
        context.bot.send_message(
            chat_id = chat_id,
            text='\n'.join(result),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_inline_keyboard(inlinebuttons.inline_create)
        )
    elif isProject1 and isProjectSelected:
        context.bot.edit_message_text(
            chat_id = chat_id,
            text='Выберите проект из списка:',
            parse_mode=ParseMode.MARKDOWN,
            message_id=query.message.message_id,
            reply_markup=get_inline_keyboard(inlinebuttons.inline_projects1)
        )
        tables.setTemp(jira.SUP,chat_id)
    elif isProject2 and isProjectSelected:
        context.bot.edit_message_text(
            chat_id = chat_id,
            text='Выберите проект из списка:',
            parse_mode=ParseMode.MARKDOWN,
            message_id=query.message.message_id,
            reply_markup=get_inline_keyboard(inlinebuttons.inline_projects2)
        )
        tables.setTemp(jira.SD,chat_id)
    elif isProject3 and isProjectSelected:
        context.bot.edit_message_text(
            chat_id = chat_id,
            text='Выберите проект из списка:',
            parse_mode=ParseMode.MARKDOWN,
            message_id=query.message.message_id,
            reply_markup=get_inline_keyboard(inlinebuttons.inline_projects3)
        )
        tables.setTemp(jira.NOTIFY,chat_id)
    elif isProject4 and isProjectSelected:
        context.bot.edit_message_text(
            chat_id = chat_id,
            text='Выберите проект из списка:',
            parse_mode=ParseMode.MARKDOWN,
            message_id=query.message.message_id,
            reply_markup=get_inline_keyboard(inlinebuttons.inline_projects4)
        )
        tables.setTemp(jira.INFRA,chat_id)
    elif isProject5 and isProjectSelected:
        context.bot.edit_message_text(
            chat_id = chat_id,
            text='Выберите проект из списка:',
            parse_mode=ParseMode.MARKDOWN,
            message_id=query.message.message_id,
            reply_markup=get_inline_keyboard(inlinebuttons.inline_projects5)
        )
        tables.setTemp(jira.QAT,chat_id)
    elif isProject6 and isProjectSelected:
        context.bot.edit_message_text(
            chat_id = chat_id,
            text='Выберите проект из списка:',
            parse_mode=ParseMode.MARKDOWN,
            message_id=query.message.message_id,
            reply_markup=get_inline_keyboard(inlinebuttons.inline_projects6)
        )
        tables.setTemp(jira.JIRA,chat_id)
    # elif isProject7 and isProjectSelected:
    #     context.bot.edit_message_text(
    #         chat_id = chat_id,
    #         text='Выберите проект из списка:',
    #         parse_mode=ParseMode.MARKDOWN,
    #         message_id=query.message.message_id,
    #         reply_markup=get_inline_keyboard(inlinebuttons.inline_projects7)
    #     )
    #     tables.setTemp(jira.JIRA,chat_id)

    elif data == inlinebuttons.Create:
        sum = tables.sql_getSummary(chat_id)
        dis = tables.sql_getDescription(chat_id)
        key = tables.sql_getProject(chat_id)
        prj = jira.mapProject[key]
        payload = jira.createIssue(sum, dis, prj, chat_id)
        response = requests.request(
            "POST",
            auth.url,
            data=payload,
            headers=auth.headers,
            auth=auth.auth
        )
        dict = str(response.text)
        dataobj = json.loads(dict)
        context.bot.edit_message_text(
            chat_id = chat_id,
            text="Запрос: https://atlassian.net/browse/%s" %(dataobj['key']),
            parse_mode=ParseMode.MARKDOWN,
            message_id=query.message.message_id
        )

def do_echo(update: Update, context: CallbackContext):
    text = update.message.text
    creator = update.message.chat.id
    loging = [
        "Date UDC +3: %s" %(update.message.date),
        "From: @%s" %(update.message.chat.username),
        "Forward message: %s" %(update.message.forward_from is not None),
        "Allow user: %s" %(creator in allowusers.allow),
        "-----------------------------"
    ]
    log (loging)
    isAllow = creator in allowusers.allow
    isForward = update.message.forward_date is not None

    if isForward and isAllow:
        message = [
            '*ТЕЛО* запроса:',
            '_%s_' %(text)
        ]
        context.bot.send_message(
            chat_id = creator,
            text = '\n'.join(message),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_inline_keyboard(inlinebuttons.inline_main)
        )
        tables.setReporter(creator)
        tables.setDescription(text, creator)
    elif  tables.sql_getSummary(creator) == "Awaiting" and not isForward and isAllow:
        tables.setSummary(text,creator)
        message = [
            '*ТЕМА* запроса:',
            '_%s_' %(text)
        ]
        context.bot.send_message(
            chat_id = creator,
            text = '\n'.join(message),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_inline_keyboard(inlinebuttons.inline_edit)
        )
    elif  tables.sql_getSummary(creator) != "Awaiting" and not isForward and isAllow:
        message = [
            '*ТЕЛО* запроса:',
            '_%s_' %(text)
        ]
        context.bot.send_message(
            chat_id = creator,
            text = '\n'.join(message),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_inline_keyboard(inlinebuttons.inline_main)
        )
        tables.setReporter(creator)
        tables.setDescription(text, creator)

def main():
    print ("Starting bot...")

    req = Request(
        connect_timeout=0.5,
        read_timeout=1.0,
    )
    bot = Bot(
        token=auth.token,
        request=req,
    )
    updater = Updater(
        bot=bot,
        use_context=True,
    )

    # Проверить что бот корректно подключился к Telegram API
    print ("---------------------------")

    # Навесить обработчики команд
    # start_handler = CommandHandler("start", do_start)
    message_handler = MessageHandler(Filters.text, do_echo)
    buttons_handler = CallbackQueryHandler(callback=keyboard_callback_handler)

    # updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)
    updater.dispatcher.add_handler(buttons_handler)

    # Начать бесконечную обработку входящих сообщений
    updater.start_polling()
    updater.idle()

    print ("Finished work...")

if __name__ == '__main__':
    main()
