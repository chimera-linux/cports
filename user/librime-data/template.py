pkgname = "librime-data"
pkgver = "0_git20260717"
pkgrel = 0
build_style = "makefile"
make_build_target = "preset-bin"
hostmakedepends = ["bash", "librime-progs"]
pkgdesc = "Rime input schema"
license = "LGPL-3.0-or-later"
_plum = "b1be1969f914cc005add4090631b855db00c2591"  # r127.20260508
_bopomofo = "6085c9a38a4a728047862b33d67eee18aa86f3b9"  # r68.20260509
_cangjie = "52d90a1b1312e74042b38c1cbc8142defbc53171"  # r77.20260601
_essay = "e9b1a374a6ea015fca5bdd04318924b4483ac35a"  # r312.20260713
_quick = "5dcdb9e353d314239e9c8cddc0f42d52da4837bb"  # r46.20260717
_luna_pinyin = "56b934b099dfbeab842320f13aa8b461a6ab3e42"  # r350.20260712
_prelude = "082425ea0684bca36474415d4a0e8db9b016487e"  # r164.20260509
_stroke = "3a4b0f4013e2b4c14b1e80c92b1d4723eb65f39c"  # r59.20250923
_terra_pinyin = "8a2c895ad7ee8e2b137d91be77f18f86b04d7fc9"  # r279.20260717
url = "https://github.com/rime/plum"
source = [
    f"https://github.com/rime/plum/archive/{_plum}.tar.gz",
    f"https://github.com/rime/rime-bopomofo/archive/{_bopomofo}.tar.gz",
    f"https://github.com/rime/rime-cangjie/archive/{_cangjie}.tar.gz",
    f"https://github.com/rime/rime-essay/archive/{_essay}.tar.gz",
    f"https://github.com/rime/rime-quick/archive/{_quick}.tar.gz",
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
    "package/rime/quick",
    "package/rime/luna-pinyin",
    "package/rime/prelude",
    "package/rime/stroke",
    "package/rime/terra-pinyin",
]
sha256 = [
    "4ebc2bec937766184546f9c0598f90a692a2e0ef1a50c0c2e594dbb3e131f61e",
    "5fc0719e8fe9b2eb8aa05c505ffb2b39d972e637951531182dd7d745a83bda51",
    "18d989bf21d0bb86b402f18be4dd060bf2653896c95448afb01d4da2e6be5464",
    "11559224d48709b0d77009a550804bfc2b763cfdf048c8d8fe224b3d36ba441c",
    "2f2ae291b1ebd17ad5bfccfabbeb3aba2a466589628f15172da5fc76b24b9f7e",
    "876c7ba559794f476abf7195a255aea29000cee281e6f5ec664928dce018bd90",
    "66239ba4745d54471e5ce5540b45e86ec663ff5dba004cb23c95531a3bdec00f",
    "14995408f49a8389bbcc50b8865ec8d1d90c26517cdb33f69b4a69b8a5d2ddb8",
    "7507d3f00d0219f49e538653af1c8462345d0b2e691616145072e5c34584e621",
]
# No tests are available.
options = ["!check"]
