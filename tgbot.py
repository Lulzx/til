#!/usr/bin/env python3
# -*- coding: utf-3 -*-
import os
import sys
import logging

from github import Github
from config import access_token, telegram_token
from tomd import Tomd
from html import unescape
from bbcode import render_html
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)

g = Github(access_token)
repo = g.get_repo("Lulzx/til")

def start(update, context):
	update.message.reply_text('what do you need? 🤔')


def parse_bbcode(message_text, length, entities, urled=False):
	if message_text is None:
		return None
	message_text = length*"^" + message_text
	if not sys.maxunicode == 0xffff:
		message_text = message_text.encode('utf-16-le')

	bbcode_text = ''
	last_offset = 1

	for entity, text in sorted(entities.items(), key=(lambda item: item[0].offset)):

		if entity.type == 'text_link':
			if text == entity.url:
				insert = str(entity.url)
			else:
				insert = '<a href="{}">{}</a>'.format(entity.url, text)
		elif entity.type == 'mention':
			insert = '<a href="https://t.me/{0}">{1}</a>'.format(text.strip('@'),text)
		elif entity.type == 'url' and urled:
			insert = '<a href="{0}">{0}</a>'.format(text)
		elif entity.type == 'bold':
			insert = '<b>' + text + '</b>'
		elif entity.type == 'italic':
			insert = '<i>' + text + '</i>'
		elif entity.type == 'underline':
			insert = '<u>' + text + '</u>'
		elif entity.type == 'strikethrough':
			insert = '<s>' + text + '</s>'
		elif entity.type == 'code':
			insert = '<code>' + text + '</code>'
		elif entity.type == 'pre':
			insert = '<pre>' + text + '</pre>'
		else:
			insert = text
		if sys.maxunicode == 0xffff:
			bbcode_text += message_text[last_offset:entity.offset] + insert
		else:
			bbcode_text += message_text[last_offset * 2:entity.offset * 2].decode('utf-16-le') + insert

		last_offset = entity.offset + entity.length

	if sys.maxunicode == 0xffff:
		bbcode_text += message_text[last_offset:]
	else:
		bbcode_text += message_text[last_offset * 2:].decode('utf-16-le')
	return bbcode_text


def post(update, context):
	if update.channel_post:
		if update.channel_post.chat.username == "rememberbox":
			text = update.channel_post.text
			entities = update.channel_post.parse_entities()
			first, *others = text.splitlines()
			length = len(first) + 2
			if first.startswith('👉'):
				path = first[2:]
				first = path.split('/')[-1] # remove trigger emoji
				filename = path.lower().replace(' ', '-') + ".md"
				rest = parse_bbcode("\n".join(others), length, entities, urled=True)
				html = "<p>" + unescape(render_html(rest)) + "</p>"
				context.bot.send_message(chat_id=691609650, text=html)
				rest = Tomd(html).markdown[length + 1:].replace('<br />', '\n')
				content = "# " + first + "\n\n" + rest
				try:
					commit = repo.create_file(filename, "automated post from telegram channel", content, branch="master")
					sha = getattr(commit['commit'], 'sha')
					url = "https://github.com/Lulzx/til/commit/" + sha
					context.bot.send_message(chat_id=691609650, text="new addition in TIL repository: {}".format(url))
				except:
					pass


def error(update, context):
	logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
	try:
		TOKEN = telegram_token # sys.argv[1]
	except IndexError:
		TOKEN = os.environ.get("TOKEN")
	updater = Updater(TOKEN, use_context=True)
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(MessageHandler(Filters.text, post))
	dp.add_error_handler(error)
	updater.start_polling()
	logger.info("Ready to rock..!")
	updater.idle()


if __name__ == '__main__':
	main()
