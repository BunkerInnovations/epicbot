import ircutil
import random
from datetime import datetime
import requests
import os
from lxml.html import fromstring
import re

# IRC Config
bot = ircutil.Connection()
bot.server = "q6dncw3mcqi57ehai5euozx3ypcg5av36fgegjtngemux4iulddhuqid.onion:6667"
bot.nick = "epicbot"
bot.hostname = "epicbot"
bot.servername = "epicbot"
bot.ident = "epicbot"


random.seed(datetime.now().second)

@bot.trigger("WELCOME")
def autojoin(event):
    print("Bot is running")
    bot.join('#test')
    
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
        emails = ["ilovepokimane@gamil.com", "stallmanhasanicebeard@yes.com", "imahipster@riseup.net", "plsdontsellmydata@facebook.com"]
        passwords = ["isimpforstallman", "panzermaster42", "meinefrauistmeineschwester", "ahyes", "epsteindidnothingwrong"]
    
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
def cancel(event):  
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
bot.connect()