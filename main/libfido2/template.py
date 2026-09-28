pkgname = "libfido2"
pkgver = "1.16.0"
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
license = "BSD-2-Clause"
url = "https://developers.yubico.com/libfido2"
source = (
    f"https://developers.yubico.com/libfido2/Releases/libfido2-{pkgver}.tar.gz"
)
sha256 = "8c2b6fb279b5b42e9ac92ade71832e485852647b53607c43baaafbbcecea04e4"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libfido2-devel")
def _(self):
    return self.default_devel()


@subpackage("libfido2-progs")
def _(self):
    return self.default_progs()
