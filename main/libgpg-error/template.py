pkgname = "libgpg-error"
pkgver = "1.51"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
    "slibtool",
]
pkgdesc = "Library for error values used by GnuPG components"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gnupg.org"
source = f"{url}/ftp/gcrypt/libgpg-error/libgpg-error-{pkgver}.tar.bz2"
sha256 = "be0f1b2db6b93eed55369cdf79f19f72750c8c7c39fc20b577e724545427e6b2"


def post_install(self):
    self.uninstall("usr/share/common-lisp")


@subpackage("libgpg-error-devel")
def _(self):
    return self.default_devel()


@subpackage("libgpg-error-progs")
def _(self):
    return self.default_progs()
