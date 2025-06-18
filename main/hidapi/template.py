pkgname = "hidapi"
pkgver = "0.15.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
]
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
license = "BSD-3-Clause OR custom:hidapi OR GPL-3.0-only"
url = "https://github.com/libusb/hidapi"
source = f"{url}/archive/refs/tags/hidapi-{pkgver}.tar.gz"
sha256 = "5d84dec684c27b97b921d2f3b73218cb773cf4ea915caee317ac8fc73cef8136"


def post_install(self):
    self.install_license("LICENSE-bsd.txt")
    self.install_license("LICENSE-orig.txt")


@subpackage("hidapi-devel")
def _(self):
    return self.default_devel()
