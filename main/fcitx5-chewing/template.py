pkgname = "fcitx5-chewing"
pkgver = "5.1.5"
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
sha256 = "252c5662fd1fb543cfd4f99b467766f235b1ddc0fe60839c10af900337a047c8"
