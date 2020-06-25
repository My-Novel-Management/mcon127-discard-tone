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
# from scenes import xxx


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
            w.plot_note("小さい頃からピアノだけが友人だった$makiは、周囲とは馴染めず、心と耳を閉ざしていく","徐々に学校をサボるようになった"),
            w.plot_note("学校を抜け出していつも遊びに行ったピアノを自宅に持っている元音大生の$yayoiが、ある時結婚してしまい、$makiは行き場を失った"),
            w.plot_note("駅前に現れた誰でも弾けるピアノを弾いていたが、それすらも親に奪われてしまう"),
            w.plot_note("その日、$makiの耳は突然聞こえなくなった", "ショックを受けた彼女は家出をする"),
            )

def ep_catchup(w: World):
    return w.episode('掃き溜めから拾った男',
            "本物の雨の中で、拾われる",
            w.plot_note("生きるために$makiはパパ活をしようとする"),
            w.plot_note("だがうまくはいかず、自暴自棄になっていた$makiを拾った男$sakaiは、全てを失った元作曲家だった"),
            w.plot_note("難聴だという$sakaiは$makiに自由にピアノを弾かせてくれた"),
            w.plot_note("突発性難聴の原因はよく分かっていないが、血流との関係が問題視されている等と教わる"),
            "脳梗塞を十年後に起こす可能性が高いらしい＞突発性難聴",
            w.plot_note("「このままペットみたいにあなたが飼ってくれたらいいのに」と言い出す$makiは、それでも$sakaiといつか家に帰る約束をさせられた"),
            )

def ep_getback(w: World):
    return w.episode('取り戻す',
            "なぜ彼女は彼の為にその楽譜を弾くのか？",
            w.plot_note("彼の為に一度は捨てた音を取り戻し、$makiはピアノの練習をする"),
            "また逃げ出そうとする$maki",
            w.plot_note("彼は脳梗塞で亡くなってしまった"),
            w.plot_note("家族に引き取られ、$makiは$sakaiに誘拐監禁されていたことになり、世間で彼は犯罪者扱いされた"),
            )

def ep_mainstage(w: World):
    return w.episode('メインステージ',
            "大切な人のために弾いたピアノが、自分を蔑んだりした、または$makiが敵視した人々の心を動かして拍手の雨を呼んだ",
            w.plot_note("彼へと捧げる彼の曲を、駅前のピアノで弾き始める$maki"),
            w.plot_note("そのピアノの音色が彼女が否定した世間から注目を集めるようになる"),
            w.plot_note("$makiはピアノを弾く", "何も聞こえないはずの彼女に、雨の音がした", "それは観衆の拍手の雨だった"),
            )

# TODO: あとで人物履歴に修正すること。今回は間に合わないのでエピソードで作ってomitします
def nt_maki(w: World):
    return w.episode('$makiの履歴書',
            "公務員の父とフルート奏者の母の下に生まれる",
            "生まれた頃から音に対して過敏なところを見せる",
            "三才の時におもちゃのピアノを買ってもらい、それで一日遊んでいて父に叱られた",
            "英会話やスイミングスクールには興味を示さなかったが、ピアノ教室だけは行きたがり、両親に頼み込んだ",
            "小学校に入り、周囲と馴染めず、一人で音楽室に忍び込んでピアノを弾いているところを先生に注意された",
            "学校でも問題になり、親にピアノを取り上げられた",
            "それでもピアノが弾きたくて近所の音大卒のお姉さん($yayoi)の家に入り浸った",
            "高校は地元の県立高校に入れたものの、サボりがちで、アルバイトをしつつ",
            "$yayoiが結婚して遠くに行ってしまうことで、ピアノが失われた",
            "駅前に誰でもひいていいピアノが置かれて、そこに通うようになる",
            "夜中にも弾いていたのを警官に補導され、両親から部屋に閉じ込められた",
            "荷物をまとめて家を飛び出したが、どうすればいいか途方にくれる",
            )

def nt_sakai(w: World):
    return w.episode('$sakaiの履歴書',
            "母親に出ていかれて、バイトでジャズ喫茶のピアノを弾いている父親の下で育つ",
            "いつもヤニとアルコールの臭いに囲まれた中で、音楽に囲まれながら、店に入れ替わり立ち代わりやってくる人妻の母乳やミルクで大きくなる",
            "物心ついた頃には鼻歌で自作の曲を作り、小学校から帰ると父親のバイト先で夕方までピアノを弾かせてもらった",
            "音大に行きたいと中学の頃から思うようになり、自分でアルバイトをして金を稼ぐ",
            "音大では周囲となじまなかったが、その天才的な作曲センスにより頭角を表した",
            "紐基質で女には困らなかったが、あまり性的なことに関心がなく、いつもピアノに向かって作曲しているような学生生活だった",
            "大学三年の時に作曲コンクールで入賞し、そこから作曲家としての人生が始まる",
            "しかし突発性難聴から、音が聞こえなくなり、作曲家としての人生を諦めた",
            "若い頃にいくつか売れた曲と、投資での生活",
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
            ch_main(w),
            ch_rireki(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

