pkgname = "pekwm"
pkgver = "0.3.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "fontconfig-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libxft-devel",
    "libxinerama-devel",
    "libxpm-devel",
    "libxrandr-devel",
    "pango-devel",
]
pkgdesc = "Window manager based on aewm++"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.pekwm.se"
source = f"https://github.com/pekdon/pekwm/archive/release-{pkgver}.tar.gz"
sha256 = "965e25982ebc428ae75cece68cd3ae6f0287c8dc3511b3f94c64f849d047e0cc"
hardening = ["vis", "!cfi"]
# no test target
options = ["!check"]
