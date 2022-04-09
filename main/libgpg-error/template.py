pkgname = "libgpg-error"
pkgver = "1.45"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Library for error values used by GnuPG components"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gnupg.org"
source = f"{url}/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "570f8ee4fb4bff7b7495cff920c275002aea2147e9a1d220c068213267f80a26"
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
