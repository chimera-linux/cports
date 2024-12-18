pkgname = "tpm2-tss"
pkgver = "4.1.3"
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
    "automake",
    "cmocka",
    "libltdl-devel",  # ltdl.m4
    "libtool",
    "perl",
    "pkgconf",
]
makedepends = [
    "cmocka-devel",
    "json-c-devel",
    "curl-devel",
    "libftdi1-devel",
    "libuuid-devel",
    "libusb-bootstrap",
    "linux-headers",
    "openssl-devel",
]
pkgdesc = "Implementation of TCG TPM2"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/tpm2-software/tpm2-tss"
source = f"{url}/releases/download/{pkgver}/tpm2-tss-{pkgver}.tar.gz"
sha256 = "37f1580200ab78305d1fc872d89241aaee0c93cbe85bc559bf332737a60d3be8"


def post_install(self):
    self.install_license("LICENSE")
    self.rename("etc/tmpfiles.d", "usr/lib", keep_name=True, relative=False)
    self.rename("etc/sysusers.d", "usr/lib", keep_name=True, relative=False)


@subpackage("tpm2-tss-devel")
def _(self):
    return self.default_devel()
