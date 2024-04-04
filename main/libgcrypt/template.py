pkgname = "libgcrypt"
pkgver = "1.10.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-static",
    "--without-capabilities",
    "ac_cv_sys_symbol_underscore=no",
]
hostmakedepends = ["pkgconf", "libgpg-error-devel"]
makedepends = ["libgpg-error-devel"]
pkgdesc = "GNU cryptographic library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gnupg.org"
source = f"{url}/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "8b0870897ac5ac67ded568dcfadf45969cfa8a6beb0fd60af2a9eadc2a3272aa"
options = ["linkundefver"]


def init_configure(self):
    with self.profile("host"):
        self.make_build_args += ["CC_FOR_BUILD=" + self.get_tool("CC")]


@subpackage("libgcrypt-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/info"])


@subpackage("libgcrypt-progs")
def _progs(self):
    return self.default_progs()


configure_gen = []
