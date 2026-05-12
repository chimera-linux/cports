pkgname = "pekwm"
pkgver = "0.4.4"
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
license = "GPL-2.0-or-later"
url = "https://www.pekwm.se"
source = f"{url}/pekwm/uv/pekwm-{pkgver}.tar.gz"
sha256 = "8e794f094151fac9b85df2aaccf27add8cce5980f7eaf05b1caa8ab17b751aed"
hardening = ["vis", "!cfi"]
# no test target
options = ["!check"]


def post_install(self):
    self.mv(
        self.destdir / "usr/share/pekwm/scripts/pekwm_panel_sysinfo",
        self.destdir / "usr/bin/",
    )
