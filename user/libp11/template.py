pkgname = "libp11"
pkgver = "0.4.16"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["openssl3-devel", "pkcs11-helper-devel"]
pkgdesc = "Library implementing a small layer between OpenSSL and PKCS#11"
license = "LGPL-2.1-or-later"
url = "https://github.com/OpenSC/libp11"
source = f"{url}/releases/download/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "97777640492fa9e5831497e5892e291dfbf39a7b119d9cb6abb3ec8c56d17553"
# test suite requires softhsm which is not in repo
options = ["!check"]


@subpackage("libp11-devel")
def _(self):
    return self.default_devel()
