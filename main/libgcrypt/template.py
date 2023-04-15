pkgname = "libgcrypt"
pkgver = "1.10.2"
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
sha256 = "3b9c02a004b68c256add99701de00b383accccf37177e0d6c58289664cce0c03"

@subpackage("libgcrypt-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/share/info"])

@subpackage("libgcrypt-progs")
def _progs(self):
    return self.default_progs()
