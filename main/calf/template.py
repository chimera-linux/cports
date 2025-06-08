pkgname = "calf"
pkgver = "0.90.7"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "fluidsynth-devel",
    "libexpat-devel",
    "lv2",
]
pkgdesc = "Calf Studio Gear audio plugins"
license = "LGPL-2.0-or-later"
url = "https://calf-studio-gear.org"
source = f"https://github.com/calf-studio-gear/calf/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e8ea276d9fd8a3dfe45e13cf6d0bd034150cf7de99473441d99ce1c89ab39978"
# vis breaks symbols
hardening = ["!vis"]

if self.profile().arch == "ppc":
    tool_flags = {"CFLAGS": ["-DPFFFT_SIMD_DISABLE"]}


def post_install(self):
    # no executables
    self.uninstall("usr/share/bash-completion")
