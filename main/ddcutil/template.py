pkgname = "ddcutil"
pkgver = "2.1.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-x11"]
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
    "linux-headers",
    "udev-devel",
]
pkgdesc = "Control monitor settings using DDC/CI and USB"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.ddcutil.com"
source = (
    f"https://github.com/rockowitz/ddcutil/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "cd8325d399399edba3df4ec58a4051c7c54fcf4fbc8f62937c6f19adb303f4ba"
# breaks symbols
hardening = ["!vis"]
# no tests
options = ["!check"]


@subpackage("ddcutil-devel")
def _(self):
    return self.default_devel()
