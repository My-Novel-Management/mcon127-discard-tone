# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
            ('maki', '真希', '灰村,真希', 17,(1,1), 'female', '学生', 'me:私'),
            ('sakai', '堺田', '堺田,良樹', 40,(1,1), 'male', '元作曲家', 'me:僕'),
            ('mam', '真希の母', '', 37,(1,1), 'female', 'パート',),
            ('dad', '茂男', '灰村,茂男', 45,(1,1), 'male', '場末のピアニスト', 'me:俺'),
            ('yayoi', '弥生', '浜野,弥生', 57,(9,10), 'female', '飲み屋店主', 'me:あたし'),
            ('soda', '想田', '', 30,(1,1), 'male', 'バイト'),
            ("police", '警官', '', 30,(1,1), 'male', '警察官'),
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
            ('sakaihome', '堺田の家', 'Tokyo'),
            ),
        "DAYS": (
            # (tag / name / month / day / year)
            ),
        "TIMES": (
            # (tag / name / hour / minute)
            ),
        "ITEMS": (
            # (tag / name / cate / info)
            ),
        "WORDS": (
            # (tag / name / cate / info)
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ),
        }

