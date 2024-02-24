pkgname = "libgpg-error"
pkgver = "1.48"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
pkgdesc = "Library for error values used by GnuPG components"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gnupg.org"
source = f"{url}/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "89ce1ae893e122924b858de84dc4f67aae29ffa610ebf668d5aa539045663d6f"
# needs qemu and patching
options = ["!cross"]


def post_install(self):
    self.rm(self.destdir / "usr/share/common-lisp", recursive=True)


@subpackage("libgpg-error-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libgpg-error-progs")
def _progs(self):
    return self.default_progs()
