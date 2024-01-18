pkgname = "ddcutil"
pkgver = "2.1.0"
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
sha256 = "c0bf89fcff98c6c3755b328c6fc01617b860ef7e067174f589afa1da5bc4129b"
# breaks symbols
hardening = ["!vis"]
# no tests
options = ["!check"]


@subpackage("ddcutil-devel")
def _devel(self):
    return self.default_devel()
