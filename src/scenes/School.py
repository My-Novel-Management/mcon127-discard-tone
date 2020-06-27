# -*- coding: utf-8 -*-
'''
Stage: "学校"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def dispising(w: World):
    maki = w.get('maki')
    return w.scene('蔑まれる$maki',
            maki.come("久しぶりにセーラー服を着て高校にやってきた"),
            maki.do("誰もがよそよそしく、教室に入る$Sを遠ざけるようにして見ている"),
            maki.do("担任も特に語りかけることなく、とにかく無視してやり過ごそうとしている"),
            maki.do("休み時間、トイレに入った$Sは、そこで噂しているのを聞いてしまう"),
            maki.hear("売春してるんだってさ、とか"),
            maki.do("何も言わずに個室を出て、無視したまま手を洗うと、外に出ていった"),
            outline="久々に高校にやってきた$makiは、売春して知らない男の家を泊まり歩いているなどと、あらぬ噂が立てられていた")

