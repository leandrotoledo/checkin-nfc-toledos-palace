#!/usr/bin/env python
import telegram

CHAT_ID = -28767330
BOT = telegram.Bot('120405045:AAEAQ3EcfZ3NztkUbOkMOwCxXdDikEW1VZE')

class ToledosPalaceBot(object):
   @staticmethod
   def checkIn(name):
      BOT.sendMessage(CHAT_ID, "%s fez check-in em Toledo's Palace!" % name)
