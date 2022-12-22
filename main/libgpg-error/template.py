pkgname = "libgpg-error"
pkgver = "1.46"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Library for error values used by GnuPG components"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gnupg.org"
source = f"{url}/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "b7e11a64246bbe5ef37748de43b245abd72cfcd53c9ae5e7fc5ca59f1c81268d"
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

# FIXME visibility
hardening = ["!vis"]
