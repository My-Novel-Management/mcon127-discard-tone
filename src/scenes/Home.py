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
    return w.scene('被害者面',
            "警察の事情聴取を終えて家に戻ってくると、世間では$makiは誘拐・監禁されたことになっていた",
            "$sakaiの扱いの酷さに激昂し、$makiは再び家を飛び出す",
            outline="家に連れ戻された$makiは、世間では$sakaiに監禁されていたことになっていた")

