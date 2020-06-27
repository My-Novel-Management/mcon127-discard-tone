#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "Discard her tone"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from config import ASSET
# import scenes
from scenes import Apart
from scenes import Bar
from scenes import Home
from scenes import Manshion
from scenes import School
from scenes import Station
from scenes import Street


################################################################
#
#   1. Story memo
#   2. Story structure
#   3. Plot
#   4. Conte
#   5. Draft
#
################################################################

# Constant
TITLE = "音を捨てた彼女"
OUTLINE = "家族や同級生の声から耳を閉ざしたピアノだけが友人の少女は、男に拾われる。男もまた失った人だった。恩人の男に恩返しをするため、少女はピアノを弾くステージに立つ"


# Episodes
def ep_runaway(w: World):
    return w.episode('全てから逃げ出した',
            "夢しかないものが、それにすがりつづけた結果、拍手喝采をもらう物語",
            "音のない世界を楽しむ彼女、から始まると良い",
            "$makiが敵視する人々、世界、その代表者",
            w.plot_note("駅前に誰でも弾けるピアノが置いてある", "それを楽しげに$makiが弾いているが酔っぱらいがやめろとやってくる",
                "それが$makiの父親だった"),
            Station.free_piano(w),
            w.plot_note("小さい頃からピアノだけが友人だった$makiは、周囲とは馴染めず、心と耳を閉ざしていく","徐々に学校をサボるようになった"),
            w.plot_note("学校を抜け出していつも遊びに行ったピアノを自宅に持っている元音大生の$yayoiが、ある時結婚してしまい、$makiは行き場を失った"),
            Apart.her_marriage(w).omit(),
            Bar.her_everyday(w),
            Station.vanish_piano(w),
            )

def ep_catchup(w: World):
    return w.episode('掃き溜めから拾った男',
            "本物の雨の中で、拾われる",
            Street.in_the_rain(w),
            w.plot_note("パパ活でもして寝床を探そうとしたがうまくいかず、自暴自棄になっていた$makiを拾った男$sakaiは、全てを失った元作曲家だった"),
            Manshion.he_is_composer(w),
            w.plot_note("難聴だという$sakaiは$makiに自由にピアノを弾かせてくれた"),
            Manshion.alms_giving(w),
            Manshion.lostman(w),
            w.plot_note("突発性難聴の原因はよく分かっていないが、血流との関係が問題視されている等と教わる"),
            "脳梗塞を十年後に起こす可能性が高いらしい＞突発性難聴",
            w.plot_note("「このままペットみたいにあなたが飼ってくれたらいいのに」と言い出す$makiは、それでも$sakaiといつか家に帰る約束をさせられた"),
            )

def ep_getback(w: World):
    return w.episode('取り戻す',
            "なぜ彼女は彼の為にその楽譜を弾くのか？",
            w.plot_note("彼の為に一度は捨てた音を取り戻し、$makiはピアノの練習をする"),
            "また逃げ出そうとする$maki",
            School.dispising(w),
            w.plot_note("彼は脳梗塞で亡くなってしまった"),
            Manshion.falldown(w),
            w.plot_note("家族に引き取られ、$makiは$sakaiに誘拐監禁されていたことになり、世間で彼は犯罪者扱いされた"),
            Home.be_victim(w),
            )

def ep_mainstage(w: World):
    return w.episode('メインステージ',
            w.plot_note("彼へと捧げる彼の曲を、駅前のピアノで弾き始める$maki"),
            Station.piano_again(w),
            w.plot_note("そのピアノの音色が彼女が否定した世間から注目を集めるようになる"),
            Station.expand_piano(w),
            w.plot_note("$makiはピアノを弾く", "何も聞こえないはずの彼女に、雨の音がした", "それは観衆の拍手の雨だった"),
            Station.clap_rain(w),
            w.symbol("（了）"),
            )

# TODO: あとで人物履歴に修正すること。今回は間に合わないのでエピソードで作ってomitします
def nt_maki(w: World):
    return w.episode('$makiの履歴書',
            "母親に逃げられた場末のピアノ弾きの父親と、そのバーや飲み屋のおばちゃんたちに囲まれて育つ",
            "生まれた頃から音に対して過敏なところを見せる",
            "いつもヤニとアルコールの臭いに囲まれた中で、音楽に囲まれながら、店に入れ替わり立ち代わりやってくる人妻の母乳やミルクで大きくなる",
            "おもちゃ代わりに遊んでいたピアノは、バーのママと、腕だけは確かだった父親から教わり、小学生でリストに挑戦するほどになった",
            "小学校に入り、周囲と馴染めず、一人で音楽室に忍び込んでピアノを弾いているところを先生に注意された",
            "学校でも問題になり、徐々に学校に行かないでバーや飲み屋に入り浸ってピアノを弾いてお小遣いをもらうという生活をしていた",
            "しかし父親にばれるといつもアパートの何もない部屋に連れ戻され、監禁される",
            "酒びたりの父は徐々に暴力もひどくなり、連れ込んだ女へのＤＶを見たくなくて耳も目も塞ぐような暮らし",
            "何度か逃げ出そうとしたが、その度に見つかり、連れ戻された",
            )

def nt_sakai(w: World):
    return w.episode('$sakaiの履歴書',
            "世界的に有名なフルート奏者の母親の下に生まれる",
            "幼い頃からうるさくても笑っている、不思議な子どもだった",
            "ただこの頃から少し耳が悪く、難聴気味であった",
            "世界を飛び回る母親の代わりに、親戚のおばさんの家で大きくなる",
            "レコード収集家であったその叔母の家で、クラシックの名曲に囲まれて大きくなった",
            "物心ついた頃には鼻歌で自作の曲を作り、小学生の頃には作曲するということを覚えた",
            "母親はその才能に大いに喜び、音楽の家庭教師を雇った",
            "音大に入り、めきめきと頭角を表す",
            "ただ周囲とはあまり馴染めなかった。対人コミュニケーションに大きな問題を抱えていたのだ",
            "それは早熟の天才たちにありがちな、周囲と違いすぎる感覚・感性による孤立だった",
            "紐基質で女には困らなかったが、あまり性的なことに関心がなく、いつもピアノに向かって作曲しているような学生生活だった",
            "大学三年の時に作曲コンクールで入賞し、そこから作曲家としての人生が始まる",
            "しかし突発性難聴から、音が聞こえなくなり、作曲家としての人生を諦めた",
            "若い頃にいくつか売れた曲と、投資での生活",
            )


def ch_writernote(w: World):
    return w.chapter("作者の覚書",
            "雨と聞いて、人はどんなイメージを持つだろうか",
            "日本は比較的雨が多く、また梅雨といった時期もある為に、好意的に解釈する人も多いだろう",
            "それでも雨は多くの人にとって悪い天気であり、生活に支障をもたらすものだ",
            "雨から考える物語はどこかしらウェットなものが増えるのかな、と予想する",
            "そんな中で今回は雨を拍手の音にたとえて、拍手喝采を浴びる難聴のピアニストの話を考えた",
            "嫌なものが最後には良いものに転化する",
            "こういった構造は、このコロナ禍で鬱屈した現在の中で、すっきりとした読後感を与えることだろう",
            "ただそういう物語においても、作者ながらのどこか痛みのある、一見すると救いようがない状況設定をしたい",
            "苦境の中でその希望にたどり着き、顔を上げる",
            "そういった物語こそが、凪司工房の物語であるからだ",
            )

def ch_main(w: World):
    return w.chapter('main',
            ep_runaway(w),
            ep_catchup(w),
            ep_getback(w),
            ep_mainstage(w),
            )

def ch_rireki(w: World):
    return w.chapter("履歴書",
            # 履歴書
            nt_maki(w),
            nt_sakai(w),
            )

def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_outline(f"{OUTLINE}")
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(ASSET)
    return w.run(
            ch_writernote(w),
            ch_main(w),
            ch_rireki(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

