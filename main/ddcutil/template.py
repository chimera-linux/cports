pkgname = "ddcutil"
pkgver = "2.2.0"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "jansson-devel",
    "kmod-devel",
    "libdrm-devel",
    "libusb-devel",
    "libx11-devel",
    "libxext-devel",
    "libxrandr-devel",
    "linux-headers",
    "udev-devel",
]
pkgdesc = "Control monitor settings using DDC/CI and USB"
license = "GPL-2.0-or-later"
url = "https://www.ddcutil.com"
source = (
    f"https://github.com/rockowitz/ddcutil/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "2a9a994b885974423a5b765aaa2c17159f7341881d15f9cb430c0bf1842185ee"
# breaks symbols
hardening = ["!vis"]
# no tests
options = ["!check"]


@subpackage("ddcutil-devel")
def _(self):
    return self.default_devel()
