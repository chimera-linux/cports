pkgname = "fcitx5-rime"
pkgver = "5.1.10"
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
sha256 = "187bab094b553517b18148b8be1878b63dd2d7e6509fb5ef031a75604f147170"
