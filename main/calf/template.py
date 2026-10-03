pkgname = "calf"
pkgver = "0.90.9"
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
sha256 = "2d304eed88e87438b2b8857a2f4480046bf4003bce2e17a042abdbbf7d59122f"
# vis breaks symbols
hardening = ["!vis"]

if self.profile.arch == "ppc":
    tool_flags = {"CFLAGS": ["-DPFFFT_SIMD_DISABLE"]}


def post_install(self):
    # no executables
    self.uninstall("usr/share/bash-completion")
