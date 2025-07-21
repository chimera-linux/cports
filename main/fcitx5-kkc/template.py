pkgname = "fcitx5-kkc"
pkgver = "5.1.7"
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
    "libkkc-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KKC wrapper for Fcitx5"
license = "GPL-3.0-or-later"
url = "https://fcitx-im.org"
source = (
    f"https://github.com/fcitx/fcitx5-kkc/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "fa9010cee4832895fb582db948561921fce9090b9a010684f0218f89c166e7ca"
hardening = ["vis", "cfi"]
