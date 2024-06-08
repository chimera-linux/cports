pkgname = "libgcrypt"
pkgver = "1.10.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-static",
    "--without-capabilities",
    "ac_cv_sys_symbol_underscore=no",
]
configure_gen = ["./autogen.sh"]
hostmakedepends = [
    "automake",
    "libgpg-error-devel",  # for gpg-error.m4
    "libtool",
    "pkgconf",
]
makedepends = ["libgpg-error-devel"]
pkgdesc = "GNU cryptographic library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gnupg.org"
source = f"{url}/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "8b0870897ac5ac67ded568dcfadf45969cfa8a6beb0fd60af2a9eadc2a3272aa"
options = ["linkundefver"]


def post_extract(self):
    # ancient dogshit
    self.rm("m4/gpg-error.m4")


@subpackage("libgcrypt-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/info"])


@subpackage("libgcrypt-progs")
def _progs(self):
    return self.default_progs()
