pkgname = "libgpg-error"
pkgver = "1.55"
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
sha256 = "95b178148863f07d45df0cea67e880a79b9ef71f5d230baddc0071128516ef78"


def post_install(self):
    self.uninstall("usr/share/common-lisp")


@subpackage("libgpg-error-devel")
def _(self):
    return self.default_devel()


@subpackage("libgpg-error-progs")
def _(self):
    return self.default_progs()
