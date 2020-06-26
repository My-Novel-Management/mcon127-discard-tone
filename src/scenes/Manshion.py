# -*- coding: utf-8 -*-
'''
Stage: "堺田のマンション"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def he_is_composer(w: World):
    return w.scene('彼は作曲家',
            "$makiを拾った男は広いマンションに一人暮らしだった",
            "作曲家だという",
            "大好きなピアノがあり、それを弾かせてもらう",
            "男は自分も難聴なんだと告白する",
            "補聴器を使っていた",
            "新しい曲はもう十年以上作っていないらしい。難聴を患い、作曲できなくなったという",
            outline="$makiを拾った男の家にはピアノがあった。元作曲家だという")

def alms_giving(w: World):
    return w.scene("男の施し",
            outline="ピアノを失った$makiに男はいつでも遊びにきてピアノを弾けばいいと言ってくれた")

def lostman(w: World):
    return w.scene("失った男",
            "$sakaiは自分の事情を語る",
            "$makiを買いたいと言ったのは、あんなに楽しそうにピアノを弾く人が羨ましかったからだと",
            "$sakaiは$makiに未発表曲を弾いてくれないかと依頼する",
            "それは$makiの初めての仕事だった",
            outline="$sakaiは大切なものを失ったと、説明した")

def falldown(w: World):
    return w.scene("倒れる男",
            outline="ある日、$sakaiの部屋に入ると、彼が倒れていた")
