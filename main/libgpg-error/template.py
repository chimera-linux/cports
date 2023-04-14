pkgname = "libgpg-error"
pkgver = "1.47"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Library for error values used by GnuPG components"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gnupg.org"
source = f"{url}/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "9e3c670966b96ecc746c28c2c419541e3bcb787d1a73930f5e5f5e1bcbbb9bdb"
# needs qemu and patching
options = ["!cross"]

def post_install(self):
    self.rm(self.destdir / "usr/share/common-lisp", recursive = True)

@subpackage("libgpg-error-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libgpg-error-progs")
def _progs(self):
    return self.default_progs()
