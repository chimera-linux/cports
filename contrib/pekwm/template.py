pkgname = "pekwm"
pkgver = "0.2.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "libjpeg-turbo-devel", "libpng-devel", "libxpm-devel", "libxft-devel",
    "libxinerama-devel", "libxrandr-devel", "fontconfig-devel",
]
pkgdesc = "Window manager based on aewm++"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.pekwm.se"
source = f"https://github.com/pekdon/{pkgname}/archive/release-{pkgver}.tar.gz"
sha256 = "62e858015e1a5a54bbddab202a1fb455c821bda62498e9cadfa1d00a5a2575c3"
# no test target
options = ["!check"]

# FIXME visibility
hardening = ["!vis"]
