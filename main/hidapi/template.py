pkgname = "hidapi"
pkgver = "0.14.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libusb-devel",
    "linux-headers",
    "udev-devel",
]
pkgdesc = "Cross-platform library for communicating with HID devices"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause OR custom:hidapi OR GPL-3.0-only"
url = "https://github.com/libusb/hidapi"
source = f"{url}/archive/refs/tags/hidapi-{pkgver}.tar.gz"
sha256 = "a5714234abe6e1f53647dd8cba7d69f65f71c558b7896ed218864ffcf405bcbd"


def post_install(self):
    self.install_license("LICENSE-bsd.txt")
    self.install_license("LICENSE-orig.txt")


@subpackage("hidapi-devel")
def _(self):
    return self.default_devel()
