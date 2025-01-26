pkgname = "fcitx5-skk"
pkgver = "5.1.6"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "extra-cmake-modules",
    "cmake",
    "gettext",
    "ninja",
    "pkgconf",
    "qt6-qtbase",
]
makedepends = [
    "fcitx5-devel",
    "fcitx5-qt-devel",
    "libskk-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "SKK wrapper for Fcitx5"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://fcitx-im.org"
source = (
    f"https://github.com/fcitx/fcitx5-skk/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "35bcf3ad63a33c92dbaea43c35638d0c54292aff1cb458fac5a75bcae3aa214c"
hardening = ["vis", "cfi"]
# fails
options = ["!cross"]
