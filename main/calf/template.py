pkgname = "calf"
pkgver = "0.90.8"
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
sha256 = "b6f9fe41fbfa5e2af0d1214bab9a2b56aa085d90868d4526f9b7886d1487a9c4"
# vis breaks symbols
hardening = ["!vis"]

if self.profile().arch == "ppc":
    tool_flags = {"CFLAGS": ["-DPFFFT_SIMD_DISABLE"]}


def post_install(self):
    # no executables
    self.uninstall("usr/share/bash-completion")
