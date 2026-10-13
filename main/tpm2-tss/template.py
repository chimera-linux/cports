pkgname = "tpm2-tss"
pkgver = "4.2.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-unit",
    "--runstatedir=/run",
    "--with-crypto=ossl",
    "--with-tctidefaultmodule=device",
    "--with-tctidefaultconfig=/dev/tpmrm0",
]
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "cmocka",
    "perl",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "cmocka-devel",
    "curl-devel",
    "json-c-devel",
    "libftdi1-devel",
    "libusb-bootstrap",
    "linux-headers",
    "openssl3-devel",
    "util-linux-uuid-devel",
]
pkgdesc = "Implementation of TCG TPM2"
license = "BSD-2-Clause"
url = "https://github.com/tpm2-software/tpm2-tss"
source = f"{url}/releases/download/{pkgver}/tpm2-tss-{pkgver}.tar.gz"
sha256 = "b53f0c5c8c4ce17f05701a410ca9688f725ca380c9bc4640eacd0eadb1fea124"
options = ["etcfiles"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("tpm2-tss-devel")
def _(self):
    return self.default_devel()
