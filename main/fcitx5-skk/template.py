pkgname = "fcitx5-skk"
pkgver = "5.1.10"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
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
license = "GPL-3.0-or-later"
url = "https://fcitx-im.org"
source = (
    f"https://github.com/fcitx/fcitx5-skk/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "ac8a2c75284c6d7ba81145df43bf531c08af4616d45703490a2e8e7bfbab731d"
hardening = ["vis", "cfi"]
# fails
options = ["!cross"]
