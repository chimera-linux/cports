pkgname = "libgpg-error"
pkgver = "1.59"
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
sha256 = "a19bc5087fd97026d93cb4b45d51638d1a25202a5e1fbc3905799f424cfa6134"


def post_install(self):
    self.uninstall("usr/share/common-lisp")


@subpackage("libgpg-error-devel")
def _(self):
    return self.default_devel()


@subpackage("libgpg-error-progs")
def _(self):
    return self.default_progs()
