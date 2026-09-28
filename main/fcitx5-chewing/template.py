pkgname = "fcitx5-chewing"
pkgver = "5.1.8"
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
license = "LGPL-2.1-or-later"
url = "https://fcitx-im.org"
source = (
    f"https://github.com/fcitx/fcitx5-chewing/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "cd82f808303834f089e70277e214cb17d02f5b60c352182e75c88b69bc2708cc"
