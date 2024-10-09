pkgname = "fcitx5-chewing"
pkgver = "5.1.6"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "fcitx5-devel",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "fcitx5-devel",
    "libchewing-devel",
]
pkgdesc = "Chewing Wrapper for Fcitx5"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later"
url = "https://fcitx-im.org"
source = (
    f"https://github.com/fcitx/fcitx5-chewing/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "9701122b2a0a984eb2dc976a03d4243de6a403844bf02647cb14f4669cf684f5"
