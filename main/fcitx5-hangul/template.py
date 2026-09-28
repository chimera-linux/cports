pkgname = "fcitx5-hangul"
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
    "libhangul-devel",
]
pkgdesc = "Hangul Wrapper for Fcitx5"
license = "LGPL-2.1-or-later"
url = "https://fcitx-im.org"
source = (
    f"https://github.com/fcitx/fcitx5-hangul/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "86a1fc1cf5aa68a0717332901710e8fd32314dc35fc7d796b8ae45dcb3f3cd4f"
# CFI: causes illegal instruction crashes
hardening = ["vis", "!cfi"]
