pkgname = "fcitx5-hangul"
pkgver = "5.1.3"
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
sha256 = "44fa27b0d0168f9e41d24da3e0f3818e09c15c11f2f99261d13134bcef478e45"
# TODO cfi causes illegal instruction crashes
hardening = ["vis"]
