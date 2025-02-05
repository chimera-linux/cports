pkgname = "libfido2"
pkgver = "1.15.0"
pkgrel = 0
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
    "openssl3-devel",
    "udev-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Library and tools for FIDO devices over USB or NFC"
maintainer = "Val Packett <val@packett.cool>"
license = "BSD-2-Clause"
url = "https://developers.yubico.com/libfido2"
source = (
    f"https://developers.yubico.com/libfido2/Releases/libfido2-{pkgver}.tar.gz"
)
sha256 = "abaab1318d21d262ece416fb8a7132fa9374bda89f6fa52b86a98a2f5712b61e"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libfido2-devel")
def _(self):
    return self.default_devel()


@subpackage("libfido2-progs")
def _(self):
    return self.default_progs()
