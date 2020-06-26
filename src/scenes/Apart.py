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
    return w.scene('$yayoiの結婚',
            "いつものように近所の元音大生の$yayoiの家に遊びにきた$makiだったが、そこでピアノが運び出されていくのを目撃する",
            "慌てて乗り込んで聞くと、メモを使って事情を説明してくれた",
            "$yayoiは結婚して福岡に行くらしい",
            "ごめんね、と謝る$yayoi",
            outline="ある日$yayoiが結婚することになり、アパートを引き払って福岡に行くと告白した")

