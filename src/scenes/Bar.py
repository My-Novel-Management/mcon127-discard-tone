# -*- coding: utf-8 -*-
'''
Stage: "仕事先の飲み屋"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def her_everyday(w: World):
    maki = w.get('maki')
    dad = w.get('dad')
    yyi = w.get('yayoi')
    return w.scene('$makiの日常',
            maki.come("父親が働かせてもらっている飲み屋にやってくる$S"),
            yyi.be("店の準備をしている$S"),
            yyi.look("厚化粧で、でっぷりした体型", "煙草を咥えている"),
            yyi.talk("あら$makiちゃん、いらっしゃい", "ピアノならまだ壊れたままだから、ごめんね"),
            maki.talk("いいですよ", "なんか手伝うことありますか？"),
            yyi.talk("じゃあ掃除でもしてもらおうかね"),
            maki.talk("分かりました"),
            maki.do("床を箒で掃いていく"),
            maki.do("小さい頃から何かと世話になっていた",
                "父親に愛想をつかして出ていった母親の代わりに、$yayoiさんや店に来る人たちに育てられたようなものだ"),
            yyi.do("夕食をもってくる"),
            maki.talk("ありがとうございます"),
            yyi.talk("補聴器でも買ってあげられればいいんだろうけどね"),
            maki.talk("何ですか？"),
            yyi.talk("ううん。お父さん、今日もパチンコ？"),
            maki.talk("家で寝てます"),
            outline="$makiは父親が働いている飲み屋")

