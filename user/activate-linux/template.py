pkgname = "activate-linux"
pkgver = "1.2.0"
pkgrel = 0
build_style = "makefile"
hostmakedepends = [
    "gawk",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "cairo-devel",
    "libconfig-devel",
    "libx11-devel",
    "libxfixes-devel",
    "libxinerama-devel",
    "libxrandr-devel",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = 'Linux port of the "Activate Windows" watermark'
license = "GPL-3.0-only"
url = "https://github.com/MrGlockenspiel/activate-linux"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "5c1ab8dc9ddfc3984398f410cd5cf6169609650659d9474b88b1d852a1c3c32b"
hardening = ["vis", "cfi"]
# No test suite
options = ["!check"]
