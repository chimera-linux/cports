pkgname = "libgpg-error"
pkgver = "1.61"
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
sha256 = "7a85413f2bc354f4f8aa832b718af122e48965e9e0eb9012ee659c13c6385c93"


def post_install(self):
    self.uninstall("usr/share/common-lisp")


@subpackage("libgpg-error-devel")
def _(self):
    return self.default_devel()


@subpackage("libgpg-error-progs")
def _(self):
    return self.default_progs()
