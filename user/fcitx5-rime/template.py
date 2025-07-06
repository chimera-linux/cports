pkgname = "fcitx5-rime"
pkgver = "5.1.11"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DRIME_DATA_DIR=/usr/share/rime-data"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "fcitx5-devel",
    "gettext-devel",
    "librime-devel",
]
depends = ["librime-data"]
pkgdesc = "RIME support for Fcitx5"
license = "LGPL-2.1-or-later"
url = "https://github.com/fcitx/fcitx5-rime"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "3f3e69cd46ab1b955d1470876da405333e954ca6df198894fa17c1a7c0fd2b88"
