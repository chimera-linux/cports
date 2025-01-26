pkgname = "fcitx5-kkc"
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
    "libkkc-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KKC wrapper for Fcitx5"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://fcitx-im.org"
source = (
    f"https://github.com/fcitx/fcitx5-kkc/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "87cfa16ed6547106bbde90afc7de3b61a0fd0e1a931bdfde312afa1172ccd430"
hardening = ["vis", "cfi"]
