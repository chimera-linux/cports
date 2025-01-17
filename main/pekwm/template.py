pkgname = "pekwm"
pkgver = "0.3.2"
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
sha256 = "cf5e61a753f1a125877c65477ffd9b76b1aa6cec0f241f1fd6af9159dd23bfdf"
hardening = ["vis", "!cfi"]
# no test target
options = ["!check"]
