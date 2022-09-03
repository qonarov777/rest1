from .models import Homepage
from django.db.models.signals import post_save
from django.dispatch import receiver
import asyncio
import telebot

@receiver(post_save, sender=Homepage)
def save_profile(sender, instance, **kwargs):

    bot = telebot.TeleBot("5756119752:AAF_IeFYEFtuL-0_UZQsZalM5M5OfKwt-0g")
    bot.send_message(5546120663, "Ma`lumot bazaga qoshildi...")
       