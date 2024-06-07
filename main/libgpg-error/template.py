pkgname = "libgpg-error"
pkgver = "1.49"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
pkgdesc = "Library for error values used by GnuPG components"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gnupg.org"
source = f"{url}/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "8b79d54639dbf4abc08b5406fb2f37e669a2dec091dd024fb87dd367131c63a9"


def post_install(self):
    self.rm(self.destdir / "usr/share/common-lisp", recursive=True)


@subpackage("libgpg-error-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libgpg-error-progs")
def _progs(self):
    return self.default_progs()
