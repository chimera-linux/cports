pkgname = "fcitx5-lua"
pkgver = "5.0.18"
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
    "lua5.4-devel",
]
pkgdesc = "Lua support for Fcitx5"
license = "LGPL-2.1-or-later"
url = "https://fcitx-im.org"
source = (
    f"https://github.com/fcitx/fcitx5-lua/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "fb0695f7738a18ad63ae9228de71aa5f2bece35fe706a1d88cb170950e0b9036"
