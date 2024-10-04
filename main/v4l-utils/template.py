pkgname = "v4l-utils"
pkgver = "1.28.1"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dqv4l2=disabled", "-Dudevdir=/usr/lib/udev"]
hostmakedepends = [
    "bash",
    "gettext-devel",
    "meson",
    "perl",
    "pkgconf",
]
makedepends = [
    "argp-standalone",
    "glu-devel",
    "libjpeg-turbo-devel",
    "libx11-devel",
    "mesa-devel",
    "udev-devel",
]
pkgdesc = "Userspace tools and libraries for V4L"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://linuxtv.org/wiki/index.php/V4l-utils"
source = f"https://linuxtv.org/downloads/v4l-utils/v4l-utils-{pkgver}.tar.xz"
sha256 = "0fa075ce59b6618847af6ea191b6155565ccaa44de0504581ddfed795a328a82"
tool_flags = {"LDFLAGS": ["-largp"]}


@subpackage("v4l-utils-devel")
def _(self):
    return self.default_devel()
