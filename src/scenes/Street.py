# -*- coding: utf-8 -*-
'''
Stage: "通り"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def in_the_rain(w: World):
    return w.scene('雨の中で',
            "どこにも自分の居場所がない、ピアノが弾けない、存在価値がなくなっていると感じる",
            "そこを通りかかった男性は$makiに話しかけた",
            "だが男の声が聞こえない彼女",
            "男は気づいてメモを書いてくれた。「君を買いたい」と",
            "よくここでピアノを弾いていたのを知っていたのだ",
            outline="パパ活がうまくいかず、途方にくれていたところで、$makiは最後の希望と通りかかった$sakaiにすがりつく")

