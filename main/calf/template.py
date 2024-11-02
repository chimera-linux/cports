pkgname = "calf"
pkgver = "0.90.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-experimental",
    "--disable-static",
]
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "fluidsynth-devel",
    "libexpat-devel",
    "lv2",
]
pkgdesc = "Calf Studio Gear audio plugins"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.0-or-later"
url = "https://calf-studio-gear.org"
source = f"https://github.com/calf-studio-gear/calf/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "60ddef9062d92b245c71e9e8a565fbaaf015a5973eaebed615e0f63c89a14f8f"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    # no executables
    self.uninstall("usr/share/bash-completion")
