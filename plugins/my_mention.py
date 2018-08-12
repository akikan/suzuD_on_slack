# -*- coding: utf-8 -*-
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
from time import sleep
from libs import my_functions as tw       # 外部関数の読み込み
import copy

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')      @発言者名: string でメッセージを送信
# message.send('string')       string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
@respond_to('twitter')
def mention_func(message):
    try:
        message.send(tw.getTweet()) # メンション
    except:
        message.reply(u'しばらく時間を空けてお試しください')

@listen_to(u'しゃべ(.*)')
def mention_func(message, something):
    numList = re.findall('([0-9])',something)
    temp = 1 if len(numList) == 0 else int(numList[0])
    temp = temp if temp < 5 else 5
    for i in range(temp):
        message.send(tw.gene())


@respond_to(u'どうしてだよぉぉぉぉぉ')
def mention_func(message):
    message.send("ど\"う\"し\"て\"だ\"よ\"ぉ\"ぉ\"ぉ\"ぉ\"ぉ\"")

@respond_to(u'うんこ')
def mention_func(message):
    message.send(u"漏らしてもうた")

@respond_to(u'鈴D')
@respond_to(u'ウンD')
def mention_func(message):
    message.send(u"盗んでもうた")



@respond_to('help')
def mention_func(message):
    message.send(u'キーワードは「twitter」,「しゃべ」,「鈴D」、「ウンD」、「藤原竜也「.*」」です')

@respond_to(u'藤原竜也「(.*)」')
def mention_func(message,something):
    isKeyword=False
    keyList=["help","ウンD","鈴D","うんこ","しゃべ","twitter"]
    wordList=[u"キーワードは「twitter」,「しゃべ」,「鈴D」、「ウンD」、「藤原竜也「.*」」だよぉぉぉぉぉ",
    u"盗んでもうたよぉぉぉぉぉ",
    u"盗んでもうたよぉぉぉぉぉ",
    u"漏らしてもうたよぉぉぉぉぉ",
    tw.gene(),
    tw.getTweet()
    ]

    temp=""
    #既存機能との組み合わせなら
    for key,word in zip(keyList, wordList):
        if key in something:
            temp=word
            isKeyword=True
    #藤原竜也に言わせたいだけなら
    if not isKeyword:
        temp = something.split("藤原竜也「")[-1]
    #Unicodeかstrかのチェック
    if isinstance(temp,str):
        hoge = u"゛".join(list(temp.decode('utf-8')))
        message.send(hoge.encode("utf-8"))
    else:
        hoge = u"゛".join(list(temp))
        message.send(hoge.encode("utf-8"))
