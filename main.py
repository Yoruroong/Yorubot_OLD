#-*- coding:utf-8 -*-
# 요루가 만들었어요
# Yoru#0002
# 출처 남기고 재사용 가능
# 코드 더러워서 죄송합니다
import discord
import json
import os
from discord.ext import commands
import asyncio
import random
from random import choice
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus,unquote
import requests
from bs4 import BeautifulSoup
import urllib
import bs4
import xml.etree.ElementTree as ET
import os
import socket
import string
import sys
import psutil
import datetime
from googletrans import Translator
import inspect
import time
import re
import nekos
import aiohttp
import re
import pyowm



app = commands.Bot(command_prefix = 'r!')

##수정해야할부분

translator = Translator()

client_id = "" # 개발자센터에서 발급받은 Client ID 값
client_secret = "" # 개발자센터에서 발급받은 Client Secret 값

API_Key = 'Open Weather Map API키 입력'
owm = pyowm.OWM(API_Key)


TOKEN = 'discord developers에서 발급한 TOKEN입력'

##끝


ball = ['음...그럴일은 없을거 같아요...', '음...웬지 그 일이 생길거 같아요..', '잘 모르겠어요;;', '그럴 확률을 베제할 수는 없는거 같아요...', '그럴 확률이 높아요!', '꼭 그 일이 실현될거에요!']
@app.event
async def on_ready():
    print('Login!')
    guild=str(len(app.guilds))
    user=str(len(app.users))
    
    with open('users.json', 'r') as f:
        users = json.load(f)

    with open('users.json', 'w') as f:
        json.dump(users, f)

@app.event
async def on_message(message):
    if message.author.bot: return
    userid = str(message.author.id)
    guildid = str(message.guild.id)
    channel = message.channel
    check = str(message.channel)
    check_channel = check.split(" ")
    check = check_channel[0]
    
    with open('users.json', 'r') as f:
        users = json.load(f)



    if message.content.startswith('r!ban'):
        if message.author.guild_permissions.kick_members:
            if message.content[6:].startswith('<@'):
                try:
                    mention_id = re.findall(r'\d+', message.content) 
                    mention_id = mention_id[0]
                    mention_id = str(mention_id)
                    await message.guild.ban(app.get_user(int(mention_id)))
                    msg = '<@{}>님을 밴하였어요!'
                    await channel.send(msg.format(mention_id))
                except:
                    msg = '높거나 제게 밴 할수있는 권한이 없어요ㅠㅠ'
                    msg = '밴하려는 사람의 권한이 저보다 {}'.format(msg)
                    await channel.send(msg)
            else:
                await channel.send("유저를 언급하여 주세요!")
        else:
            await channel.send('You have no authority.')

    if message.content.startswith('r!kick'):
        if message.author.guild_permissions.kick_members:
            if message.content[7:].startswith('<@'):
                try:
                    mention_id = re.findall(r'\d+', message.content) 
                    mention_id = mention_id[0]
                    mention_id = str(mention_id)
                    await message.guild.kick(app.get_user(int(mention_id)))
                    msg = '<@{}>님을 킥하였어요!'
                    await channel.send(msg.format(mention_id))
                except:
                    msg = '높거나 제게 kick 할수있는 권한이 없어요ㅠㅠ'
                    msg = '킥하려는 사람의 권한이 저보다 {}'.format(msg)
                    await channel.send(msg)
            else:
                await channel.send("유저를 언급하여 주세요!")
        else:
            await channel.send('You have no authority.')


    if message.content.startswith('r!clean'):
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            msg = await channel.send('SUCCESS')

    if message.content == 'r!join':
        if not userid in users:
            users[userid] = {}
            users[userid]['memo']="NONE"
            users[userid]['vip']=0
            users[userid]['money']=0
            msg11 = "귀하는 http://yoru.pe.kr/yorubot/terms 에 동의하신걸로 간주됩니다."
            await channel.send('가입 성공.{}'.format(msg11))
        else:
            await channel.send('이미 가입이 되어 있습니다.')

    if message.content == 'r!돈':
        try:
            money = users[userid]['money']
            await channel.send('당신의 잔고는 `{}` CUTE 입니다.'.format(money))
        except:
            await channel.send('r!join')


    if message.content == 'r!돈내놔':
        try:
            get=users[userid]['got']
            if get == 0:
                ran = random.randrange(100,777)
                await channel.send('당신의 잔고에 100CUTE~777CUTE 사이의 돈을 넣을께요~')
                users[userid]['got'] = 1
                users[userid]['money'] = users[userid]['money'] + ran
                await channel.send('`{}`CUTE만큼의 돈을 당신의 잔고에 넣었어요!'.format(ran))
            else:
                await channel.send('쿨타임 지나지 않았습니다')
        except:
            await channel.send('`r!join`')

    if message.content == 'r!help':
        useful = '`r!급검`, `r!번역 [언어] [내용]`, `r!linkshort [link]`, `r!youtube [검색할 제목]`'
        tmi = '루시이봇은 요루봇 파이썬버전을 js버전으로 가져왔어요!'
        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed=discord.Embed(
            title='도움말',
            colour=discord.Colour(value=colour),
        )
        embed.add_field(name='돈', value='`r!돈`,`r!돈받기`,`r!지갑`',inline=False)
        embed.add_field(name='MOD', value='`r!warn @멘션`, `r!kick @멘션`, `r!ban @멘션`, `r!clean`')
        embed.add_field(name='Weather', value='`r!미세먼지`, `r!세계날씨`', inline=False)
        embed.add_field(name='Useful', value=useful)
        embed.add_field(name='Memo', value='`r!memo`, `r!memo [내용]`', inline=False)
        embed.add_field(name='TMI', value=tmi)
        try:
            emsg = await message.channel.send("도움말을 발송중이에요...")
            await message.author.send(embed=embed)
            msg='번역 지원 언어 목록 :  : '
            url='http://yoru.pe.kr/rushii/'
            await message.author.send('{}{}'.format(msg, url))
            await emsg.edit(content=":white_check_mark: DM을 확인해주세요!")
        except:
            return await message.channel.send(embed=embed)
                
    if message.content == 'r!neko':
        neko = nekos.img("neko")
        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(
            title = 'Neko',
            colour=discord.Colour(value=colour),
        )    
        embed.set_footer(text='Nekos Life')
        embed.set_image(url=neko.format(neko))
        await channel.send(embed=embed)
        
    if message.content.startswith('r!미세먼지'):
        API_key = unquote('q0deRRGfv%2FJ%2FBIbfZ5uJbSg%2FsU%2B2ruYwKKDi%2FYolmsyuK7b1IXI691p4WPbfSFmy0LUD0yN90%2Fs7qzGvH9hGWA%3D%3D')
        url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst'
        queryParams = '?' + urlencode({ quote_plus('ServiceKey') : API_key, quote_plus('numOfRows') : '10', quote_plus('pageNo') : '1', quote_plus('itemCode') : 'PM10', quote_plus('dataGubun') : 'HOUR', quote_plus('searchCondition') : 'MONTH' })
        request = Request(url + queryParams)
        request.get_method = lambda: 'GET'
        response_body = urlopen(request).read().decode('utf-8')
        root = ET.fromstring(response_body)
        seoul = root.find('body').find('items').find('item').find('seoul')
        gyeonggi = root.find('body').find('items').find('item').find('gyeonggi')
        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(
            title = '미세먼지',
            description = 'Seoul, Gyeonggi',
            colour=discord.Colour(value=colour),
        )
        embed.add_field(name='Seoul', value='{}pm2'.format(seoul.text))
        embed.add_field(name='Gyeonggi', value='{}pm2'.format(gyeonggi.text))

        await channel.send(embed=embed)

    if message.content.startswith('r!세계날씨'):
        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(
            title = '__**WEATHER**__',
            colour=discord.Colour(value=colour),
        )
        await Print_City_Temp(1835848, embed)
        await Print_City_Temp(1850147, embed)
        await Print_City_Temp(2643743, embed)
        await Print_City_Temp(5128581, embed)
        await Print_City_Temp(2988507, embed)
        await Print_City_Temp(2147714, embed)
        await channel.send(embed=embed)

    if message.content.startswith('r!linkshort'):
        arg = message.content.split(" ")
        args = arg[1]
        encText = urllib.parse.quote(args)
        data = "url=" + encText
        url = "https://openapi.naver.com/v1/util/shorturl"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            response_body.decode('utf-8').replace(' 'and':'and',', '')
            b=response_body.decode('utf-8').split('"')
            em = discord.Embed(title='링크 단축', description=b[13], colour=0xDEADBF)
            em.set_author(name=message.author, icon_url=message.author.avatar_url)
            await channel.send(embed=em)
        else:
            print("Error Code:" + rescode)
            await channel.send("Error Code:" + rescode)

    if message.content.startswith('r!c'):
        if message.author.id == 480240821623455746:
            msg=message.content[3:]
            arg=msg.split(" ")
            args=arg[0:]
            print(args)
            print(msg)
            try:
                python = '```py\n{}\n```'
                res = eval(msg)
                if inspect.isawaitable(res):
                    result = await res
                else:
                    result = res
            except Exception as e:
                embed = discord.Embed(colour=0xef6767, timestamp=datetime.datetime.utcnow())
                embed.add_field(name='Error', value=python.format(str(e)))
                return await message.channel.send(embed=embed)

            embed = discord.Embed(colour=0x6bffc8, timestamp=datetime.datetime.utcnow())
            embed.add_field(name='Success', value=python.format(result))
            await message.channel.send(embed=embed)
        else:
            author=message.author
            msg='cmd:<@{}> {}'.format(userid, userid)
            msg2='권한이 없습니다. 관리자에게 보고되었습니다.<@{}>'
            await app.get_user(480240821623455746).send(msg)
            await channel.send(msg2.format(userid))
        
    if message.content.startswith('r!급검'):
        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(
            title = '실검',
            description = 'Naver.',
            colour=discord.Colour(value=colour),
        )
        html = requests.get('https://naver.com/').text
        soup = BeautifulSoup(html, 'html.parser')

        title_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')

        for idx, title in enumerate(title_list, 1):
            embed.add_field(name='{}{}'.format(idx, '위'), value='{}'.format(title.text), inline=False)

        await channel.send(embed=embed)

    if message.content == 'r!memo':
        if not userid in users:
            await channel.send('`r!join`')
            return
        data = users[userid]['memo']
        embed = discord.Embed(title="메모한 내용", description=data, color=0x00ff00)
        msg = await channel.send(embed = embed)
            
    if message.content.startswith('r!memo '):
        if not userid in users:
            await channel.send('`r!join`')
            return
        args=message.content.split(" ")
        users[userid]['memo']=" ".join(args[1:])
        memo=users[userid]['memo']
        embed = discord.Embed(title="메모가 완료 되었습니다", description='내용:{}'.format(memo), color=0x00ff00)
        await channel.send(embed = embed)

    if message.content.startswith('r!ping'):
        before = time.monotonic()
        msg = await channel.send('PONG!')
        now = time.monotonic()-before
        ping = now*1000
        await msg.edit(content='퐁! 요루봇V2메인 모듈의 핑:{}ms'.format(ping))

    if message.content.startswith('r!say'):
        if not userid in users:
            return await channel.send('`r!join`')
        if vip == 1:
            owner=app.get_user(480240821623455746)
            msg=message.content[6:]
            await channel.send(msg)
            sg = message.guild
            sc = message.channel
            msg='```{}```{}-{}:`{}`'.format(msg, sg, sc, sc.id)
            await owner.send(msg)
            await message.delete()
        else:
            channel.send('This command is for VIP.')
        

    if message.content.startswith('r!resource'):
        cpuav=cpu()
        await channel.send('{}%'.format(cpuav))

    if message.content.startswith('r!번역 한글'):
        m = message.content
        msg=translator.translate(m[7:], src='auto', dest='ko').text
        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(
            title = '번역',
            description = '```{}```'.format(msg),
            colour=discord.Colour(value=colour),
        )
        await channel.send(embed=embed)

    if message.content.startswith('r!번역 영어'):
        m = message.content
        msg=translator.translate(m[7:], src='auto', dest='en').text
        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(
            title = '번역',
            description = '```{}```'.format(msg),
            colour=discord.Colour(value=colour),
        )
        await channel.send(embed=embed)

    if message.content.startswith('r!번역 중국어'):
        m = message.content
        msg=translator.translate(m[8:], src='auto', dest='zh-cn').text
        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(
            title = '번역',
            description = '```{}```'.format(msg),
            colour=discord.Colour(value=colour),
        )
        await channel.send(embed=embed)

    if message.content.startswith('r!번역 포르투갈어'):
        m=message.content
        msg=translator.translate(m[10:], src='auto', dest='pt').text
        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(
            title = '번역',
            description = '```{}```'.format(msg),
            colour=discord.Colour(value=colour),
        )
        await channel.send(embed=embed)

    if message.content.startswith('r!youtube'):
        query = message.content[10:]
        try:
            url = 'https://www.youtube.com/results?'
            payload = {'search_query': ''.join(query)}
            headers = {'user-agent': 'Red-cog/1.0'}
            conn = aiohttp.TCPConnector()
            session = aiohttp.ClientSession(connector=conn)
            async with session.get(url, params=payload, headers=headers) as r:
                result = await r.text()
            await session.close()
            yt_find = re.findall(r'href=\"\/watch\?v=(.{11})', result)
            url = '상위 검색 결과 : https://www.youtube.com/watch?v={}'.format(yt_find[0])
            await channel.send(url)
        except Exception as e:
            message = 'Something went terribly wrong! [{}]'.format(e)
            await channel.send(message)

    if message.content.startswith("r!backup"):
        if message.author.id == 480240821623455746:
            emsg = await message.channel.send("백업중이에요...")
            await emsg.edit(content="클라우드에 백업중(11%)")
            await emsg.edit(content="클라우드에 백업중(69%)")
            await emsg.edit(content="클라우드에 백업중(100%)")
            await emsg.edit(content="BACKUP을 성공했어요")

    if message.content.startswith('r!8ball'):
        msg = message.content[8:]
        if msg == "":
            rmsg = '질문을 입력해주세요! `r!8ball [Q]`'
            await channel.send(rmsg)
            return
        rand = random.choice(ball)
        rmsg = '질문:{} \n 답변:{}'
        print(rmsg)
        await channel.send(rmsg.format(msg, rand))

    with open('users.json', 'w') as f:
        json.dump(users, f)
        
def cpu():
    cpu = 0
    for x in range(2):
        cpu += psutil.cpu_percent(interval=1)
    return round(float(cpu)/3,2)

async def Print_City_Temp(City_ID, embed):
    obs = owm.weather_at_id(City_ID)  
    
    L = obs.get_location()
    City_name = L.get_name()
    
    W = obs.get_weather()
    Status = W.get_status()

    if Status == 'Haze':
        Status = '`안개`'
    if Status == 'Clouds':
        Status = '`구름`'
    if Status == 'Rain':
        Status = '`비`'
    
    Temp = W.get_temperature(unit='celsius')

    msg = City_name + '의 현재 날씨는 '+ Status + '이고 온도는 ' + str(Temp['temp']) + '도 입니다.'
    embed.add_field(name=City_name, value=msg, inline=False)


app.run(TOKEN)
