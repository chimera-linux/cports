pkgname = "libp11"
pkgver = "0.4.18"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
hostmakedepends = ["automake", "pkgconf", "slibtool"]
makedepends = ["openssl3-devel", "pkcs11-helper-devel"]
pkgdesc = "Library implementing a layer between OpenSSL and PKCS#11"
license = "LGPL-2.1-or-later"
url = "https://github.com/OpenSC/libp11"
source = f"{url}/releases/download/libp11-{pkgver}/libp11-{pkgver}.tar.gz"
sha256 = "9292de67ca73aba1deacf577c9086b595765f36ef47712cfeb49fa31f6e772fb"
# test suite requires softhsm which is not in repo
options = ["!check"]


@subpackage("libp11-devel")
def _(self):
    return self.default_devel()
