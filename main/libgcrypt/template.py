pkgname = "libgcrypt"
pkgver = "1.9.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-static", "--without-capabilities",
    "ac_cv_sys_symbol_underscore=no"
]
hostmakedepends = ["pkgconf"]
makedepends = ["libgpg-error-devel"]
pkgdesc = "GNU cryptographic library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gnupg.org"
source = f"{url}/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "ea849c83a72454e3ed4267697e8ca03390aee972ab421e7df69dfe42b65caaf7"

@subpackage("libgcrypt-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/share/info"])

@subpackage("libgcrypt-progs")
def _progs(self):
    return self.default_progs()
