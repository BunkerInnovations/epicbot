import ircutil
import random
from datetime import datetime
import requests
import os
from lxml.html import fromstring
import re
import time

# IRC Config
bot = ircutil.Connection()
bot.server = "127.0.0.1:6667"
bot.nick = "epicbot"
bot.hostname = "epicbot"
bot.servername = "epicbot"
bot.ident = "epicbot"


random.seed(datetime.now().second)

@bot.trigger("WELCOME")
def autojoin(event):
    print("Bot is running")
    bot.join('#general-shitcord')
    
@bot.trigger(lambda event: event.MSG and event.msg.startswith("$hi"))
def hi(event):
    bot.msg(event.chat, f'{event.nick}: Hey!')

@bot.trigger(lambda event: event.MSG and event.msg.startswith("$join"))
def join(event):
    if len(event.msg.split()) < 2:
        bot.msg(event.chat, f"Missing channel")
    elif not event.msg.split()[1].startswith("#"):      
        bot.msg(event.chat, f"Please specify a valid channel (starting with #)")
    else:
        bot.msg(event.chat, f'Joining {event.msg.split()[1]}')
        bot.join(event.msg.split()[1])

@bot.trigger(lambda event: event.MSG and event.msg.startswith("$dice"))
def dice(event):
    bot.msg(event.chat, f'Rolling the dice... {random.randint(1,6)}')

@bot.trigger(lambda event: event.MSG and event.msg.startswith("$uwuify"))
def uwuify(event):   
    if len(event.msg.split()) < 2:
        bot.msg(event.chat, f"Missing string")
    else:
        str1 = " ".join(event.msg.split()[1:]).replace('r', 'w')
        bot.msg(event.chat, f"{str1.replace('l','w')}")

@bot.trigger(lambda event: event.MSG and event.msg.startswith("$crack"))
def crack(event):
    if len(event.msg.split()) < 2:
        bot.msg(event.chat, f"Please specify who to crack!")
    else:
        name = event.msg.split()[1]
        emails = ["ilovepokimane@gamil.com", "idolmaster1337@gmail.com", "trole404@trole.net", "ducomerdeintoschiebe@waifu.club",
                  "theabbixaretheprogrammer@cock.li", "jetztgaslos@gmx.de", "maxiloveshamradio1357@kampfwagen.de",
                  "stallmanhasanicebeard@yes.com", "imahipster@riseup.net", "plsdontsellmydata@facebook.com", "TimCooks@gmail.com", "BillGates@icloud.com", "idolmaster696969420@panzerimfwagen.bruh"]
        passwords = ["isimpforstallman", "panzermaster42", "meinefrauistmeineschwester", "ahyes", "rnbubuntuuser", "********",
                     "etorliebejunges1337404", "epsteindidnothingwrong", "cremedelacremeducomerde", "ilovefacebook!", "revoxsux", "sosussy", "revoxsus"]
    
        bot.msg(event.chat, f"Cracking into {name}'s computer...")   
        bot.msg(event.chat, f"Got email {random.choice(emails)}...")
        bot.msg(event.chat, f"Got password {random.choice(passwords)}...")    
        bot.msg(event.chat, f"Sending data to government... crack done!")

@bot.trigger(lambda event: event.MSG and event.msg.startswith("$etor"))
def etor(event):
    bot.msg(event.chat, f"etor liebt junges!!")

@bot.trigger(lambda event: event.MSG and event.msg.startswith("$cancel"))
def cancel(event):
    if len(event.msg.split()) < 2:
        bot.msg(event.chat, f"Please specify who to cancel!")
    else:
        bot.msg(event.chat, f"{event.msg.split()[1]} got cancelled...")

@bot.trigger(lambda event: event.MSG and event.msg.startswith("$choose"))
def choose(event):  
    if not "," in event.msg:
        bot.msg(event.chat, f"Please send multiple choices separated by a comma (',')")
    else:
        bot.msg(event.chat, f"I choose {random.choice(event.msg.split(',')[1:])}")

@bot.trigger(lambda event: event.MSG and event.msg.startswith("$get"))
def get(event):  
    if len(event.msg.split()) < 2:
        bot.msg(event.chat, f"Missing URL")
    else:
        response = requests.get(event.msg.split()[1])
        response_post = requests.post("https://envs.sh", files={'file' : response.text.encode()})
        bot.msg(event.chat, event.nick + ": " + response_post.text)
        
@bot.trigger(lambda event: event.MSG and not event.msg.startswith("$get"))
def title(event):
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', event.msg)
    for url in urls:
        response = requests.get(url)
        tree = fromstring(response.content)
        bot.msg(event.chat,tree.findtext('.//title'))
        
@bot.trigger(lambda event: event.MSG and event.msg.startswith("$radio"))
def radio(event):
        response = requests.get("http://phrl42.ydns.eu:8000/")
        tree = fromstring(response.content)
        bot.msg(event.chat, "Currently playing: " + tree.xpath("/html/body/div[2]/div[2]/table/tbody/tr[9]/td[2]")[0].text)

@bot.trigger(lambda event: event.MSG and event.msg.startswith("$price"))
def price(event):
        if len(event.msg.split()) < 2:
            bot.msg(event.chat, f"Missing cryptocurrency name")
        else:
            response = requests.get("https://rate.sx/1" + event.msg.split()[1])
            if response.text.split()[0] != "ERROR":
                bot.msg(event.chat, f"Price for 1 {event.msg.split()[1]}: {response.text.split()[0]}$")
            else:
                bot.msg(event.chat, "An error occured, maybe you made a typo?")

@bot.trigger(lambda event: event.MSG and event.msg.startswith("$rnb"))
def rnb(event):
    bot.msg(event.chat, f"rnb torrenting waifu material...")

@bot.trigger(lambda event: event.MSG and event.msg.startswith("$phrl"))
def phrl(event):
    bot.msg(event.chat, f"phrl loves otaku culture!")


@bot.trigger(lambda event: event.MSG and event.msg.startswith("$furim"))
def furim(event):
     bot.msg(event.chat, f"Are the Abbix the programmer of the linus kernal? xD Imma duco merde into schiebe")

@bot.trigger(lambda event: event.MSG and event.msg.startswith("$abbix"))
def abbix(event):
     bot.msg(event.chat, f"haha noob, I use scheme to take over the world...")
        
@bot.trigger(lambda event: event.MSG and event.msg.startswith("$idotmaster1"))
def idotmaster1(event):
    bot.msg(event.chat, f"haha idolmaster XDXDXDXD so funni!!!!")

                
bot.connect()
