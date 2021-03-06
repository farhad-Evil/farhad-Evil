from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
import random
import time
import os
import tgcrypto
import pytz
import asyncio
import shutil
import datetime
import requests
import wikipedia
from bs4 import BeautifulSoup
from itsDB import *
from faker import Faker
from apscheduler.schedulers.asyncio import AsyncIOScheduler
SunOn = ["True"]


def hours(num1):
    font1 = {"0": "๐", "1": "๐", "2": "๐", "3": "๐", "4": "๐",
             "5": "๐", "6": "๐", "7": "๐", "8": "๐ ", "9": "๐ก"}
    font2 = {"0": "โช", "1": "โต", "2": "โถ", "3": "โท", "4": "โธ",
             "5": "โน", "6": "โบ", "7": "โป", "8": "โผ", "9": "โฝ"}
    font3 = {"0": "๐", "1": "๐", "2": "๐", "3": "๐", "4": "๐",
             "5": "๐", "6": "๐", "7": "๐", "8": "๐", "9": "๐"}
    font4 = {"0": "โ", "1": "โ", "2": "โ", "3": "โ", "4": "โ",
             "5": "โ", "6": "โ", "7": "โ", "8": "โ", "9": "โ"}

    font = random.choice([font1, font2, font3])
    listh = []
    for key in font.keys():
        if key == num1[0]:
            listh.append(font[key])
    for key in font.keys():
        if key == num1[1]:
            listh.append(font[key])
    for key in font.keys():
        if key == num1[3]:
            listh.append(font[key])
    for key in font.keys():
        if key == num1[4]:
            listh.append(font[key])

    listh.insert(2, ":")
    listh.insert(3, " ")
    listh.insert(2, " ")
    num = "".join(listh)
    return num


async def BioTime():
    if app.is_connected:
        now = datetime.datetime.now(pytz.timezone("Asia/Tehran"))
        time = now.strftime("%H:%M")
        await app.update_profile(first_name=f"-๐๐๐ซ๐ก๐๐ | {hours(time)}")
scheduler = AsyncIOScheduler()
scheduler.add_job(BioTime, "interval", minutes=1)
CryptoP = "โขโโโโโโโโงโโฆโโงโโโโโโโโข\n"
async def Crypto():
    global CryptoP
    r = requests.get("https://coinmarketcap.com/").text
    doc = BeautifulSoup(r , "html.parser")
    tbody = doc.tbody
    Crypto = tbody.contents
    price1 = {}
    for tr in Crypto[:10]:
        name , price = tr.contents[2:4]
        cname = name.p.string
        cprice = price.a.string
        price1[cname] = cprice
    for k,v in price1.items():
        CryptoP += f"**๐ ูุงู ุงุฑุฒ :  **{k}\n**๐ฐ ู?ูุช ุงุฑุฒ** : {v}\n"
        CryptoP += "\n"
scheduler.add_job(Crypto, "interval", minutes=1)

# async def proxy():
#     async for message in app.iter_history("@OneTapProxy" , limit = 5):
#         if message.text:
#          print(message.text)
#         else: continue
# scheduler.add_job(proxy, "interval", seconds=3)

movielist = []
async def imdb():
    r = requests.get("https://www.imdb.com/chart/moviemeter/").text
    r = BeautifulSoup(r , "html.parser")
    movies ={}
    moviesfinal = []
    mclass = r.tbody.contents[:20]
    t = mclass[5].find(class_="titleColumn")
    for mov in mclass[1::2]:
        movies[mov.find(class_="titleColumn").text.strip("\n")] = mov.find(class_="ratingColumn imdbRating").text.strip("\n")
    for k,v in movies.items():
        a = k.split("\n")
        if v == "":
            moviesfinal.append(f"ูุงู ู?ูู : {a[0]}\nุณุงู ุงูุชุดุงุฑ : {a[1]}\nุงูุช?ุงุฒ : ูุฏุงุฑุฏโ\n\n")
        elif v != "":
            moviesfinal.append(f"ูุงู ู?ูู : {a[0]}\nุณุงู ุงูุชุดุงุฑ : {a[1]}\nุงูุช?ุงุฒ : {v}\n\n")
    sr = "".join(moviesfinal)
    final = f"โ      โคโโโโโโข~โแฏฝโ~โขโโโโโโฅ\n{sr}"
    movielist.append(final)
scheduler.add_job(imdb, "interval", seconds=4)


async def SunTime():
    if "True" in SunOn:
        sun = {"12": "๐", "16": "๐", "17": "๐", "18": "๐", "19": "๐",
               "1": "๐", "5": "๐", "6": "๐", "7": "๐", "8": "๐"}
        now = datetime.datetime.now(pytz.timezone("Asia/Tehran"))
        time1 = now.strftime("%H")
        for k, v in sun.items():
            if time1 == k or (time1[1] == k and time1[0] == "0"):
                await app.update_profile(last_name=f"{v}")
                break
scheduler.add_job(SunTime, "interval", hours=1)


def cal(isit, nums):
    if isit[1] == "ุฌูุน":
        totaljam = 0
        for nums1 in nums:
            totaljam = totaljam + nums1
        return totaljam
    elif isit[1] == "ูููุง":
        totalmenha = 0
        for nums1 in nums:
            totalmenha = nums1 - totalmenha
        return totalmenha
    elif isit[1] == "ุถุฑุจ":
        totalzarb = 1
        for nums1 in nums:
            totalzarb *= nums1
        return totalzarb
    elif isit[1] == "ุชูุณ?ู":
        totaltaghsim = 1
        for nums1 in nums:
            totaltaghsim = nums1 // totaltaghsim
        return totaltaghsim


api_id = 7803291
api_hash = "17ca1383ad8095f3b921a5033093b0e6"
app = Client("cliBOT", api_id, api_hash)
listsafe = [383456888]
unsafegap = [-1001325979653, -1001508310212]
typinggap = [-1001381304652, -1001406922641, -1001376097909]
listenemy = []
# gapfosh = []
gapactive = ["!on"]
# mostchatsgap = [-1001406922641]
# mostchatspeople = {}
sathdl = {1: 1}
markread = []
markreadpv = []
markreadgap = []
logope = [383456888]
comment1 = [-1001577002797 ,-1001267606452 , -1001508310212 , -1001406922641 , -1001162088572] 

@app.on_message(filters.command("anime") & filters.group & filters.me)
async def anime(client, message):
    await message.reply(f"Anti Anime Fan Is Activating..")
    for nums in range(1, 6):
        await message.reply("โช๏ธ" * nums)
    await message.reply("Chat Cleared...โ๏ธ")


@app.on_message(filters.command("block", prefixes=None) & filters.me)
async def hello2(client, message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        fname = message.reply_to_message.from_user.first_name

        await message.edit(f"[{fname}](tg://user?id={user_id}) __Successfully Blocked !__๐")
        await app.block_user(user_id)
    else:
        user = message.text.split()
        await message.edit(f"{user[1]} __Successfully Blocked !__๐")
        await app.block_user(user[1][1::1])


@app.on_message(filters.command("unblock", prefixes=None) & filters.me)
async def hello2(client, message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        fname = message.reply_to_message.from_user.first_name

        await message.edit(f"[{fname}](tg://user?id={user_id}) __Successfully UnBlocked !__๐")
        await app.unblock_user(user_id)
    else:
        user = message.text.split()
        await message.edit(f"{user[1]} __Successfully UnBocked !__๐")
        await app.unblock_user(user[1][1::1])


@app.on_message(filters.command("spam", prefixes=None) & filters.me)
async def spam(client, message):
    await message.delete(message.message_id)
    tedad = message.text.split()
    spamtext = tedad[2::1]
    spamtext = " ".join(spamtext)
    for num in range(int(tedad[1])):
        await app.send_message(message.chat.id, spamtext)


@app.on_message(filters.regex("^[Pp]ing$") & filters.me)
async def spam(client, message):
    str1 = ["๐ต", "๐ต", "๐ต", "๐ต", "๐ต"]
    start = time.time()
    for i in range(len(str1)):
        str1.pop(i)
        str1.insert(i, "๐ด")
        str2 = "".join(str1)
        await app.edit_message_text(message.chat.id, message.message_id, str2)
        str1.pop(i)
        str1.insert(i, "๐ต")
    end = time.time()
    await message.edit(f"**Time Elapsed : {round(end - start , 2)} s**")


@app.on_message(filters.regex("^[Cc]art$") & filters.me)
async def spam(client, message):
    await message.edit_text("**๐ณ ```6037 9981 1315 4701```**\n       __Name__ : ูุฑูุงุฏ ุจุงูุฑ?")


@app.on_message(filters.command("๐๐", prefixes=None) & filters.me)
async def spam(client, message):
    await message.edit("๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐\n๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐\n๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐\n๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐")


@app.on_message(filters.regex("^[Ss]unOff$") & filters.me)
async def spam(client, message):
    await message.edit_text("**Sun Show Is Off Now**")
    SunOn.clear()
    await app.update_profile(last_name="")


@app.on_message(filters.regex("^[Ss]unOn$") & filters.me)
async def spam(client, message):
    await message.edit_text("**Sun Show Is On Now**")
    SunOn.append("True")


@app.on_message(filters.command("6sec", prefixes=None) & filters.me)
async def spam(client, message):
    sec = ["๐", "๐", "๐", "๐", "๐", "๐"]
    for chars in sec:
        await message.edit(chars)
        time.sleep(1)
    await message.edit("๐ ุชูุงู ๐")


@app.on_message(filters.command("12sec", prefixes=None) & filters.me)
async def spam(client, message):
    sec = ["๐", "๐", "๐", "๐", "๐", "๐", "๐", "๐", "๐", "๐", "๐", "๐"]
    for chars in sec:
        await message.edit(chars)
        time.sleep(1)
    await message.edit("๐ ุชูุงู ๐")


@app.on_message(filters.regex(r"^[Mm]arkread") & filters.me)
async def hello1(client, message):
    text = message.text.lower()
    if text == "markread":
        markreadgap.append(message.chat.id)
        await message.delete(message.message_id)
    elif text == "markread off":
        await message.edit("**Mark Read Is Off Now **")
        markread.clear()
    elif text == "markread on":
        await message.edit("**Mark Read Is On Now** ")
        markread.append("t")
    elif text == "markreadpv on":
        await message.edit("**Mark Read Pv Is On Now **")
        markreadpv.append("t")
    elif text == "markreadpv off":
        markreadpv.clear()
        await message.edit("**Mark Read Pv Is Off Now **")


@app.on_message(filters.command("get", prefixes="!") & filters.me)
async def spam(client, message):
    chattitle = await app.get_chat(message.chat.id)
    chattitle2 = chattitle["title"]
    await message.edit_text(f"======\n**title :** ```{chattitle2}```\n**ID GP :** (```{message.chat.id}```)\n**Members Count :** ({await app.get_chat_members_count(message.chat.id)})\n======")


@app.on_message(filters.command("pin", prefixes="!") & filters.me)
async def spam(client, message):
    await message.delete(message.message_id)
    await app.pin_chat_message(message.chat.id, message.reply_to_message.message_id)


@app.on_message(filters.command("clear", prefixes="") & filters.me)
async def spam(client, message):
    userenemy = message.reply_to_message.from_user.id
    listenemy.remove(userenemy)
    fname = message.reply_to_message.from_user.first_name
    gapfosh.remove(message.chat.id)
    await message.edit_text(f"[{fname}](tg://user?id={userenemy})** Removed From Enemy List๐**")


@app.on_message(filters.command("enemy", prefixes="") & filters.me)
async def spam(client, message):
    userenemy = message.reply_to_message.from_user.id
    fname = message.reply_to_message.from_user.first_name
    listenemy.append(userenemy)
    gapfosh.append(message.chat.id)

    await message.edit_text(f"[{fname}](tg://user?id={userenemy})** Is Enemy Now ๐**")


@app.on_message(filters.command("banhere", prefixes="") & filters.me)
async def spam(client, message):
    await message.delete(message.message_id)
    unsafegap.append(message.chat.id)


@app.on_message(filters.command("unbanhere", prefixes="") & filters.me)
async def spam(client, message):
    await message.delete(message.message_id)
    unsafegap.remove(message.chat.id)


@app.on_message(filters.command("off", prefixes="!") & filters.me)
async def spam(client, message):
    await message.edit_text("**Self Is DeActivated๐ค**")
    gapactive.clear()


@app.on_message(filters.command("on", prefixes="!") & filters.me)
async def spam(client, message):
    await message.edit_text("**ุฑุจุงุช ูุนุงู ุดุฏ**")
    gapactive.append(message.text)


@app.on_message(filters.command("id", prefixes="!") & filters.me)
async def spam(client, message):
    if message.reply_to_message:
        common = await app.get_common_chats(message.reply_to_message.from_user.id)
        commonlen = len(common)
        userget = await app.get_users(message.reply_to_message.from_user.id)
        userget1 = userget["status"]
        count = await app.get_profile_photos_count(message.reply_to_message.from_user.id)
        iduser = message.reply_to_message.from_user.id
        firstnameuser = message.reply_to_message.from_user.first_name
        if userget1 == "online":
            await message.edit(f"==========\n**โถ Name : **(```{firstnameuser}```)\n**โถ Userid :** (```{iduser}```)\n**โถ Profile Pictures :** (```{count}```)\n**โถ Status :** (Online โ)\n\n**โถ Common Groups :** ({commonlen})\n========== ")
        elif userget1 == "offline":
            await message.edit(f"==========\n**โถ Name : **(```{firstnameuser}```)\n**โถ Userid :** (```{iduser}```)\n**โถ Profile Pictures :** (```{count}```)\n**โถ Status :** (Offline ๐ต)\n\n**โถ Common Groups :** ({commonlen})\n========== ")
        elif userget1 == "recently":
            await message.edit(f"==========\n**โถ Name : **(```{firstnameuser}```)\n**โถ Userid :** (```{iduser}```)\n**โถ Profile Pictures :** (```{count}```)\n**โถ Status :** (Recently ๐)\n\n**โถ Common Groups :** ({commonlen})\n========== ")


@app.on_message(filters.command("$", prefixes="") & filters.me)
async def spam(client, message):
    try:
        isit = message.text.split()
        nums = isit[2::1]
        ums = [int(num) for num in nums]
        await message.edit_text(f"ุฌูุงุจ : {cal(isit,nums)}")
    except:
        await message.reply("Wrong Command !")

@app.on_message(filters.regex(r"^ู?ฺฉ") & filters.me)
async def hello1(client, message):
    text = message.text.split()
    av = {"ุง?ุฑุงู" : "fa-IR" , "ุงููุงู" : "de-DE" , "ฺุงูพู" : "jp-JP" , "ุงูุฑ?ฺฉุง" : "en-US" , "ฺฉุงูุงุฏุง" : "en-CA" , "ููุฏ" : "en-IN"}
    if text[1] in av.keys():
        f = Faker(av[text[1]])
        fullname = f.name()
        email = f.email()
        address = f.address()
        city = f.city()
        credit = f.credit_card_full()
        fake = f"**ุงุณู** : {fullname}\n**ุง?ู?ู** : {email}\n**ุงุฏุฑุณ** : {address}\n**ุดูุฑ** : {city}\n**ุงุทูุงุนุงุช ฺฉุงุฑุช** : {credit}"
        await message.edit(f"โโโโโโโโโ ? โโโโโโโโโ\n{fake}")
    else:
        yy = " - ".join(av.keys())
        await message.edit(f"__ุงุฒ ฺฉุดูุฑ ูุง? ุฑูุจุฑู ุงุณุชูุงุฏู ฺฉู?ุฏ :__ {yy}")
    #     #Commands can be Turned Off ===================================


@app.on_message(filters.regex("^ฺฉ?ุฑ$") & filters.group)
async def spam(client, message):
    if "!on" in gapactive and unsafegap.count(message.chat.id) == 0:
        await message.reply("__ู?ุฎูุง?ุ__")


@app.on_message(filters.regex("^ฺฉ?ุฑู$") & filters.group)
async def spam(client, message):
    if "!on" in gapactive and unsafegap.count(message.chat.id) == 0:
        await message.reply("__ุงุฒ ุงุดูุง?? ุจุงูุงุชูู ุฎูุดุจุฎุชู__")


@app.on_message(filters.regex("^ุณุทุญ$") & filters.group)
async def spam(client, message):
    if "!on" in gapactive and unsafegap.count(message.chat.id) == 0:
        if message.from_user.id == 1708823038:
            await message.reply(f"ุณุทุญ ุดูุง %100 ู?ุจุงุดุฏ")
        else:
            rand = random.randint(1, 100)
            await message.reply(f"ุณุทุญ ุดูุง %{rand} ู?ุจุงุดุฏ")


# @app.on_message(filters.command("ููุงู", prefixes="") & filters.group)
# async def spam(client, message):
#     if "!on" in gapactive and unsafegap.count(message.chat.id) == 0:
#         await message.reply("ุชู ุจูุงู")


@app.on_message(filters.command("@Vector_Fa", prefixes="") & filters.group)
async def spam(client, message):
    if "!on" in gapactive and unsafegap.count(message.chat.id) == 0:
        await message.reply("__ูุฎููุฏู__")


@app.on_message(filters.regex("^ุฑ?ุฏู$") & filters.group)
async def spam(client, message):
    if "!on" in gapactive and unsafegap.count(message.chat.id) == 0:
        await message.reply("__ุนู ูุงูุงุฑุช ุญุงุถุฑ ุดุฏ__")


@app.on_message(filters.command("ุง?ุฒ?", prefixes="") | filters.command("Ez", prefixes="") | filters.command("ez", prefixes="") & filters.group)
async def spam(client, message):
    if "!on" in gapactive and unsafegap.count(message.chat.id) == 0:
        if message.from_user.id == 1708823038:
            await message.reply(f"__ุฏุงุดู MrP ูพุฑู__")
        else:
            await message.reply(f"__ููุจ? ูููุฒ__")


@app.on_message(filters.command("ฺฉูู?", prefixes="") & filters.group)
async def spam(client, message):
    if "!on" in gapactive and unsafegap.count(message.chat.id) == 0:
        await message.reply(f"__ูุงูพุงุช ุจุณุชู? ููู?__")


@app.on_message(filters.command("ุจฺฉ?ุฑู", prefixes="") & filters.group)
async def spam(client, message):
    if "!on" in gapactive and unsafegap.count(message.chat.id) == 0:
        await message.reply(f"ฺฉุณ? ฺฉู ฺฉุต ุฏุงุฑู ุจฺฉ?ุฑู ูู?ฺฏู")


@app.on_message(filters.regex("^ุงูู$") & filters.group)
async def spam(client, message):
    if "!on" in gapactive and unsafegap.count(message.chat.id) == 0:
        aval = random.choice(
            ["ุงูุฑ?ู ุดูุง ?ฺฉ ุช?ุชุงุจ ุทูุง?? ุจุฑูุฏู ุดุฏ?ุฏ", "ูพุดูุงู ฺูุฏุฑ ุชูุฑ?ู ฺฉุฑุฏ? ุจู ุง?ู ุณุฑุนุช ุฑุณ?ุฏ?"])
        await message.reply(aval)


@app.on_message(filters.regex("^ุณุทุญ ฺฏุฑูู$") & filters.group)
async def spam(client, message):
    if "!on" in gapactive and unsafegap.count(message.chat.id) == 0:
        randsath = random.randint(0, 100)
        await message.reply(f"ุณุทุญ ฺฏุฑูู %{randsath} ุงุณุช")


@app.on_message(filters.regex("^ููุงู$") & filters.group )
async def spam(client, message):
    if "!on" in gapactive and message.chat.id in [-1001406922641,-1001577002797] and message.reply_to_message:
        makhalinDec = getMakhal(message.reply_to_message.from_user.id)
        if message.reply_to_message.from_user.id == 383456888:
            await message.reply("ุจุฑุง? ููู ู?ุฎูุง? ุจูุงู?ุ")
        elif makhalinDec == None:
            firstNml(message.reply_to_message.from_user.first_name, message.reply_to_message.from_user.id, message.chat.id, 0)
            await message.reply(f"ุงูู?ู ุฎุง?ู ูุงู? [{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) ุซุจุช ุดุฏ")
        else:
            Nummakhal = getMakhal(message.reply_to_message.from_user.id)[3] + 1
            updateMakhal(message.reply_to_message.from_user.id ,message.chat.id ,  Nummakhal)
            await message.reply(f"ุดูุง ?ฺฉ ุฎุง?ู ูุงู? ุจุฑุง? [{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) ุซุจุช ฺฉุฑุฏ?ุฏ \n**ุชุนุฏุงุฏ ุฎุง?ู ูุงู? ูุง? ุฏุฑุญุงู ุญุงุถุฑ : {Nummakhal}**")

@app.on_message(filters.regex("^ุณุทุญ ุจุงุฒ?$") & filters.group)
async def spam(client, message):
    if "!on" in gapactive and unsafegap.count(message.chat.id) == 0:
        ranks = ["iron", "bronze", "silver", "gold",
                 "plat", "diamond", "immortal", "radiant"]
        rank = random.choice(ranks)
        await message.reply(f"ุณุทุญ ุจุงุฒ? ุดูุง ุฏุฑ ุญุฏ ({rank}) ู?ุจุงุดุฏ")


@app.on_message(filters.command("font", prefixes="") & filters.group)
async def spam(client, message):
    if "!on" in gapactive and unsafegap.count(message.chat.id) == 0:
        mylis = []
        text = message.text.split()
        r = requests.get(f"http://api.codebazan.ir/font/?text={text[1]}")
        r = r.json()
        r = r["result"]
        for k, v in r.items():
            mylis.extend([f"{k} : ```{v}```\n"])
        sr = "\n".join(mylis)
        await message.reply(sr)


@app.on_message(filters.command("ุงุฐุงู", prefixes="") & filters.group)
async def spam(client, message):
    if "!on" in gapactive and unsafegap.count(message.chat.id) == 0:
        mylis = []
        text = message.text.split()
        r = requests.get(f"https://api.codebazan.ir/owghat/?city={text[1]}")
        r = r.json()
        r = r["Result"][0]
        for k, v in r.items():
            mylis.extend([f"{k} : {v}\n"])
        sr = "\n".join(mylis)
        if type(r['shahr']) == str:
            await message.reply(sr)
        else:
            await message.reply("**ุดูุฑ ููุฑุฏ ูุธุฑ ุฑุง ุฏุฑุณุช ูุงุฑุฏ ฺฉู?ุฏ.**")
            


@app.on_message(filters.regex(r"^[Ll]ogo") & filters.group)
async def hello1(client, message):
    models = {"1": "79", "2": "75", "3": "77", "4": "73",
              "5": "71", "6": "62", "7": "63", "8": "59"}
    # 64 too
    split = message.text.split()
    messageid = message.message_id
    messageid += 1
    if message.text.lower() == "logo on":
        await message.delete(message.message_id)
        logope.append(message.from_user.id)
    if message.text.lower() == "logo off":
        await message.delete(message.message_id)
        logope.remove(message.from_user.id)
    elif split[1] not in models.keys():
        await message.reply("**ุฏุฑ ุจุงุฒู 1-8 ูุฏู ุฑู ูุงุฑุฏ ฺฉู?ุฏ**")
    elif split[0].lower() == "logo" and message.from_user.id in logope:
        await message.reply("**Sending...**")
        for k, v in models.items():
            if split[1] == k:
                r = requests.get(
                    f"https://api.codebazan.ir/ephoto/writeText?output=image&effect=create-online-black-and-white-layer-logo-{v}.html&text={split[2]}", stream=True)
                with open("ss.png", 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                try:
                    await message.reply_photo("ss.png")
                    await app.delete_messages(message.chat.id, messageid)
                except:
                    await message.reply("ุฏูุจุงุฑู ุงูุชุญุงู ฺฉู?ุฏ")


@app.on_message(filters.command("ูุนู?", prefixes="") & filters.group)
async def spam(client, message):
    if "!on" in gapactive and unsafegap.count(message.chat.id) == 0:
        mylis = []
        text = message.text.split()
        if len(text) == 3:
            r = requests.get(f"https://api.codebazan.ir/vajehyab/?text={text[1]}")
            r = r.json()
            r = r["result"]
            await message.reply(f"ฺฉููู : {r['fa']}\nุงูฺฏู?ุณ? : {r['en']}\n\nูุนู? : {r['mani']}\n\nุฏูุฎุฏุง : {r['Fdehkhoda']}")


@app.on_message(filters.regex(r"^ููุงุดูุงุณ?") & filters.me)
async def hello1(client, message):
    if "!on" in gapactive and unsafegap.count(message.chat.id) == 0:
        mylis = []
        false = ["ุณุฑุนุช ุจุงุฏ", "ุจู ุฑูุฒ ุฑุณุงู?"]
        r = requests.get(
            f"https://api.codebazan.ir/weather/?city={message.text.split()[1]}").json()
        today = r['result']
        for k, v in today.items():
            if k not in false:
                mylis.extend([f"**{k}** : {v}"])
            else:
                continue
        str = "\n".join(mylis)
        await app.edit_message_text(message.chat.id, message.message_id, f"{str}\n**ุฏูุง? ูุฑุฏุง** : {r['ูุฑุฏุง']['ุฏูุง']}")


@app.on_message(filters.regex(r"^[Ww]ikipedia") & filters.me)
async def hello1(client, message):
    if "!on" in gapactive and unsafegap.count(message.chat.id) == 0:
        text = message.text.split()
        try:
            if len(text) == 1:
                await message.reply(wikipedia.summary(text[1] , sentences = 3))
        except:
            await message.reply("**Didn't Found Any Thing.**")

@app.on_message(filters.regex("^ูุฑุฎ ุงุฑุฒ$") & filters.group)
async def spam(client, message):
    arzez = {"ุฏูุงุฑ ฺฉุงูุงุฏุง": "ุฏูุงุฑ ฺฉุงูุงุฏุง ๐จ๐ฆ : ", "ุฏูุงุฑ": "ุฏูุงุฑ ุงูุฑ?ฺฉุง ๐บ๐ธ : ", "?ูุฑู": "?ูุฑู ๐ช๐บ : ", "ุฏุฑูู ุงูุงุฑุงุช": "ุฏุฑูู ุงูุงุฑุงุช ๐ฆ๐ช : ","ุฏุฑุงู ุงุฑููุณุชุงู": "ุฏุฑุงู ุงุฑููุณุชุงู ๐ฆ๐ฒ :","ุฑ?ุงู ุนุฑุจุณุชุงู": "ุฑ?ุงู ุนุฑุจุณุชุงู ๐ธ๐ฆ :", "ุฏ?ูุงุฑ ุนุฑุงู": "ุฏ?ูุงุฑ ุนุฑุงู ๐ฎ๐ถ : ", "ุฑูุจู ุฑูุณ?ู": "ุฑูุจู ุฑูุณ?ู ๐ท๐บ : ", "ูพููุฏ ุงูฺฏู?ุณ": "ูพููุฏ ุงูฺฏู?ุณ ๐ฌ๐ง : ", "ู?ุฑ ุชุฑฺฉ?ู": "ู?ุฑ ุชุฑฺฉ?ู ๐น๐ท : "}
    if "!on" in gapactive and unsafegap.count(message.chat.id) == 0:
            listarz = []
            r = requests.get("http://api.codebazan.ir/arz/?type=arz")
            r = r.json()
            for i in r:
                for k, v in arzez.items():
                    if i['name'] == k:
                        listarz.append(f"{v}**{i['price']}**")
            list1 = "\n".join(listarz)
            await message.reply(list1)


@app.on_message(filters.regex("^ฺฉุฑ?ูพุชู$") & filters.group)
async def spam(client, message):
    if "!on" in gapactive and unsafegap.count(message.chat.id) == 0:
        await message.reply(CryptoP)


@app.on_message(filters.regex("^imdb$") & filters.group)
async def spam(client, message):
    if "!on" in gapactive and unsafegap.count(message.chat.id) == 0:
        await message.reply(movielist[0])


@app.on_message(filters.group, group=6)
async def spam(client, message):
    if message.chat.id in typinggap:
        await app.send_chat_action(message.chat.id, "typing")
    if "t" in markread and message.chat.id in markreadgap:
        await app.read_history(message.chat.id, message.message_id)



@app.on_message(filters.private)
async def hello1(client, message):
    if message.from_user.id not in unsafegap:
        await app.send_chat_action(message.chat.id, "typing")
    if "t" in markreadpv:
        await app.read_history(message.chat.id, message.message_id)
    if message.text == "ุณูุงู" or message.text == "slm" or message.text == "salam" and userid1:
        slm = random.choice(["ุณูุงู", "ุนู?ฺฉ ุณูุงู"])
        await message.reply(slm)
    elif message.text == "ููููู" or message.text == "ูุฑุณ?" or message.text == "mrc":
        await message.reply("ุฎูุงูุด")


@app.on_message(filters.regex("^Ssend$") & filters.private, group=8)
async def hello1(client, message):
    await message.edit_text("""
        โ ุงฺฏู? ุดูุง ุจุง ูููู?ุช ุฏุฑ ฺฉุงูุงู ูุฑุงุฑ ฺฏุฑูุช
โ ๏ธุจุฑุง? ุฌููฺฏ?ุฑ? ุงุฒ ุงุณูพู ูุฑ ?ด ุณุงุนุช ุงฺฏู?ุชูู ุฑู ุจูุฑุณุช?ุฏ
        """)
    await app.copy_message("@ImPeRiAlZuLa", message.chat.id, message.reply_to_message.message_id)


    

scheduler.start()
app.run()
