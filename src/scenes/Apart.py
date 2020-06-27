# -*- coding: utf-8 -*-
'''
Stage: "弥生のアパート"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def her_marriage(w: World):
    maki, yayoi = w.get('maki'), w.get('yayoi')
    return w.scene('$yayoiの結婚',
            maki.come("いつものように遊びにきたら、"),
            maki.do("引っ越しのトラックがあり、ピアノが運び出されていくのを見た"),
            yayoi.be("業者の人と話し込んでいる"),
            maki.talk("$yayoiさん"),
            yayoi.talk("ああ、$makiちゃん", "実はね、結婚するんだ"),
            maki.do("彼女から説明を受ける"),
            maki.talk("それじゃあ福岡に行っちゃうの？", "ピアノも一緒に？"),
            yayoi.talk("荷物だけ先に送って、あとはこっちで色々と準備もあるから",
                "なかなか言い出せなくてね", "ほんとにごめんなさい"),
            outline="ある日$yayoiが結婚することになり、アパートを引き払って福岡に行くと告白した")

