pkgname = "libgpg-error"
pkgver = "1.50"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
pkgdesc = "Library for error values used by GnuPG components"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gnupg.org"
source = f"{url}/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "69405349e0a633e444a28c5b35ce8f14484684518a508dc48a089992fe93e20a"


def post_install(self):
    self.uninstall("usr/share/common-lisp")


@subpackage("libgpg-error-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libgpg-error-progs")
def _progs(self):
    return self.default_progs()
