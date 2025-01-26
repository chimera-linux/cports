pkgname = "fcitx5-hangul"
pkgver = "5.1.6"
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
sha256 = "320ddd9f5832b94f0ae5edd914de25ad63c8c3af176d6d00ae4e130341610970"
# CFI: causes illegal instruction crashes
hardening = ["vis", "!cfi"]
