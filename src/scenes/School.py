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
    return w.scene('蔑まれる$maki',
            "久々に高校にやってきた$makiだったが、今まで以上に周囲のよそよそしい態度に疑問を覚える",
            "先生から呼び出され、売春しているのかと聞かれてブチギレる",
            "再び学校から逃げ出す$maki",
            outline="久々に高校にやってきた$makiは、売春して知らない男の家を泊まり歩いているなどと、あらぬ噂が立てられていた")

