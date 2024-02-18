pkgname = "libfido2"
pkgver = "1.14.0"
pkgrel = 2
build_style = "cmake"
configure_args = [
    "-DBUILD_EXAMPLES=OFF",
    "-DBUILD_STATIC_LIBS=OFF",
    "-DUDEV_RULES_DIR=",  # handled by systemd-udev
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libcbor-devel",
    "linux-headers",
    "openssl-devel",
    "udev-devel",
    "zlib-devel",
]
pkgdesc = "Library and tools for FIDO devices over USB or NFC"
maintainer = "Val Packett <val@packett.cool>"
license = "BSD-2-Clause"
url = "https://developers.yubico.com/libfido2"
source = (
    f"https://developers.yubico.com/libfido2/Releases/libfido2-{pkgver}.tar.gz"
)
sha256 = "3601792e320032d428002c4cce8499a4c7b803319051a25a0c9f1f138ffee45a"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libfido2-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libfido2-progs")
def _progs(self):
    return self.default_progs()
