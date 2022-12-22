pkgname = "v4l-utils"
pkgver = "1.22.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-qv4l2", "--with-udevdir=/usr/lib/udev"
]
make_cmd = "gmake"
hostmakedepends = [
    "gmake", "automake", "libtool", "pkgconf", "gettext-tiny-devel"
]
makedepends = [
    "libjpeg-turbo-devel", "sysfsutils-devel", "eudev-devel",
    "libx11-devel", "mesa-devel", "glu-devel", "argp-standalone",
]
pkgdesc = "Userspace tools and libraries for V4L"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://linuxtv.org/wiki/index.php/V4l-utils"
source = f"http://linuxtv.org/downloads/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "65c6fbe830a44ca105c443b027182c1b2c9053a91d1e72ad849dfab388b94e31"
tool_flags = {
    "CFLAGS": ["-D__off_t=off_t", "-D__off64_t=off_t"],
    "LDFLAGS": ["-largp"],
}

def pre_configure(self):
    self.do("autoreconf", "-if")

@subpackage("v4l-utils-devel")
def _devel(self):
    return self.default_devel()

# FIXME visibility
hardening = ["!vis"]
