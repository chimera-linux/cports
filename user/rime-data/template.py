pkgname = "rime-data"
pkgver = "0.20250123"
pkgrel = 0
build_style = "makefile"
make_build_target = "preset-bin"
hostmakedepends = ["bash", "rime-progs"]
pkgdesc = "Rime input schema"
maintainer = "Bin Jin <bjin@protonmail.com>"
license = "LGPL-3.0-or-later"
_plum = "4c28f11f451facef809b380502874a48ba964ddb"  # r126.20240417
_bopomofo = "c7618f4f5728e1634417e9d02ea50d82b71956ab"  # r59.20210131
_cangjie = "0ac8452eeb4abbcd8dd1f9e7314012310743285f"  # r73.20240325
_essay = "4dfd95ab166d542a10647753d17ce83126f70ff6"  # r265.20250121
_luna_pinyin = "d2107f46dbffbe069b10072925be3c18da40fe77"  # r290.20250123
_prelude = "3803f09458072e03b9ed396692ce7e1d35c88c95"  # r154.20240519
_stroke = "7c9874c6b2e0b94947653e9a7de6f99623ff27e4"  # r56.20250118
_terra_pinyin = "333ec4128fa1f93924a0707da3c623ccd92a73f0"  # r270.20241225
url = "https://github.com/rime/plum"
source = [
    f"https://github.com/rime/plum/archive/{_plum}.tar.gz",
    f"https://github.com/rime/rime-bopomofo/archive/{_bopomofo}.tar.gz",
    f"https://github.com/rime/rime-cangjie/archive/{_cangjie}.tar.gz",
    f"https://github.com/rime/rime-essay/archive/{_essay}.tar.gz",
    f"https://github.com/rime/rime-luna-pinyin/archive/{_luna_pinyin}.tar.gz",
    f"https://github.com/rime/rime-prelude/archive/{_prelude}.tar.gz",
    f"https://github.com/rime/rime-stroke/archive/{_stroke}.tar.gz",
    f"https://github.com/rime/rime-terra-pinyin/archive/{_terra_pinyin}.tar.gz",
]
source_paths = [
    ".",
    "package/rime/bopomofo",
    "package/rime/cangjie",
    "package/rime/essay",
    "package/rime/luna-pinyin",
    "package/rime/prelude",
    "package/rime/stroke",
    "package/rime/terra-pinyin",
]
sha256 = [
    "121d5a405dd1457582609d2a4cc0c6c55f9ada8750e524b5c0b6585dbc5268c8",
    "37bc156bca8bca93b001b112ee440fc498207a4f6fbcaa2d2c306cfdd4560577",
    "7fea467b08aeb38b0ebc6260a086f11578615549b1ac423bd4a5c6734ccf1ea8",
    "4f3790789d4df57f558779d3bcb255b2cc682dd2ad704411d0b59491c3a08a16",
    "d90301fa9a9d7a8721221b06bba45bec1071c59c8fbcc06e3f25cb9d695ef62c",
    "afa07cd98c540a0ac2d1d6e98ffa776549c535e617d3e41eb6ef80806df806f2",
    "9728b1123640a699b9032855a8b261928077278fa1870407c50f53c71cb82f74",
    "5f94ac60a156ee45c7a01598af3a1bdc7b829e2c1d75da590a9ae024bb3c49dd",
]
# No tests are available.
options = ["!check"]
