pkgname = "calf"
pkgver = "0.90.3"
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
sha256 = "8781cbd1a81dec59b5923a23141ab2ca74e0e724389e15ffcf3820ace138a46c"
# vis breaks symbols
hardening = ["!vis"]
