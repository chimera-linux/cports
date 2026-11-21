pkgname = "gpgme"
pkgver = "2.3.1"
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
sha256 = "2bf94e0e677e5a8fc31f79dd323f91c5416b36fb851058bc1e8bce39f2642434"


@subpackage("gpgme-devel")
def _(self):
    return self.default_devel()
