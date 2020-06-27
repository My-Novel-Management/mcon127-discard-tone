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
    maki, sakai = w.get('maki'), w.get('sakai')
    return w.scene('雨の中で',
            "雨を避けるようにしてアーケードに。誰もいない",
            maki.come("駅前のピアノがなくなり、途方にくれて誰もいなくなった商店街のアーケードの下を歩いていた"),
            maki.do("雨が降っているけれど、音は聞こえない", "ただ寒さを感じる", "空腹に襲われる"),
            maki.do("お金がないことに気づいて、力なく道端に座り込む"),
            maki.do("警官の姿を見て、逃げ出す"),
            "警官は恐怖の対象",
            maki.do("雨の中に駆け出して、びしょ濡れになる"),
            maki.do("と、$Sの隣に車が停まる"),
            sakai.be("車から降りてきたのは知らない男性"),
            sakai.talk("どうして濡れているんだい？"),
            maki.do("男が何を言っているか分からない"),
            maki.do("くしゃくしゃのメモ帳を見せて"),
            sakai.talk("ああ、そうか", "君もそうなんだね", "とりあえずうちに来なさい", "風邪をひいてしまう"),
            maki.do("どうしようか迷ったが、泊まらせてくれるかも知れないと覚悟を決めて車に乗り込んだ"),
            outline="パパ活がうまくいかず、途方にくれていたところで、$makiは最後の希望と通りかかった$sakaiにすがりつく")

