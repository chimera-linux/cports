pkgname = "pekwm"
pkgver = "0.3.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libxpm-devel",
    "libxft-devel",
    "libxinerama-devel",
    "libxrandr-devel",
    "fontconfig-devel",
]
pkgdesc = "Window manager based on aewm++"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.pekwm.se"
source = f"https://github.com/pekdon/pekwm/archive/release-{pkgver}.tar.gz"
sha256 = "8c501dba954395b558afb6776cbda7732da023d75ca18f4b04c22cf49a2e7507"
# FIXME cfi
hardening = ["vis", "!cfi"]
# no test target
options = ["!check"]
