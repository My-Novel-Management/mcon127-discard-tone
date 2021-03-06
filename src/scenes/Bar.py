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
    soda = w.get('soda')
    return w.scene('$makiの日常',
            w.symbol("　　　　◆"),
            maki.talk("ほんともう酷いんだよ", "自分が酒飲みたいからって娘捕まえて酒のアテを作らせるんだからさ"),
            maki.be("カウンターだけに明かりが灯った暗い店内で、$makiは皿の上に盛られたピラフをスプーンで掬って口に詰め込みながら、",
                "夜の仕込みをする$yayoiに愚痴を零していた"),
            yyi.be(),
            yyi.talk("ごめんねえ、$makiちゃん", "うちのピアノ壊れたまま、まだ修理に出せないでいるから"),
            maki.talk("え？"),
            maki.do("大鍋に彼女お得意のビーフシチューを煮込みながら何か喋っているのは分かったが、",
                "生憎と口を読み取れる角度にない", "思わず聞き返した$Sに$yayoiはジェスチャーでピアノを指差して補足した"),
            maki.talk("$yayoiさんは悪くない", "あのバカ親父が悪いだけだよ"),
            yyi.look("それに苦笑しつつ$Sは水のお替りを注いでくれる",
                "五十を過ぎて顎も二重になった彼女は真っ白い顔パックを貼り付けたまま作業をしていて、",
                "間違って客が入ってきたらお化けと$makiが会話しているのかと勘違いしてしまいそうだ",
                "エプロンに書かれた横文字が更にワイドに広がるような豊満な体型が右に左にと動く様はエネルギッシュだが、",
                "あの大根より太い腕に抱っこされてあやされていたんだなと思うと、", "&"),
            maki.think("たまには肩揉みでもして日頃の恩返しをしたくなってくる"),
            maki.talk("ねえ$yayoiさん、何か手伝うことある？"),
            yyi.talk("いつも悪いわね", "それじゃあ床の掃除でもしといてくれる？"),
            maki.talk("分かりました"),
            maki.do("夕食代わりのピラフをさっさと食べ終えて皿とコップを洗うと、",
                "奥のロッカーから箒を取ってきて椅子がテーブルの上に反対にして上げてある、その下の埃を集めて掃き出していく"),
            maki.do("$makiが生まれた頃には既にこの場所で飲み屋を始めていたというから、天井や壁には十七年以上前の酒や煙草の臭いが染み付いているのだろう",
                "あの酔っぱらいのピアノに惚れたという、顔も覚えていない母親は、今頃どこかで別の家族でも作っているのだろうか",
                "一月に一回くらいはそんなことを考えるけれど、",
                "今更母親面して戻ってこられてもこっちがどんな顔すればいいか分からない"),
            yyi.talk("補聴器でも買ってあげられればいいんだろうけどね"),
            maki.talk("何ですか？"),
            yyi.talk("ううん。お父さん、今日もパチンコ？"),
            maki.talk("家で寝ちゃいましたよ"),
            maki.do("手でハンドルを回す動作をした$yayoiにそう答えて一瞬肩を竦め、掃除の続きに戻った"),
            outline="$makiは父親が働いている飲み屋")

