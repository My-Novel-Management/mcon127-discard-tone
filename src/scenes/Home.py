# -*- coding: utf-8 -*-
'''
Stage: "真希の家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def be_victim(w: World):
    maki = w.get('maki')
    dad = w.get('dad')
    return w.scene('被害者面',
            "貧しさがわかる狭さと物、あと$makiが苦労して生活を支えていることなど",
            "壁にはセーラー服が掛けてある",
            maki.be("家に戻ってきた$S"),
            dad.come("入ってくる父"),
            dad.do("その手のビニール袋にはアルコールが入っている"),
            dad.talk("全く、お前は自分が女だってこと忘れてんだろ？", "ああ、何言ったって聞こえないか？"),
            maki.talk("違うもん", "$sakaiさんは"),
            "父親の怒鳴り声が、まだ耳がしっかり聞こえていた頃にいつまでも鳴り止まない雑音だったことを思い出す",
            dad.talk("何が違うんだよ", "あいつが脳梗塞起こさなかったらお前一生あそこに監禁だったかも知れないんだぞ？"),
            maki.do("小さな卓上テレビをつけると、そこには$Sのことが匿名でニュースになっていた",
                "$sakaiのことは実名報道で、誘拐・監禁していた男性が病死した事件として扱っていた"),
            maki.talk("違うのに"),
            dad.do("つまみを出して、缶ビールをあけて飲み始める父親"),
            maki.do("そのうちにいびきを立てて寝始めた父",
                "それを見て、$Sはこっそりと家を抜け出した"),
            outline="家に連れ戻された$makiは、世間では$sakaiに監禁されていたことになっていた")

