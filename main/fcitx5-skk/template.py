pkgname = "fcitx5-skk"
pkgver = "5.1.11"
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
sha256 = "aae6a77a36ee3f4ccf20aed7fbec98290afeb66ba48c1b2e7ae71321ed84d66d"
hardening = ["vis", "cfi"]
# fails
options = ["!cross"]
