pkgname = "fcitx5-kkc"
pkgver = "5.1.5"
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
    "libkkc-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KKC wrapper for Fcitx5"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://fcitx-im.org"
source = (
    f"https://github.com/fcitx/fcitx5-kkc/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "4ea546788bb4088cfac84d1e364068bc951305c331380e27b835907e02399eaa"
hardening = ["vis", "cfi"]
