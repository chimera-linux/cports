pkgname = "activate-linux"
pkgver = "1.1.0"
pkgrel = 1
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
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = 'Linux port of the "Activate Windows" watermark'
license = "GPL-3.0-only"
url = "https://github.com/MrGlockenspiel/activate-linux"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "cf892c90a57bf6026f777715207aa7066fc7c4940da39d62a6c24b51a726786d"
hardening = ["vis", "cfi"]
# No test suite
options = ["!check"]
