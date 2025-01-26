pkgname = "fcitx5-chewing"
pkgver = "5.1.7"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://fcitx-im.org"
source = (
    f"https://github.com/fcitx/fcitx5-chewing/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "a7b142f8ab638504eaddc08a8936cc614cfa6f588da288fa3582ed74ef08c64f"
