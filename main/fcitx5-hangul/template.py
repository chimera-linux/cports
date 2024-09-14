pkgname = "fcitx5-hangul"
pkgver = "5.1.4"
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
sha256 = "49404de5de38f4b182e487e7a51a4a68fdb5b8acef531d27ba328aca552b9009"
# CFI: causes illegal instruction crashes
hardening = ["vis", "!cfi"]
