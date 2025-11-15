pkgname = "libgpg-error"
pkgver = "1.56"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
    "slibtool",
]
pkgdesc = "Library for error values used by GnuPG components"
license = "LGPL-2.1-or-later"
url = "https://www.gnupg.org"
source = f"{url}/ftp/gcrypt/libgpg-error/libgpg-error-{pkgver}.tar.bz2"
sha256 = "82c3d2deb4ad96ad3925d6f9f124fe7205716055ab50e291116ef27975d169c0"


def post_install(self):
    self.uninstall("usr/share/common-lisp")


@subpackage("libgpg-error-devel")
def _(self):
    return self.default_devel()


@subpackage("libgpg-error-progs")
def _(self):
    return self.default_progs()
