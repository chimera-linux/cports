pkgname = "fcitx5-skk"
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
    "libskk-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "SKK wrapper for Fcitx5"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://fcitx-im.org"
source = (
    f"https://github.com/fcitx/fcitx5-skk/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "381778153abf93bfc13aeb164b0fa5606ea5e0f53ed401babb1a4f2a530d120b"
hardening = ["vis", "cfi"]
# fails
options = ["!cross"]
