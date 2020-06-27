# -*- coding: utf-8 -*-
'''
Stage: "堺田のマンション"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def he_is_composer(w: World):
    maki, sakai = w.get('maki'), w.get('sakai')
    return w.scene('彼は作曲家',
            "マンション外観。割と高級住宅街にある",
            maki.come("男のマンションに入ってくる$S"),
            sakai.come("鍵を開けて部屋に入る"),
            "内装は小奇麗、物が少ないが、散らかっている",
            maki.do("広いリビングにはグランドピアノがあり、床に書きかけた譜面が散らばっている"),
            sakai.talk("散らかっていてごめんよ"),
            maki.do("譜面を見る", "それを弾いてみる$S"),
            "説明よりも描写で知らせる",
            sakai.talk("譜面が読めるのか"),
            maki.talk("これ、続きは？"),
            sakai.talk("ないよ"),
            sakai.explain("$Sは作曲家だけど作曲できなくなったと説明する"),
            sakai.talk("難聴でね"),
            sakai.do("彼は補聴器を$makiに見せて苦笑する"),
            maki.talk("おんなじだ"),
            maki.do("と笑う$S"),
            maki.talk("弾いていい？"),
            maki.do("外は夜", "いつもなら大嫌いな家に帰らなければいけない"),
            sakai.talk("いいよ", "ここは防音もちゃんとしている", "それより何か食べたいものある？"),
            sakai.do("$Sは$makiにメモに走り書きしたのを見せて尋ねる"),
            maki.talk("ラーメン", "お湯注ぐやつ"),
            sakai.talk("カップ麺はないなあ", "何か適当に出前を取るよ"),
            maki.do("ピアノを弾き始める$S", "楽しくて笑顔になる"),
            outline="$makiを拾った男の家にはピアノがあった。元作曲家だという")

def alms_giving(w: World):
    maki, sakai = w.get('maki'), w.get('sakai')
    return w.scene("男の施し",
            sakai.talk("そんなに気に入ったならいつでも遊びにくればいい"),
            maki.talk("ほんとに？", "ピアノ弾いても怒らない？"),
            sakai.talk("ここはその為の部屋だからね"),
            sakai.do("合鍵を$makiに渡した"),
            "合鍵の形を詳細描写",
            outline="ピアノを失った$makiに男はいつでも遊びにきてピアノを弾けばいいと言ってくれた")

def lostman(w: World):
    maki, sakai = w.get('maki'), w.get('sakai')
    return w.scene("失った男",
            maki.be("家に遊びにきている$S"),
            sakai.come("出前を持ってやってくる"),
            "$makiにとってのご馳走が、ピザやハンバーガーなんかだと分からせる。あとコーラとかのジャンクフード系",
            sakai.talk("ピザなんて久しぶりに食べるよ"),
            maki.do("$sakaiが話すのも気にせず、ピアノを触っている$S"),
            sakai.talk("飲み物はオレンジジュースでいいんだっけ？"),
            "$sakaiがアルコールを飲まないことに$makiは嬉しくなること",
            maki.do("$sakaiがコップに注いだのを見て適当に頷く"),
            maki.do("ピアノを弾くのを中断して、テーブルにやってくる$S"),
            sakai.do("$makiが難聴気味なのをいいことに、ピザを食べる彼女に向けて独り言を話し始める$S"),
            sakai.talk("$meの母親はフルート奏者でね、いつも世界の色々な街に行っては音楽と会話していた",
                "だから$meにとって音というのは空気みたいなものだったんだ",
                "気がついたら作曲をするようになっていたよ"),
            sakai.talk("大学で専門的な勉強もしたけれど、そこには$meと同じように音のことを考えている人間はいなかった",
                "どちらかといえば仕事として、あるいは技術としての音、あるいは音楽というものを考え、実践している人ばかりで、",
                "結局友達は音楽だけだったよ"),
            sakai.talk("それがある日突然、失われた",
                "突発性難聴という言葉は聞いたことがあったが、それがまさか自分に降り掛かってくるなんて思ってもなかったよ"),
            sakai.talk("結局戻ったのは僅かな聴力で、作曲することもできず、音は$meの世界から遠ざかってしまった"),
            sakai.talk("駅前にピアノを寄付したのは$meなんだ",
                "そのピアノを楽しそうに弾く君を見て、一度話してみたいと思っていた"),
            sakai.talk("いつかまた$meが曲を書けたら、その曲を君に弾いてもらいたい"),
            maki.talk("いいよ"),
            maki.do("$Sは笑顔で承諾し、ピザを口に入れた"),
            outline="$sakaiは大切なものを失ったと、説明した")

def falldown(w: World):
    maki, sakai = w.get('maki'), w.get('sakai')
    return w.scene("倒れる男",
            maki.come("セーラー服を着たまま、家へとやってくる"),
            maki.do("合鍵を使い、するすると中に入る"),
            maki.do("なんか妙な感じがする"),
            maki.do("玄関でインタフォンを押すけど反応がない",
                "補聴器を外しているんだと思って入る"),
            maki.do("声を掛けるけれど何も反応がない"),
            maki.do("リビングにはいない", "ただピアノがあるだけだ",
                "そこには新曲の楽譜が完成していた"),
            maki.talk("ねえ、これって"),
            maki.do("と、寝室のドアが開いているのに気づいた"),
            maki.do("寝室に入る"),
            maki.do("そこには倒れたまま動かなくなっている$sakaiがいた"),
            maki.do("$Sはどうすればいいか分からず立ち尽くしていたが、はっとして電話を手に取る"),
            maki.talk("あの、助けて下さい！"),
            maki.do("慌てて電話をした先は警察だった"),
            outline="ある日、$sakaiの部屋に入ると、彼が倒れていた")
