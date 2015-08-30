#!/usr/bin/env python
import telegram

CHAT_ID = -28767330

class ToledosPalaceBot(object):
   def __init__(self):
      self.bot = telegram.Bot('120405045:AAEAQ3EcfZ3NztkUbOkMOwCxXdDikEW1VZE')

   def checkIn(self, name):
      self.bot.sendMessage(CHAT_ID, "%s fez check-in em Toledo's Palace!" % name)

bot = ToledosPalaceBot()
bot.checkIn('Rafael')
