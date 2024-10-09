pkgname = "fcitx5-hangul"
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
    "libhangul-devel",
]
pkgdesc = "Hangul Wrapper for Fcitx5"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "LGPL-2.1-or-later"
url = "https://fcitx-im.org"
source = (
    f"https://github.com/fcitx/fcitx5-hangul/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "46728e38f501c81402f4824a429793d85ab7e592c9dfb738a21d85cb2f5d34a4"
# CFI: causes illegal instruction crashes
hardening = ["vis", "!cfi"]
