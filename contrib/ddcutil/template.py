pkgname = "ddcutil"
pkgver = "2.1.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-x11"]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "libtool",
    "gmake",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "jansson-devel",
    "libdrm-devel",
    "libkmod-devel",
    "libusb-devel",
    "linux-headers",
    "udev-devel",
]
pkgdesc = "Control monitor settings using DDC/CI and USB"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://www.ddcutil.com"
source = (
    f"https://github.com/rockowitz/ddcutil/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "911d3b712b485527a65def57538fbdb5e83779a0cd6e1e4746672d90b558680a"
# breaks symbols
hardening = ["!vis"]
# no tests
options = ["!check"]


@subpackage("ddcutil-devel")
def _devel(self):
    return self.default_devel()
