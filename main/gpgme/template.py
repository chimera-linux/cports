pkgname = "gpgme"
pkgver = "2.0.1"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gnupg",
    "libtool",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "libassuan-devel",
    "libgpg-error-devel",
    "python-devel",
]
depends = ["gnupg"]
pkgdesc = "GnuPG Made Easy"
license = "GPL-3.0-or-later"
url = "https://gnupg.org/software/gpgme/index.html"
source = f"https://gnupg.org/ftp/gcrypt/gpgme/gpgme-{pkgver}.tar.bz2"
sha256 = "821ab0695c842eab51752a81980c92b0410c7eadd04103f791d5d2a526784966"


@subpackage("gpgme-devel")
def _(self):
    return self.default_devel()
