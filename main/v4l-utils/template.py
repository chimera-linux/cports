pkgname = "v4l-utils"
pkgver = "1.26.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dqv4l2=disabled", "-Dudevdir=/usr/lib/udev"]
hostmakedepends = ["bash", "gettext-devel", "meson", "perl", "pkgconf"]
makedepends = [
    "libjpeg-turbo-devel",
    "udev-devel",
    "libx11-devel",
    "mesa-devel",
    "glu-devel",
    "argp-standalone",
]
pkgdesc = "Userspace tools and libraries for V4L"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://linuxtv.org/wiki/index.php/V4l-utils"
source = f"https://linuxtv.org/downloads/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "4a71608c0ef7df2931176989e6d32b445c0bdc1030a2376d929c8ca6e550ec4e"
tool_flags = {"LDFLAGS": ["-largp"]}


@subpackage("v4l-utils-devel")
def _devel(self):
    return self.default_devel()
