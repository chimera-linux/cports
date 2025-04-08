pkgname = "calf"
pkgver = "0.90.6"
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
sha256 = "e9e58f2b35177765be756987787079730579f351fa5ccf0fd2405ceab4da036d"
# vis breaks symbols
hardening = ["!vis"]

if self.profile().arch == "ppc":
    tool_flags = {"CFLAGS": ["-DPFFFT_SIMD_DISABLE"]}


def post_install(self):
    # no executables
    self.uninstall("usr/share/bash-completion")
