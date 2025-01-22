pkgname = "uqm"
pkgver = "0.8.0"
pkgrel = 0
build_style = "meson"
meson_dir = "sc2"
hostmakedepends = ["meson", "ninja", "pkgconf"]
makedepends = [
    "libmikmod-devel",
    "libpng-devel",
    "libvorbis-devel",
    "sdl2-compat-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Port of Star Control 2"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://sc2.sourceforge.net"
source = (
    f"https://github.com/z-erica/sc2-uqm/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "bf65c4346ed316800e45f67805a14cf22bf96bb7585a5e42ad4999176b8301ed"
